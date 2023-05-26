from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET
from django.db.models.functions import ExtractHour, ExtractMinute, TruncMinute
from django.db.models import Count,DateTimeField
from datetime import datetime, timedelta
from .models import Event
from .models import Context
from django.utils import timezone
from django.db.models import Q



@require_GET
def get_first_10_Events(request):
    records = Event.objects.all()[:10]
    data = [{'id': record.id,
             'course_id': record.context.course_id,
             'username': record.username,
             'session': record.session,
             'agent': record.agent,
             'host': record.host,
             'time': record.time,
             'event': record.event,
             'event_type': record.event_type,
             'event_source': record.event_source,
             'page': record.page
             } for record in records]
    return JsonResponse(data, safe=False)


def get_filtered_events(request):
    username = request.GET.get('username')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    course_key = request.GET.get('course_key')
    event_type = request.GET.get('event_type')
    event_source = request.GET.get('event_source')

    events = Event.objects.all()

    if username:
        events = events.filter(username=username)
    if start_date:
        events = events.filter(time__gte=start_date)
    if end_date:
        events = events.filter(time__lte=end_date)
    if course_key:
        events = events.filter(context__course_id=course_key)
    if event_type:
        events = events.filter(event_type=event_type)
    if event_source:
        events = events.filter(event_source=event_source)

    data = [
        {
            'username': event.username,
            'event_type': event.event_type,
            'event_source': event.event_source,
            # Agrega otros campos que desees mostrar en la respuesta
        }
        for event in list(events)
        
    ]
    return JsonResponse(data, status=200, safe=False)

def get_event_count_data(time_unit, start_time, end_time):
    if time_unit not in ['hours', 'minutes']:
        raise ValueError(f'Invalid time unit: {time_unit}')

    try:
        start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        end_time = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        raise ValueError(f'Invalid date format: {start_time} or {end_time}')



    if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
        return JsonResponse({'error': 'Invalid date format'}, status=400)

    events = Event.objects.filter(time__gte=start_time,time__lte=end_time )
    annotated_events = events.annotate(
        count=Count('id', db_column='event_count')
    ).values('count')

    if time_unit == 'hours':
        grouped_events = annotated_events.annotate(
            hour=ExtractHour('time')).values('hour', 'count')
    else:
        grouped_events = annotated_events.annotate(
            minute=ExtractMinute('time')).values('minute', 'count')

    data = [
        {
            'time': event['hour'] if time_unit == 'hours' else event['minute'],
            'count': event['count']
        }
        for event in grouped_events
    ]

    return data


@require_GET
def get_event_count(request):
    time_unit = request.GET.get('time_unit')
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')

    try:
        data = get_event_count_data(time_unit, start_time, end_time)
        return JsonResponse(data, safe=False)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)




def count_events_per_minute(request):
    # Obtener la fecha del día
    dayD = datetime(2023, 4, 3).date() # theres some data from 2023-4-2
    # Calcular la fecha de inicio y fin del día
    start_time = datetime.combine(dayD, datetime.min.time())
    end_time = start_time + timedelta(days=1)
    start_time = timezone.make_aware(start_time, timezone.get_default_timezone())
    end_time = timezone.make_aware(end_time, timezone.get_default_timezone())


    # Filtrar los eventos del día
    events = Event.objects.filter(time__range=(start_time, end_time))
    # Agrupar los eventos por minuto y contar
    grouped_events = events.annotate(minute=TruncMinute('time', output_field=DateTimeField())) \
                          .values('minute') \
                          .annotate(count=Count('id'))

    # Crear un arreglo de 1440 minutos del día
    minutos_del_dia = [0] * 1440

    # Rellenar el arreglo con la cuenta de eventos correspondiente
    for evento in grouped_events:
        minuto = (evento['minute'] - start_time).seconds // 60
        minutos_del_dia[minuto] = evento['count']

    # Devolver la respuesta como JSON
    return JsonResponse(minutos_del_dia, safe=False)

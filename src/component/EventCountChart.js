import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';

const EventCountChart = () => {
    const [chartData, setChartData] = useState(null);

    useEffect(() => {
        // Llamar al endpoint para obtener los datos
        fetch('http://localhost:8000/count_events_per_minute/')
            .then((response) => response.json())
            .then((data) => {
                // Preparar los datos para el gráfico
                const groupedData = [];
                for (let i = 0; i < data.length; i += 10) {
                    const group = data.slice(i, i + 10);
                    const sum = group.reduce((total, item) => total + item, 0);
                    groupedData.push(sum);
                }

                const labels = [];
                for (let i = 0; i < 144; i++) {
                    const minutes = i * 10;
                    const hours = Math.floor(minutes / 60).toString().padStart(2, '0');
                    const mins = (minutes % 60).toString().padStart(2, '0');
                    labels.push(`${hours}:${mins}`);
                }
                console.log(groupedData);
                console.log(labels);

                // Configuración del gráfico
                const chartData = {
                    labels,
                    datasets: [
                        {
                            label: 'Suma de eventos',
                            data: groupedData,
                            fill: false,
                            borderColor: 'rgba(75,192,192,1)',
                            tension: 0.1,
                        },
                    ],
                };

                // Opciones de configuración del gráfico
                const options = {
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Hora',
                            },
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Suma',
                            },
                        },
                    },
                };

                // Actualizar el estado del gráfico
                setChartData({ data: chartData, options });
            });
    }, []);

    return (
        <div>
            {chartData ? (
                <div>
                    <h2>Eventos totales del 3 de abril</h2>
                    <Line data={chartData.data} options={chartData.options} />
                </div>
            ) : (
                <p>Cargando datos...</p>
            )}
        </div>
    );
};

export default EventCountChart;

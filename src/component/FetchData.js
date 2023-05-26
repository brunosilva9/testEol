export const groupedDataFeched = async () => {
    try {
        const response = await fetch('http://localhost:8000/count_events_per_minute/');
        const data = await response.json();
        // Preparar los datos para el gráfico
        let groupedData = [];
        let labels = [];
        for (let i = 0; i < data.length; i += 10) {
            const group = data.slice(i, i + 10);
            const sum = group.reduce((total, item) => total + item, 0);
            groupedData.push(sum);
        }
        for (let i = 0; i < 144; i++) {
            const minutes = i * 10;
            const hours = Math.floor(minutes / 60).toString().padStart(2, '0');
            const mins = (minutes % 60).toString().padStart(2, '0');
            labels.push(`${hours}:${mins}`);
        }

        return { groupedData, labels };
    } catch (err) {
        console.log(err);
    }
};

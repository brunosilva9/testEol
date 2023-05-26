import React, { useState, useEffect } from "react";
import { Chart } from "chart.js";

const GraphComponentWithFilter = ({ data }) => {
    const [filteredData, setFilteredData] = useState([]);

    useEffect(() => {
        // Filtrar los datos según el curso seleccionado
        const filtered = data.filter(item =>  console.log(item));
       ;
        setFilteredData(filtered);
    }, [data]);

    useEffect(() => {
        // Crear el gráfico cuando los datos filtrados estén listos
        if (filteredData.length > 0) {
            createChart();
        }
    }, [filteredData]);

    const createChart = () => {
        // Obtener las etiquetas y valores para el gráfico
        const labels = filteredData.map(item => item.etiqueta);
        const values = filteredData.map(item => item.valor);

        // Configurar el gráfico
        const ctx = document.getElementById("chart").getContext("2d");
        new Chart(ctx, {
            type: "bar",
            data: {
                labels: labels,
                datasets: [
                    {
                        label: "Valores",
                        data: values,
                        backgroundColor: "rgba(75, 192, 192, 0.2)",
                        borderColor: "rgba(75, 192, 192, 1)",
                        borderWidth: 1,
                    },
                ],
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                    },
                },
            },
        });
    };

    return (
        <div>
            <h1>GraphComponentWithFilter</h1>
            <canvas id="chart" width="400" height="200"></canvas>
        </div>
    );
};

export default GraphComponentWithFilter;

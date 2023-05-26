import React, { useEffect, useState } from "react";
import { groupedDataFeched } from "./FetchData";
import { Line } from "react-chartjs-2";
import { CategoryScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend } from 'chart.js';
import Chart from "chart.js/auto";
Chart.register(CategoryScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend);
const EventCountChart = () => {
    const [data, setData] = useState([]);
    const [labels, setLabels] = useState([]);
    const [startTime, setStartTime] = useState(0);
    const [endTime, setEndTime] = useState(143);

    useEffect(() => {
        const fetchData = async () => {
            const { groupedData, labels } = await groupedDataFeched();
            setData(groupedData);
            setLabels(labels);
        };

        fetchData();
    }, []);

    const filteredData = data.slice(startTime, endTime + 1);
    const filteredLabels = labels.slice(startTime, endTime + 1);

    const handleStartTimeChange = (value) => {
        if (value <= endTime) {
            setStartTime(value);
        }
    };

    const handleEndTimeChange = (value) => {
        if (value >= startTime) {
            setEndTime(value);
        }
    };

    const eventCountChart = (
        <div style={{ width: "100%", height: "100%" }}>
            <Line
                data={{
                    labels: filteredLabels,
                    datasets: [
                        {
                            data: filteredData,
                            label: "Events Count",
                            borderColor: "rgb(0, 217, 255)",
                            fill: true,
                        },
                    ],
                }}
            />
        </div>
    );

    return (
        <div>
            <div>
                <label htmlFor="startTime">Start Time:</label>
                <input
                    type="range"
                    id="startTime"
                    value={startTime}
                    min={0}
                    max={endTime}
                    onChange={(e) => handleStartTimeChange(Number(e.target.value))}
                />
                <span>{labels[startTime]}</span>
            </div>
            <div>
                <label htmlFor="endTime">End Time:</label>
                <input
                    type="range"
                    id="endTime"
                    value={endTime}
                    min={startTime}
                    max={143}
                    onChange={(e) => handleEndTimeChange(Number(e.target.value))}
                />
                <span>{labels[endTime]}</span>
            </div>
            <div>{eventCountChart}</div>
        </div>
    );
};

export default EventCountChart;
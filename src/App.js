import "./App.css";
import React, { useEffect, useState } from "react";
import GraphComponentWithFilter from "./component/GraphComponentWithFilter";
import EventCountChart from "./component/EventCountChart.js";
import mock from "./mock_data/data.json"; // to Do ELIMinate


const SERVER_URL = 'http://localhost:8000';

const App = () => {
  const [data, setData] = useState([mock]);
  const [eventsPerMinute, setEventsPerMinute] = useState([]);
  //setData(mock); // to Do ELIMinate

  useEffect(() => {
    console.log("tratando de acceder al end point")

    fetch(`${SERVER_URL}/count_events_per_minute/`)
      .then((data) => {
        console.log(data);
        setEventsPerMinute(data);
      })
      .catch((error) => {
        // Manejar errores
      });
    // load mock  


  }, []);

  return (
    <div className="App">
      <header className="App-header">

        <EventCountChart />
        <GraphComponentWithFilter data={data} />
      </header>
    </div>
  );
}

export default App;

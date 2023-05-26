import React, { useState } from "react";
import GraphComponentWithFilter from "./component/GraphComponentWithFilter";
import EventCountChart from "./component/EventCountChart.js";
import mock from "./mock_data/data.json"; // ELIMINAR
import Switch from "react-switch";

const App = () => {
  const [isEventCountChartVisible, setIsEventCountChartVisible] = useState(true);
  const toggleChart = () => {
    setIsEventCountChartVisible(!isEventCountChartVisible);
  };

  return (
    <div className="App">
      <header className="App-header">
        <div>
          <div style={{ height: "100vh", display: "flex", flexDirection: "column" }}>
            {isEventCountChartVisible ? (
              <EventCountChart  />
            ) : (
              <GraphComponentWithFilter data={mock} />
            )}
          </div>
          <div style={{ textAlign: "center", marginBottom: "20px" }}>
            <Switch
              onChange={toggleChart}
              checked={isEventCountChartVisible}
              onColor="#86d3ff"
              onHandleColor="#2693e6"
              handleDiameter={30}
              uncheckedIcon={false}
              checkedIcon={false}
              boxShadow="0px 1px 5px rgba(0, 0, 0, 0.6)"
              activeBoxShadow="0px 0px 1px 10px rgba(0, 0, 0, 0.2)"
              height={20}
              width={48}
              className="react-switch"
              id="toogle"
              aria-label="Toggle Graph"

            />
          </div>
        </div>
      </header>
    </div>
  );
};

export default App;

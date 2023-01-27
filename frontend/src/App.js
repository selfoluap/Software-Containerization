import React, { useEffect, useState } from "react";
import './App.css';

function App() {
  const [data, setData] = useState([]);

  const fetchData = () => {
    return fetch("testtodos.com/api/server/get_tasks")
    .then((response) => 
      response.json())
    .then((data) => setData(data["todos"]))
  }

  useEffect(() => {
    fetchData();
  }, [])

  return (
    <div className="App">
      <header className="App-header">
      <h1>ToDo's v1</h1>
      <ul>
        {data && data.length > 0 && data.map((dataObj, index) => (
            <li key={dataObj.id}>{dataObj.desc} written by {dataObj.author}</li>
          ))}
      </ul>
      </header>
    </div>
  );
}

export default App;

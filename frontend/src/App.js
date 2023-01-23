import React, { useEffect, useState } from "react";
import './App.css';

function App() {
  const [data, setData] = useState([]);

  const fetchData = () => {
    return fetch("/api/v1.0/todos")
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
      <h1>ToDo's v4</h1>
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

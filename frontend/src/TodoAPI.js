import './App.css';
import React, { useEffect, useState } from "react";

function TodoAPI() {
  
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');


  //GET METHOD
  useEffect(() => {
     fetch('http://api.backend.com/server/get_tasks')
        .then((response) => response.json())
        .then((data) => {
           console.log(data);
           setTodos(data["todos"]);
        })
        .catch((err) => {
           console.log(err.message);
        });
  }, []);

    //POST METHOD
    const addTodos = async (title, body) => {
       await fetch('https://jsonplaceholder.typicode.com/posts', {
          method: 'POST',
          body: JSON.stringify({
             //id: Math.random().toString(36).slice(2), ***ID???***
             title: title,
             body: body
          }),
          headers: {
             'Content-type': 'application/json; charset=UTF-8',
          },
       })
          .then((response) => response.json())
          .then((data) => {
             setTodos((todos) => [data, ...todos]);
             setTitle('');
             setBody('');
          })
          .catch((err) => {
             console.log(err.message);
          });
    };
    
    const handleSubmit = (e) => {
       e.preventDefault();
       addTodos(title, body);
    };    

    //DELETE METHOD
    const deleteTodo = async (id) => {
      await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`, {
         method: 'DELETE',
      }).then((response) => {
         if (response.status === 200) {
            setTodos(
               todos.filter((todo) => {
                  return todo.id !== id;
               })
            );
         } else {
            return;
         }
      });
      };
  
  return (
   <div className="todo-container">
      <h1>What's the plan for today?</h1>
      <div className="add-todo-container">
             <form onSubmit={handleSubmit}>
                <input type="text" className="add-todo-title" placeholder="Add title of todo" value={title}
                   onChange={(e) => setTitle(e.target.value)}
                />
                
                <textarea name="" className="add-todo-body" placeholder="Add description" id="" cols="10" rows="8" 
                   value={body} onChange={(e) => setBody(e.target.value)} 
                ></textarea>
                <button className="add-btn" type="submit">Add todo</button>
             </form>
      </div>
      <hr/>
      <div className="get-todo-container">
         {todos.map((todo) => {
            return (
               <div className="todo" key={todo.id}>
                  <h1 className="todo-title">{todo.author}</h1>
                  <p className="todo-body">{todo.desc}</p>
                  <div className="delete-todo-container">
                     <div className="delete-btn" onClick={() => deleteTodo(todo.id)}>Delete todo</div>
                  </div>
               </div>
            );
         })}
      </div>
   </div>
   
  );
}


export default TodoAPI;

import './App.css';
import React, { useEffect, useState } from "react";

function TodoAPI() {

  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');


  //GET METHOD
  useEffect(() => {
     fetch('/backend/server/get_todos')
        .then((response) => response.json())
        .then((data) => {
           console.log(data);
           setTodos(data);
        })
        .catch((err) => {
           console.log(err.message);
        });
  }, []);


  //POST METHOD
  const addTodos = async (title, description) => {
   await fetch('/backend/server/create_todo', {
      method: 'POST',
      body: JSON.stringify({
         //id: Math.random().toString(36).slice(2), ***ID???***
         title: title,
         description: description
      }),
      headers: {
         'Content-type': 'application/json; charset=UTF-8',
      },
   })
      .then((response) => response.json())
      .then((data) => {
         setTodos((todos) => [data, ...todos]);
         setTitle('');
         setDescription('');
         fetch('/backend/server/get_todos')
        .then((response) => response.json())
        .then((data) => {
           console.log(data);
           setTodos(data);
        })
        .catch((err) => {
           console.log(err.message);
        });
      })
      .catch((err) => {
         console.log(err.message);
      });
};
   
const handleSubmit = (e) => {
   e.preventDefault();
   addTodos(title, description);
}; 


//DELETE METHOD
const deleteTodo = async (id) => {
   await fetch(`/backend/server/delete_todo/${id}`, {
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

                <textarea name="" className="add-todo-description" placeholder="Add description" id="" cols="10" rows="8" 
                   value={description} onChange={(e) => setDescription(e.target.value)} 
                ></textarea>
                <button className="add-btn" type="submit">Add todo</button>
             </form>
      </div>
      <hr/>
      <div className="get-todo-container">
         {todos?.map((todo) => {
            return (
               <div className="todo" key={todo?.id}>
                  <h1 className="todo-title">{todo?.title}</h1>
                  <p className="todo-description">{todo?.description}</p>
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
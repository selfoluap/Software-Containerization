import React, {useState, useEffect, useRef} from 'react';
import props from 'prop-types';

function TodoForm(props) {
  const[input, setInput] = useState(props.edit ? props.edit.value : ''); //input field is not gonna clear out after selecting for update

  const inputRef = useRef(null);

  //focus on current input field
  useEffect(() => {
    inputRef.current.focus();
  })

  const handleChange = e => {
    setInput(e.target.value);
  }

  //stop refreshing after submiting form
  const handleSubmit = e => {
    e.preventDefault();

    props.onSubmit({
        id: Math.floor(Math.random() * 10000),
        text: input
    });

    setInput("");
  };

  return (
    <form className="todo-form" onSubmit={handleSubmit}>
        {props.edit ? ( 
            <>
        <input 
            type="text" 
            placeholder="Update selected todo" 
            value={input} 
            name="text" 
            className="todo-input edit"
            onChange={handleChange}
            ref={inputRef}
        />
        <button className="todo-button edit">Update todo</button>
        </>) : 
        (
            <> <input 
            type="text" 
            placeholder="Add a todo" 
            value={input} 
            name="text" 
            className="todo-input"
            onChange={handleChange}
            ref={inputRef}
        />
        <button className="todo-button">Add todo</button>
        </>)}
    </form>
  );
}

export default TodoForm
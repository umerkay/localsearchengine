import React from 'react'
import { Link } from 'react-router-dom'

export default function Header({name, setName}) {
  return (
    <header className={"App-header"}>
      <div className='con'>
        <span className="title">
          <span> Hello,</span>
          <input type={"text"} onInput={setName} spellCheck={false} value={name}></input>
        </span>
        <span className="details">
          <span>This project has been made as part of the coursework required for CS250 Data Structures & Algorithms.
          The project demonstrates text indexing and querying capabilities.</span>
          <a href="https://github.com/umerkay/localsearchengine">Visit GitHub</a>
          <span>Made with 💖 by <a href="https://umerkay.github.io">Umerkay</a></span>
        </span>
      </div>
    </header>
  )
}
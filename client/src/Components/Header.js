import React from 'react'
import { Link } from 'react-router-dom'

export default function Header({ focus }) {
  return (
    <header className={"App-header" + (focus ? " focus" : "")}>
      <Link style={{ color: "white", textDecoration: "none", fontWeight: "bold" }} to="/" className="title">Watch<span className='primary'>Today</span></Link>
      <span className="details">
        Can not decide which movie to watch today? You are in the right place
        <br></br>
        <span className="info">This application is only a demonstration of Umer's frontend skills with React, a JavaScript framework</span>
        <br></br>
        <a style={{ color: "white", textDecoration: "none", fontSize: "1rem" }} href="https://umerkay.github.io">Click here to get back to my portfolio</a>
      </span>
    </header>
  )
}
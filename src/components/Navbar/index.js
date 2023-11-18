import React from 'react'
import "./Navbar.css"
import { Link } from 'react-router-dom'
export default function Navbar() {
  return (
    <nav>
      <ul>
        <li>
        <Link className='link' to="/calendar">Calendar</Link>
        </li>
      <li>
        <Link className='link' to="/profile">Profile</Link>
      </li>
      </ul>
    </nav>
  )
}

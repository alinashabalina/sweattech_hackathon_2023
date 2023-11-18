import React from 'react'
import { Link } from 'react-router-dom'
export default function Navbar() {
  return (
    <div>
        {/* <Link to="/">Form</Link> */}
        <Link to="/calendar">Calendar</Link>
        <Link to="/profile">Profile</Link>
    </div>
  )
}

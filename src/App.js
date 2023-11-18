import React from 'react'
import Form from './components/Form'
import Calendar from './components/Calendar'
import Navbar from './components/Navbar'
import Profile from './components/Profile'
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";

export default function App() {
  return (
    <>
    <Router>
      <Routes>
        <Route exact path="/" element={<Form />}></Route>
        <Route exact path="/calendar" element={<Calendar />}></Route>
        <Route exact path="/profile" element={<Profile />}></Route>
      </Routes>
    <Navbar />
    </Router>
    </>
  )
}

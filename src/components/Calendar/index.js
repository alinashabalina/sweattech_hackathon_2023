import React, { useState } from 'react'
import DayView from '../DayView';
import {DateCalendar} from '@mui/x-date-pickers/DateCalendar';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';

export default function Calendar() {
  const [clicked, setClicked] = useState(false)
  return (
    <>
    <LocalizationProvider dateAdapter={AdapterDayjs}>
        <DateCalendar onClick={()=>setClicked(true)} />
    </LocalizationProvider>
    {clicked && <DayView />}
    </>
  )
}

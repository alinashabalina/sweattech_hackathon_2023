import React from 'react'
import {DateCalendar} from '@mui/x-date-pickers/DateCalendar';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';

export default function Calendar() {
  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
        <DateCalendar />
    </LocalizationProvider>
  )
}

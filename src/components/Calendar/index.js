import React, { useState } from 'react'
import {DateCalendar} from '@mui/x-date-pickers/DateCalendar';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import dayjs from 'dayjs';

export default function Calendar() {
  const [value, setValue] = useState(dayjs)
  console.log(value);
  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
        <DateCalendar value={value} onChange={(newValue)=>setValue(newValue)} />
    </LocalizationProvider>
  )
}

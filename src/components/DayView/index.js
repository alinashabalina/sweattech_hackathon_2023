import React, { useState } from 'react'
import "./DayView.css"
export default function DayView() {
    const [submitted, setSubmitted] = useState(false);

    function getTheDate(){
        const currentDate = new Date();

        const year = currentDate.getFullYear() % 100; // Get the current year (e.g., 2023)
        const month = currentDate.getMonth() + 1; // Get the current month (January is 0, so add 1)
        const day = currentDate.getDate(); // Get the current day of the month
        
        // Format the date components if needed (to ensure double digits for month/day if < 10)
        const formattedMonth = month < 10 ? `0${month}` : month;
        const formattedDay = day < 10 ? `0${day}` : day;
        
        // Create a string in the format YYYY-MM-DD
        const formattedDate = `${formattedDay}${formattedMonth}${year}`;
        console.log(formattedDate); // Output: e.g., "181123"
        return formattedDate
    }

    function handleSubmit(e){
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = Object.fromEntries(formData);
        console.log(data);
        const date= getTheDate();
        const dataToSend = {date: date, ...data};
        console.log("dataToSend", dataToSend)
        setSubmitted(true);
    }


  return (
    <>
    <form onSubmit={handleSubmit}>
        <p>Did your period start on time?</p>
       <input type="radio" id="yes" name="periodDay" value={true} />
        <label htmlFor="yes">Yes</label><br/>
        <input type="radio" id="no" name="periodDay" value={false} />
       <label htmlFor="no">No</label><br/>

       <p>What's your energy level?</p>
       <input type="radio" id="energetic" name="dayEnergy" value="energetic" />
        <label htmlFor="energetic">energetic</label><br/>
        <input type="radio" id="strong" name="dayEnergy" value="strong" />
       <label htmlFor="strong">strong</label><br/>
       <input type="radio" id="relaxed" name="trainidayEnergyngChosen" value="relaxed" />
        <label htmlFor="relaxed">relaxed</label><br/>
        <input type="radio" id="tired" name="dayEnergy" value="tired" />
       <label htmlFor="tired">tired</label><br/>

       <p>Where do you prefer to work out?</p>
       <input type="radio" id="home" name="trainingType" value="home" />
        <label htmlFor="home">At home</label><br/>
        <input type="radio" id="gym" name="trainingType" value="gym" />
       <label htmlFor="gym">At the gym</label><br/>
        <input type="radio" id="skip" name="trainingType" value="skip" />
       <label htmlFor="skip">Skip for today</label><br/>
       <button type='submit'>Submit</button>
    </form>
    {submitted && 
    <>
    <h3>Play the video:</h3>
    <iframe className='video' width={400} height={315} src="https://www.youtube.com/embed/g_tea8ZNk5A?si=Lnu60c_2g-cJMtkJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </>}
    </>
  )
}

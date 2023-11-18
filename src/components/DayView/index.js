import React, { useState } from 'react'

export default function DayView() {
    const [submitted, setSubmitted] = useState(false);

    function handleSubmit(e){
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = Object.fromEntries(formData);
        console.log(data);
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
    </>}
    </>
  )
}

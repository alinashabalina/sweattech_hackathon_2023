import React, { useState } from 'react'

export default function Form() {
    // const [question, setQuestion] = useState(1)
    // console.log({question});

    // const [userData, setUserData] = useState({})
    
    
    function handleSubmit(e){
        e.preventDefault();
        // setQuestion(question => question+1);
        const formData = new FormData(e.target);
        const data = Object.fromEntries(formData);
        // setUserData({...userData, : newdata})
        console.log(data);
    }

  return (
    <form onSubmit={handleSubmit}>
        {/* {question === 1 &&
        <> */}
        <label htmlFor="dateOfBirth">Date of Birth</label>
        <input type="date" id='dateOfBirth' name='dateOfBirth' />
        {/* <button type="submit">next</button> */}
        {/* </>}
        {question === 2 &&
        <> */}
        <label htmlFor="hormoneState">Which hormone state would you say you are in now?</label>
        <select id='hormoneState' name='hormoneState'>
        <option value="">-- Choose --</option>
        <option value="menstruation">menstruation</option>
        <option value="pregnancy">pregnancy</option>
        <option value="menopause">menopause</option>
        </select>
        {/* <button type='submit'>next</button> */}
        {/* </>}
        {question === 3 &&
        <> */}
        <label htmlFor="dayOfCycle">Which day in your cycle are you in now?</label>
        <input type="number" id='dayOfCycle' name='dayOfCycle' min="1" max="28" />
        {/* <button type='submit'>next</button> */}
        {/* </>}
        {question === 4 &&
        <> */}
        <label htmlFor="goal">What is your primary goal of working out?</label>
        <select id='goal' name='goal'>
        <option value="">-- Choose --</option>
        <option value="weightloss">healthy weight loss</option>
        <option value="health">general health</option>
        <option value="strength">strength</option>
        <option value="mobility">mobility and flexibility</option>
        <option value="stamina">stamina and endurance</option>
        </select>
        
        <button type='submit'>Submit</button>
        {/* </>} */}
    </form>
  )
}

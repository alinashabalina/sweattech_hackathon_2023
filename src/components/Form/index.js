import React, { useState } from 'react'
import "./Form.css"

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
        <section>
        <label htmlFor="dateOfBirth">Date of Birth</label><br/>
        <input type="date" id='dateOfBirth' name='dateOfBirth' />
        </section>
        <section>
        <label htmlFor="hormoneState">Which hormone state would you say you are in now?</label><br/>
        <select id='hormoneState' name='hormoneState'>
        <option value="">-- Choose --</option>
        <option value="menstruation">menstruation</option>
        <option value="pregnancy">pregnancy</option>
        <option value="menopause">menopause</option>
        </select>
        </section>

        <section>
        <label htmlFor="dayOfCycle">Which day in your cycle are you in now?</label><br/>
        <input type="number" id='dayOfCycle' name='dayOfCycle' min="1" max="28" />
        </section>

        <section>
        <label htmlFor="goal">What is your primary goal of working out?</label><br/>
        <select id='goal' name='goal'>
        <option value="">-- Choose --</option>
        <option value="weightloss">healthy weight loss</option>
        <option value="health">general health</option>
        <option value="strength">strength</option>
        <option value="mobility">mobility and flexibility</option>
        <option value="stamina">stamina and endurance</option>
        </select>
        </section>

        <button type='submit'>Submit</button>
    </form>
  )
}

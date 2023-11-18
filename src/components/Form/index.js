import React from 'react'

export default function Form() {
    function handleSubmit(e){
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = Object.fromEntries(formData);
        console.log(data);
    }

  return (
    <form onSubmit={handleSubmit}>
        <label htmlFor="dateOfBirth">Date of Birth</label>
        <input type="date" id='dateOfBirth' name='dateOfBirth' />

        <label htmlFor="hormoneState">Which hormone state would you say you are in now?</label>
        <select id='hormoneState' name='hormoneState'>
        <option value="">-- Choose --</option>
        <option value="menstruation">menstruation</option>
        <option value="pregnancy">pregnancy</option>
        <option value="menopause">menopause</option>
        </select>

        <label htmlFor="dayOfCycle">Which day in your cycle are you in now?</label>
        <input type="number" id='dayOfCycle' name='dayOfCycle' min="1" max="28" />

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
    </form>
  )
}

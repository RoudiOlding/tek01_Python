const convertToCelsiusButton = document.getElementById('convertToCelsius');
const convertToFahrenheitButton = document.getElementById('convertToFahrenheit');
const backToHomeButton = document.getElementById('backToHome');
const inputTemperature = document.getElementById('inputTemperature');

// Initial state: Hide the "Back to Home" button
backToHomeButton.classList.add('hidden');

convertToCelsiusButton.addEventListener('click', () => {
    // Hide input and conversion buttons
    inputTemperature.classList.add('hidden');
    convertToCelsiusButton.classList.add('hidden');
    convertToFahrenheitButton.classList.add('hidden');

    // Show "Back to Home" button
    backToHomeButton.classList.remove('hidden');

    alert('Converted to Celsius!');
});

convertToFahrenheitButton.addEventListener('click', () => {
    // Hide input and conversion buttons
    inputTemperature.classList.add('hidden');
    convertToCelsiusButton.classList.add('hidden');
    convertToFahrenheitButton.classList.add('hidden');

    // Show "Back to Home" button
    backToHomeButton.classList.remove('hidden');

    alert('Converted to Fahrenheit!');
});

backToHomeButton.addEventListener('click', () => {
    // Show input and conversion buttons
    inputTemperature.classList.remove('hidden');
    convertToCelsiusButton.classList.remove('hidden');
    convertToFahrenheitButton.classList.remove('hidden');

    // Hide "Back to Home" button
    backToHomeButton.classList.add('hidden');

    alert('Going back to home!');
});
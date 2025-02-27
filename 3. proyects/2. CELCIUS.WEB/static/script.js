const convertToCelsiusButton = document.getElementById('convertToCelsius');
const convertToFahrenheitButton = document.getElementById('convertToFahrenheit');
const backToHomeButton = document.getElementById('backToHome');
const inputTemperature = document.getElementById('inputTemperature');
const resultDisplay = document.getElementById('result');
const conversionForm = document.getElementById('conversionForm');

backToHomeButton.classList.add('hidden');

// Function to handle conversion
function handleConversion(url) {
    const formData = new FormData(conversionForm); // Get form data
    fetch(url, {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json()) // Parse JSON response
    .then(data => {
        // Display the result
        resultDisplay.textContent = data.result;

        // Hide input and conversion buttons
        inputTemperature.classList.add('hidden');
        convertToCelsiusButton.classList.add('hidden');
        convertToFahrenheitButton.classList.add('hidden');

        // Show "Back to Home" button
        backToHomeButton.classList.remove('hidden');
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Add event listeners to the conversion buttons
convertToCelsiusButton.addEventListener('click', () => {
    handleConversion('/convertCelsius');
});

convertToFahrenheitButton.addEventListener('click', () => {
    handleConversion('/convertFahrenheit');
});

// Add event listener to the "Back to Home" button
backToHomeButton.addEventListener('click', () => {
    // Show input and conversion buttons
    inputTemperature.classList.remove('hidden');
    convertToCelsiusButton.classList.remove('hidden');
    convertToFahrenheitButton.classList.remove('hidden');

    // Hide "Back to Home" button
    backToHomeButton.classList.add('hidden');

    // Clear the input field
    inputTemperature.value = '';

    // Clear and hide the result
    resultDisplay.textContent = '';
});
document.addEventListener('DOMContentLoaded', function() {
    const cityInput = document.getElementById('cityInput');
    const Enter = document.getElementById('Enter');
    const Result = document.getElementById('Result');
   
    Enter.addEventListener('click', function() {
        const city = cityInput.value;
        if (city.trim() ==='') {
            alert('Please enter a city name.');
            return;
        }
        const apiKey = '481171c0df2ea9d65037ecbecd36bbe2';
        const apiUrl=`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

        fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const temperature = data.main.temp;
            const description = data.weather[0].description;
            const resultText = `Weather in ${city}: ${temperature}°C, ${description}`;
            Result.textContent = resultText;
        })
        .catch(error => {
            console.error('Error fetching weather data.', error);
            Result.textContent = 'No such city found';
        });
    });
});



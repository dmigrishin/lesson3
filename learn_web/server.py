from flask import Flask
from weather import weather_by_city
app = Flask (__name__)

@app.route('/')
def index():
    weather = weather_by_city("Vladivostok, Russia")
    
    if weather:
        return f"Прогноз погоды, температура {weather[0]['temp_C']}, ощущается как {weather[0]['FeelsLikeC']}", 201
    else:
        return "Сервис временно недоступен"

if __name__ == "__main__":
    app.run(debug=True)
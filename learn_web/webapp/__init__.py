from flask import Flask, render_template
from webapp.weather import weather_by_city
from webapp.python_org_news import get_python_news

def create_app():

    app = Flask (__name__)

    @app.route('/')
    def index():
        title = "Новости Python"
        weather = weather_by_city("Vladivostok, Russia")
        news_list = get_python_news()
        return render_template("index.html", page_title = title, weather = weather, news_list = news_list)

    return app
# if __name__ == "__main__":
#     app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
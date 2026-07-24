import random
from flask import Flask

app = Flask(__name__)

# Список дефолтных фактов про Minecraft
mc_facts = [
    "Бедрок имеет прочность 3,600,000 единиц.",
    "Тыквы встречаются реже, чем алмазная руда.",
    "Криперы появились из-за ошибки в коде при создании модели свиньи.",
    "Изначально Minecraft назывался «Cave Game».",
    "Дракон Края официально имеет имя — Джинн (Jean).",
    "Взгляд на эндермена через стекло или тыкву не разозлит его.",
]


@app.route("/")
def hello_world():
    return '<h1>Главная страница</h1><a href="/random_fact">Посмотреть случайный факт!</a>'


@app.route("/random_fact")
def random_fact():
    fact = random.choice(mc_facts)
    return f"<h1>Случайный факт про Minecraft:</h1><p>{fact}</p>"


if __name__ == "__main__":
    app.run(debug=True)
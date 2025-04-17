"""
Numonster
================================================

Numonster.py

This is the main entry-point to the Flask server that powers [Numonster].
"""

import pyhtml as p
from flask import Flask,request

app = Flask(__name__)
characters={"knight":{"life":"120", "physical strength":"20", "magical power":"0", "real power":"5","physical defensive power":"15", "magical defensive power":"5"},
            "monk":{"life":"80", "physical power":"0", "magical power":"20", "real power":"5", "physical defensive power":"5", "magical defensive power":"15"},
            "pioneer":{"life":"100", "physical power":"10", "magical power":"10", "real power":"20", "physical defensive power":"10", "magical defensive power":"10"}
            }
monsters={
    "easy":{
        "small creatures":[
            {"name": "evil goblin", "HP":30,"physical power":5,"magical power":0,"real power": 0,"physical defensive power":5,"magical defensive power":5},
            {"name":"ghost","HP":50,"physical power":"0","magical power":5,"real power":0,"physical defensive power":0,"magical defensive power":5}
        ],
        "boss":{"name":"goblin king","HP":80,"physical power":0,"magical power":0,"real power":5,"physical defensive power":8,"magical defensive power":8}
    },
    "normal":{
        "small creatures":[
            {"name":"orc","HP":40,"physical power":6,"magical power":0,"real power":0,"physical defensive power":6,"magical defensive power":6},
            {"name":"ogre mage","HP":"60","physical power":0,"magical power":8,"real power":0,"physical defensive power":8,"magical defensive power":8}
        ],
        "boss":{"name":"Beast king","HP":90,"physical power":10,"magical power":0,"real power":0,"physical defensive power":10,"magical defensive power":10}
    },
    "hard":{
        "small creatures":[
            {"name":"dragon","HP":80,"physical power":10,"magical power":10,"real power":0,"physical defensive power":10,"magical defensive power":10},
            {"name":"demon king","HP":120,"physical power":15,"magical power":15,"real power":15,"physical defensive power":12,"magical defensive power":12}
        ],
        "boss":{"name":"destroying king","HP":150,"physical power":20,"magical power":20,"real power":20,"physical defensive power":20,"magical defensive power":20}
    }
}
game_state={}

@app.get("/")
def home():
    """Main page"""
    form=p.form(
        p.label("Select your character: "),
        p.select(
            p.option("knight ",value="knight"),
            p.option("monk  ",value="monk"),
            p.option("pioneer",value="pioneer"),
            name="character"
        ),
        p.br(),
        p.label("Select difficulty: "),
        p.select(
            p.option("Easy",value="Easy"),
            p.option("Normal",value="Normal"),
            p.option("Hard",value="Hard"),
            name="difficulty"
        ),
        p.br(),
        p.input(type="submit",value="Start Game!"),
        action="/start",
        method="post"
    )
    details_knight=p.p(p.a("knight details",href="/character_info?character=knight"))
    details_monk = p.p(p.a("monk details",href="character_info?character=monk"))
    details_pioneer=p.p(p.a("pioneer details",href="character_info?character=pioneer"))

    page = p.html(
            p.head(p.title("Numonster")),
            p.body(
                p.h1("Numonster"),
                p.img(src="/static/istockphoto-2080572486-1024x1024.jpg"),
                p.p("Choose your character and difficulty"),
                form,
                details_knight,
                details_monk,
                details_pioneer
            ),
        )
    return str(page)
@app.get("/character_info")
def character_info():
    character=request.args.get("character","")
    details=characters.get(character)
    if not details:
        content=p.p(f"No details of  your character{character}")
    else:
        table=p.table(
            *(p.tr(p.td(i),p.td(str(value))) for i, value in details.items()),
        )
        if character=="knight":
            image=p.img(src="/static/istockphoto-1952332326-1024x1024.jpg")
        elif character=="monk":
            image=p.img(src="/static/istockphoto-826935450-1024x1024.jpg")
        elif character=="pioneer":
            image=p.img(src="/static/istockphoto-1198829958-1024x1024.jpg")
        else:
            image=""
        content=p.div(table,image)
    page=p.html(
        p.head(p.title(f"{character} Details")),
        p.body(
            p.h1(f"{character} Details"),
            content,
            p.br(),
            p.a("return to selection",href="/")
        )
    )
    return str(page)

if __name__ == "__main__":
    app.run(port=5001)

from flask import Flask, request, render_template, redirect, url_for
from random import randint, choice
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///votes.db")
TODOS = ['run', 'homework', 'clear my room']

@app.route("/")
def index():
  return redirect(url_for('roll'))
  # info = db.execute("SELECT * from photos;")
  # for row in info:
    # print(row.get('img'))
  num_dice = int(request.args.get("dice", 2))
  roll = []
  dice = [9856, 9857, 9858, 9859, 9860, 9861]
  for die in range(num_dice):
    roll.append(chr(choice(dice)))
  return render_template("main.html", dice=roll, roll_count=99)
  # return f"<h1 style='font-size:8rem;'>{die1} {die2}</h1>"
@app.route("/add")
def add():
  return render_template("add.html")
@app.route("/todo", methods=["GET", "POST"])
def hi():
  if request.method == "POST":
    new_task = request.form.get("new_task", ":)")
    if new_task not in TODOS:
      TODOS.append(new_task)
  return render_template("index.html", todos=TODOS)

@app.route("/one/")
def one():
  return "page 1"
@app.route("/two")
def two():
  return "page 2"
  
@app.route("/weather")
def weather():
  condition = request.args.get("cond", "temp")
  temp = request.args
  print("-------> ", temp)
  if condition == "rain":
    icon = 127783
  elif condition == "snow":
    icon = 127784
  elif condition == "cloudy":
    icon = 127781
  elif condition == "hot":
    icon = 127777
  else:
    icon = 129409#127774
  return render_template("weather.html", emoji = chr(icon))
@app.route("/hello/<person>")
def hello(person):
  if person == "Ruby":
    icon = chr(127829)
  else:
    icon = chr(128640)
  return f"<h1>Hello, {person}! {icon}</h1>"

def roll_dice(n):
  dice = [randint(1,6) for x in range(n)]
  return dice

@app.route("/roll", methods=["GET","POST"])
def roll():
  d = int(request.args.get("d", 5))
  m = int(request.args.get("m", 3))
  if request.method == "GET":
    roll_count = 1
    current_roll = []
    for x in range(d):
      r = randint(1,6)
      dice = {
        "die":x + 1,
        "value": r,
        "face": chr(9855 + r)
      }
      current_roll.append(dice)
    # return render_template("main.html", 
    #                        dice=current_roll, 
    #                        roll_count=roll_count)
  else:
    current_roll = []
    for name,value in request.form.items():
      if name == "roll_count":
        roll_count = int(value) + 1 
      else:
        if int(value) == 0:
          value = randint(1,6)
          previous = "R"
        else:
          value = int(value)
          previous = "H"
        
        dice = {
          "die":name,
          "face": chr(9855+value),
          "value":value,
          "previous":previous          
        }
        current_roll.append(dice)

  return render_template("main.html",
                          dice=current_roll, roll_count=roll_count, m=m)


@app.route("/clims/")
def clims():
  name = request.args.get('name')
  return f"<h1 style='font-size:5rem;'>Welcome to the CLIMS Database, {name}</h1>"

if __name__ == "__main__":
  # website_url = "https://flaskDemo.hsecs1.repl.co"
  # app.config['SERVER_NAME'] = website_url
  app.run("0.0.0.0", debug=True)



def to_feetinches(inches):
  feet = inches // 12
  in_left = inches - (12 * feet)
  return [feet, in_left]

def get_weather_icon(condition):
  if condition == "rain":
    return chr(128031)
  elif condition == "sun":
    return chr(129409)
  else:
    return '🍔'

def to_mph():
  mph = 456
  return mph

def num_letters(sentence):
  pass
  
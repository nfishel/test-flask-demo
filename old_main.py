from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from flask_session import Session
from random import randint, choice
from cs50 import SQL

app = Flask(__name__)


#Session Config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'

Session(app)


db = SQL("sqlite:///votes.db")
TODOS = [
  {'id':1, 'task_name':'run', 'is_complete': False},
  {'id':2, 'task_name':'homework', 'is_complete': True},
  {'id':3, 'task_name':'feed the dog', 'is_complete': False},
]
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
  duplicate_task = False
  if request.method == "POST":
    new_task = request.form.get("new_task", ":)")
    if len(TODOS) == 0:
      new_id = 1
    else:
      new_id = TODOS[-1].get("id") + 1
    
    task = {'id':new_id, 'task_name': new_task, 'is_complete':False}
    for old in TODOS:
      if new_task in old.values():
        duplicate_task = True
    if not duplicate_task:
      TODOS.append(task)
    else:
      msg = f"{new_task} is already in your list of things todo today!"
      return render_template("error.html", message=msg)
  return render_template("index.html", todos=TODOS)

@app.route("/del/<int:id>")
def removeTask(id):
  for index, task in enumerate(TODOS):
    if task.get('id') == id:
      TODOS.pop(index)
  return redirect("/todo")

@app.route("/one")
def one():
  return jsonify(TODOS)
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
  
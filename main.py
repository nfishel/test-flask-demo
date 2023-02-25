from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

TODOS = []  
@app.route("/")
def index():
  return render_template("index.html")

  
#better TODO App
@app.route("/add", methods=["GET","POST"])
def add():
  # GET --> Show the form to add a new task
  if request.method == "GET":
    return render_template("addtask.html")
  else:  # POST --> Process the submitted form
    # set the next id --> 1 if it is the first task
    # or 1 more than the last id in the TODOS list
    if len(TODOS) == 0:
      id = 1
    else:
      id = TODOS[-1]['id'] + 1
    # get data from the form
    task_name = request.form.get("task_name")
    priority = request.form.get("priority")
    is_complete = bool(request.form.get("completed", False))
    

    # make a dict out of our data
    task = {
      "id": id,
      "name": task_name,
      "priority": priority,
      "is_complete": is_complete
    }
    TODOS.append(task)
    return redirect(url_for("todo"))

@app.route("/todo")
def todo():
  return render_template("todo.html", todos=TODOS)
    
if __name__ == "__main__":
  app.run(host="0.0.0.0",port="80", debug=True)
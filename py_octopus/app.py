# app.py

from api import OctopusAPI


app = OctopusAPI()


@app.route("/home")
def home(request, response):
    response.text = f"Py-Octopus: The Fastest Web Application Framework"


@app.route("/home/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"


@app.route("/about")
def about(request, response):
    response.text = "Hello from the ABOUT page"


@app.route("/add/{val_1:d}/{val_2:d}")
def add(request, response, val_1, val_2):
    total = int(val_1) + int(val_2)
    response.text = f"{val_1} + {val_2} = {total}"

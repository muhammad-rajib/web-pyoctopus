# app.py

from api import OctopusAPI


app = OctopusAPI()


"""
# Function Based Handlers
"""

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


"""
# Class Based Handlers
"""
@app.route("/book")
class BooksResource:
    def get(self, req, resp):
        resp.text = "Endpoint to get Book Page"

    def post(self, req, resp):
        resp.text = "Endpoint to create a book"


# Django Like Routing
def sample(req, resp):
    resp.text = "Sample django type route"

app.add_route("/sample", sample)


# templates handler
@app.route("/template")
def template_handler(req, resp):
    resp.body = app.template(
        "index.html", 
        context={"title": "Awesome Framework", "name": "Py-Octopus"}
        )

# exception
def custom_exception_handler(req, resp, exception_cls):
    resp.text = str(exception_cls)

app.add_exception_handler(custom_exception_handler)


@app.route("/exception")
def exception_throwing_handler(request, response):
    raise AssertionError("This handler should not be used")


# custom middleware
from middleware import Middleware

class SimpleCustomMiddleware(Middleware):
    def process_request(self, req):
        print("Processing request", req.url)

    def process_response(self, req, res):
        print("Processing response", req.url)

app.add_middleware(SimpleCustomMiddleware)
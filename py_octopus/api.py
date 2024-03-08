# api.py 

from webob import Request, Response


class OctopusAPI:
    def __call__(self, environ, start_response):
        request = Request(environ)

        response = Response()
        response.text = "Hello Py-Octopus !!!"

        return response(environ, start_response)

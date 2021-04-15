from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/')
def hello_world():
    """
    A simple test API
    This ednpoint does nothing
    Only returs "Hello, World!"
    ---
    responses:
      200:
        description: Hello, World! message
    """
    return 'Hello, World!'
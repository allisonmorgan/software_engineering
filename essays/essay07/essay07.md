# Flask

[Flask](http://flask.pocoo.org) is a "microframework" written in Pythgon for generating lightweight web applications. It calls itself a microframework because, at its core, it leaves all database interactions, form validation, authentication, etc. to other tools and libraries. Based on the [Web Server Gateway Interface Framework](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface#Examples), Flask allows for simple interactions between web servers and applications, in this case Python scripts.

### Deeper Dive

Flask was developed in 2010, and is used by companies like [LinkedIn](https://www.youtube.com/watch?v=OXN3wuHUBP0#t=46) and [Pinterest](https://www.quora.com/What-challenges-has-Pinterest-encountered-with-Flask/answer/Steve-Cohen?srid=hXZd&share=1) for APIs. The creator of Flask, Armin Ronacher said:

> The idea of Flask is to build a good foundation for all applications. Everything else is up to you or your extensions.

Now, I will highlight the components of a Flask application, which will hopefully elaborate upon the creator's mindset behind Flask.

### [Minimal Example](http://flask.pocoo.org/docs/0.12/quickstart/)

Here's a simple example of a python script for creating a Flask application:

```{python}
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

In the first two lines, we've created an instance of the `Flask` class. The `@app.route("/")` call, tells us that visiting the local path "/" will execute the `hello()` function below. You can run this script, by typing the following into the command line:

```
export FLASK_APP=hello.py
flask run
 * Serving Flask app "hello"
 * Running on http://127.0.0.1:5000/
```

Then visit `http://127.0.0.1:5000/` on your browser, to see the application. This example is quite lightweight. Flask offers a number of other nice features, such as:

- [URL routing](http://flask.pocoo.org/docs/0.12/quickstart/#routing) can be dynamically typed (e.g. `/biography/<input_name>` -> `/biography/ada_lovelace`)
- Particular function calls based on [HTTP method](http://flask.pocoo.org/docs/0.12/quickstart/#http-methods), and grabbing [input form data](http://flask.pocoo.org/docs/0.12/quickstart/#the-request-object)
- Rendering custom [templates](http://flask.pocoo.org/docs/0.12/quickstart/#rendering-templates)

But generally, Flask's functionality is quite minimal. For more advanced applications, there exist [extensions](http://flask.pocoo.org/docs/0.12/extensions/#extensions) for asking databases, handling form submission, etc. And this is the ethos of Flask, and the idea the creators had in mind - Flask is simple, and all of the particulars for your use case have been ported to these extensions.

### Getting Started

If you are a Python user, to [install Flask](http://flask.pocoo.org/docs/0.12/installation/#installation) you should simply be able to run:
```
pip install Flask
```

To test it out, you can save my above script to a `hello.py` file and run `export FLASK_APP=hello.py` and `flask run`, and you should be up and running.

### References
- [Flask Homepage](http://flask.pocoo.org)
- [Flask Documentation](http://flask.pocoo.org/docs/0.12/)
- [Flask Github](https://github.com/pallets/flask)
- [Flask Wikipedia](https://en.wikipedia.org/wiki/Flask_(web_framework))

Author: Allie Morgan (allison.morgan@colorado.edu)

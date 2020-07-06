# Megawapp

## Turning Megawatt into an app

As of right now, this takes Nick Montfort’s highly idiosyncratic Megawatt code and tries to turn it into, first, a traditional python package, then a Flask server that uses that package code to deliver Megawatt on its frontend.

## Modulizing

We’re following the traditional python module structure described [here](https://docs.python-guide.org/writing/structure/).

Right now, we’re only using chapter 1 of Megawatt. The code that is reused throughout the primary script has been moved to the `helpers.py` file, while all the code that directly writes the chapter is in the `megawatt.py` file.

## Server-making

We’re working with a melange of these two guides:

[How to package and distribute python applications](https://www.digitalocean.com/community/tutorials/how-to-package-and-distribute-python-applications)

[Flask by example](https://realpython.com/flask-by-example-part-1-project-setup/)

To start the server, run `python run.py` in the terminal and then navigate to `localhost:5000` in your browser of choice.

Right now, the server automatically serves the title when we go to root `/` and the first chapter when we go to `localhost:5000/chapter-1`

from flask import Flask
app = Flask(__name__)
import megawatt

#when we're running a simple flask server, we set the route URL and then define a function to be run when that endpoint is accessed
@app.route('/')
def title():
    return 'Megawatt, by Nick Montfort'

@app.route('/chapter-1')
def chapter_1():
    return megawatt.write_chapter_1()

#the __(whatever)__ variables are special variables defined by the Python interpreter
# in this case, if the file is being run directly
# meaning we're running this script in the terminal as python run.py
# its __name__ is automatically assigned as '__main__'
# see further explanation [here](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
if __name__ == '__main__':
    app.run()


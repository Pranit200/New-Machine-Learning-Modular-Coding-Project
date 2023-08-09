from flask import Flask      
from src.logger import logging
# pip show flask

app = Flask(__name__)

# '/' is used to run application on / and methods
@app.route('/',methods = ['GET', 'POST'])
def index():
    logging.info("we are testing our logging file")

    return "Welcome Pranit"

# There are multiple paremeters in app.run
if __name__ == "__main__":
    app.run(debug = True) # default port number is 5000
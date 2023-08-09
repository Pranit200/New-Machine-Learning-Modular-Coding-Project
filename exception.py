from flask import Flask      
from src.logger import logging
from src.exception import CustomException
import os,sys
# pip show flask

app = Flask(__name__)

# '/' is used to run application on / and methods
@app.route('/',methods = ['GET', 'POST'])
def index():
    try:
        raise Exception("we are testing our Exception file")  # Error
    except Exception as e:
        ML = CustomException(e,sys)
        logging.info(ML.error_message)

        logging.info("we are testing our logging file")

        return "Welcome Pranit"

# There are multiple paremeters in app.run
if __name__ == "__main__":
    app.run(debug = True) # default port number is 5000
from flask import Flask, request
from config import Configuration

from flask_restplus import Api
from datetime import datetime as dt



app = Flask(__name__)
api = Api(app = app, 
            version = '1.0',
            title = 'Intent Classifier',
            description = 'Microservice that allows you to figure out the intent of the text.')


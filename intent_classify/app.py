from flask import Flask, request
from config import Configuration

from flask_restplus import Api
from datetime import datetime as dt
#import logging



app = Flask(__name__)
api = Api(app = app, 
            version = '1.0',
            title = 'Intent Classifier',
            description = 'Microservice that allows you to figure out the intent of the text.')

#logging.basicConfig(level=logging.DEBUG)

#@app.after_request
#def after_request(response):
#    app.logger.info(
#        "%s [%s] %s %s %s %s %s %s %s",
#        request.remote_addr,
#        dt.utcnow().strftime("%d/%b/%Y:%H:%M:%S.%f")[:-3],
#        request.method,
#        request.path,
#        request.scheme,
#        response.status,
#        response.content_length,
#        request.referrer,
#        request.user_agent,
#    )
#    return response


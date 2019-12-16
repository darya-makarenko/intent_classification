from app import app
from app import api

import view
from view import IntentClassify
import logging


if __name__ == "__main__":
    
	logging.basicConfig(filename='example.log',level=logging.DEBUG)
	api.add_resource(IntentClassify, '/intent_classify', '/intent_classify')	
	app.run(host="127.0.0.1", port=5000)

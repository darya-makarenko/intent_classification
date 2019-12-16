from app import api
from flask import render_template
import flask.views
from flask import Flask, request, jsonify
import intent_classify
from intent_classify import classify_intent
import json
from flask_restplus import Resource, fields

namespace = api.namespace('classify_intent', description="Detect intent of the text.")
single_model = api.model('Input Single Text Model', 
				  {'text': fields.String, 'lang': fields.String})
multiple_model = api.model('Input Multiple Texts Model', 
				  {'texts': fields.List(fields.Nested(single_model))})

@namespace.route('/')
class IntentClassify(Resource):
    @api.doc(responses={ 200: 'OK' })
    def get(self):
        return """This service gives you an intent detecting functionality. Use post query with thr following structure: 
                {'text': <...>, 'lang': <...>} 
                or use JSON key 'texts': [<array of texts>]."""


    @api.doc(responses={ 200: 'OK', 400: 'Bad Request'})
    @api.expect(multiple_model)
    def post(self): 
        data = json.loads(request.data)
        
        texts = []
        if (data != None) and  ('texts' in data.keys()):
            texts = data['texts']
            texts_info = classify_intent(texts)
            return jsonify(texts_info)
        else:
            namespace.abort(400, status = 'Could not detect any intent. Possibly bad texts were given.')
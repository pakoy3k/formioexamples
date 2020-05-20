import flask
from flask import Response
import json
from flask_cors import CORS

app = flask.Flask(__name__)
cors = CORS(app)
#app.config["DEBUG"] = True

@app.route('/tramite', methods=['GET'])

def tramite():
	with open('tramite.json','r') as mytramite:
		data = json.load(mytramite)
	print(data)
	#objs = json.load(data)
	#resp = Response(objs, status=200, mimetype='application/json; charset=utf-8')
	#print(objs)
	mytramite.close()
	return data

@app.route('/', methods=['GET'])
def home():
    return "HI"

if __name__ == '__main__':
	app.run(host='0.0.0.0')

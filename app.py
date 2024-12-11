from flask import Flask, request

app = Flask(__name__)

variables = {}


@app.route('/set_var', methods=['POST'])
def set_var():
	global variables
	body = request.json
	key, value = body['key'], body['value']
	variables[key] = value
	return 'variable created', 201


@app.route('/get_var', methods=['GET'])
def get_var():
	global variables
	body = request.json
	key = body['key']
	if key not in variables.keys():
		return 'variable not found', 404
	return variables[key], 200


if __name__ == '__main__':
	app.run()

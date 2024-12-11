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


@app.route('/edit_var', methods=['PUT'])
def edit_var():
	global variables
	body = request.json
	key, value = body['key'], body['value']
	if key not in variables.keys():
		return 'variable not found', 404
	variables[key] = value
	return 'variable edited', 200


@app.route('/delete_var', methods=['DELETE'])
def delete_var():
	global variables
	body = request.json
	key = body['key']
	if key not in variables.keys():
		return 'variable not found', 404
	del variables[key]
	return 'variable deleted', 204


if __name__ == '__main__':
	app.run()

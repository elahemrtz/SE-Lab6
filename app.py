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


if __name__ == '__main__':
	app.run()

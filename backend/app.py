import sys

from flask import Flask, request

from db import key_exists, initialize_db, exec_query

app = Flask(__name__)


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
	return 'server is healthy', 200


@app.route('/set_var', methods=['POST'])
def set_var():
	body = request.json
	key, value = body['key'], body['value']
	if key_exists(key):
		return 'variable already exists', 403

	exec_query('INSERT INTO public.variables VALUES(%s, %s)', (key, value))

	return 'variable created', 201


@app.route('/get_var', methods=['GET'])
def get_var():
	body = request.json
	key = body['key']

	if not key_exists(key):
		return 'variable not found', 404

	return exec_query('SELECT value from public.variables WHERE key=%s', (key,), return_value=True)[0], 200


@app.route('/edit_var', methods=['PUT'])
def edit_var():
	body = request.json
	key, value = body['key'], body['value']

	if not key_exists(key):
		return 'variable not found', 404

	exec_query('UPDATE public.variables SET value=%s WHERE key=%s', (value, key))
	return 'variable edited', 200


@app.route('/delete_var', methods=['DELETE'])
def delete_var():
	body = request.json
	key = body['key']

	if not key_exists(key):
		return 'variable not found', 404

	exec_query('DELETE FROM public.variables WHERE key=%s', (key,))

	return 'variable deleted', 204


initialize_db()
if __name__ == "__main__":
	app.run(debug=True)

import unittest
import requests

base_url = 'http://0.0.0.0:3000'


class MyTestCase(unittest.TestCase):
	def test_something(self):
		for i in range(10):
			k = f'key_name{i // 2}'
			v = f'hello{i // 2}'
			headers = {'Content-Type': 'application/json'}

			if i % 2 == 0:
				response = requests.delete(f'{base_url}/delete_var',
										   data='{"key": "' + k + '"}',
										   headers=headers)
				self.assertIn(response.status_code, [204, 404])
				response = requests.post(f'{base_url}/set_var',
										 data='{"key": "' + k + '", "value": "' + v + '"}',
										 headers=headers)
			else:
				response = requests.get(f'{base_url}/get_var',
										data='{"key": "' + k + '"}',
										headers=headers)
			body = response.text
			print(body)
			self.assertIn(response.status_code, [200, 201])
			self.assertEqual(body, 'variable created' if i % 2 == 0 else v)


if __name__ == '__main__':
	unittest.main()

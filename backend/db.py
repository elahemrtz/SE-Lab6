import os
from typing import Optional

import psycopg

conn: Optional[psycopg.Connection] = None


def initialize_db():
	global conn
	# postgresql:///?User=postgres&Password=se_lab6_password&Database=se_lab6&Server=se-lab6-database-1&Port=5432
	dbname = os.environ.get('PGSQL_DBNAME', 'se_lab6')
	user = os.environ.get('PGSQL_USER', 'postgres')
	password = os.environ.get('PGSQL_PASSWORD', 'se_lab6_password')
	host = os.environ.get('PGSQL_HOST', 'localhost')
	port = os.environ.get('PGSQL_PORT', '5432')
	print(dbname, user, password, host, port)
	conn = psycopg.connect(dbname=dbname, user=user, password=password, host=host, port=port)
	print('Connected to database')


def key_exists(key: str) -> bool:
	return exec_query('SELECT value from public.variables WHERE key=%s', (key,), return_value=True) is not None


def exec_query(query, params=None, return_value=False):
	with conn.cursor() as cur:
		cur.execute(query, params)
		conn.commit()
		if return_value:
			return cur.fetchone()

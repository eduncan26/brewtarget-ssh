import sqlite3

class Database:
	"""
	DB connection and methods
	"""

	base_recipe_query = 'SELECT * FROM RECIPE'

	def __init__(self, connection_str):
		self.connection_str = connection_str

	def connect(self):
		self.connection = sqlite3.connect(self.connection_str)
		return self.connection

	def disconnect(self):
		return self.connection.close()

	def get_recipes(self):
		return self.connection.execute(self.base_recipe_query).fetchall()

	def get_recipe(self, recipe_name):
		return self.connection.execute(self.base_recipe_query + ' WHERE name = "' + recipe_name + '"').fetchone()


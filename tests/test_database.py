import unittest
from brewtarget_ssh import database

class TestDataBase(unittest.TestCase):

	def setUp(self):
		self.db = database.Database('/usr/share/brewtarget/default_db.sqlite')
		self.connection = self.db.connect();

	def tearDown(self):
		self.db.disconnect()

	def test_get_recipes(self):
		self.assertTrue(len(self.db.get_recipes()) > 0)

	def test_get_recipe(self):
		q = 'Bt: American Barleywine'
		recipe = self.db.get_recipe(q)
		self.assertTrue(len(recipe))
		self.assertTrue(recipe[1] == 'Bt: American Barleywine')


if __name__ == '__main__':
	unittest.main()
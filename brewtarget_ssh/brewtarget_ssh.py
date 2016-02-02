import database

class BrewtargetSSH:

	def __init__(self):
		self.db = database.Database('/usr/share/brewtarget/default_db.sqlite')

	
	# TODO: write decorator to open the db connection
	# before the fn has been called and to close it
	# after the fn has been called
	def get_recipes(self):
		self.db.connect()
		return self.db.get_recipes()



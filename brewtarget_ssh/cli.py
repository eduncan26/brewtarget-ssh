import argparse
import database

db = database.Database('/usr/share/brewtarget/default_db.sqlite')

parser = argparse.ArgumentParser(description="Interact with Brewtarget over SSH")

parser.add_argument('recipes', metavar='n', type=str, help='Get recipes')
parser.add_argument('--all', dest='')

args = parser.parse_args()

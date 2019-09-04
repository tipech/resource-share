"""Random user generator

Provides a generator class for the users of the resource sharing problem, as
well as common functions such as printing or I/O.

Classes:
  Generator -- handles generation of User objects

"""
import random, json, os
from datetime import datetime
from pprint import pprint

from model.user import User
# from graphics import Point, Line, Rectangle, Text, GraphWin

class Generator():
	"""Handles generation of User objects"""
	def __init__(self, res_list, width=1000, height=1000,
		size_min=0, size_max=.1, custom_seed = None):
		"""Seed random number generator"""
		
		self.res_list = res_list
		self.width = width
		self.height = height
		self.size_min = size_min
		self.size_max = size_max

		self.count = 0
		self.users = []


		if(custom_seed):
			random.seed(custom_seed)
		else:
			random.seed()


	def get_random_square(self):
		"""Get a square with random size, position in generator's bounds."""

		corner = (random.uniform(0,self.width), random.uniform(0,self.height))
		size = random.uniform(self.size_min * self.width,
							  self.size_max * self.width)
		return (corner[0]+size, corner[1]+size)


	def create_user(self):
		"""Generate a single User object"""

		new_user = User(self.count, self.get_random_square(), self.res_list)
		self.users.append(new_user)
		self.count += 1
		return new_user


	def create_users(self, count):
		"""Generate multiple User objects."""

		for x in range(0,count):
			self.create_user()


	def to_JSON(self):
		"""Store generator parameters and results as JSON."""

		gen_dict = {"id": '', "dimension": 2, "length": self.count,
			"bounds":{
				"id":'',"dimension": 2, "dimensions":
				[[0, self.width], [0, self.height]]},
			"regions": [user.to_JSON() for user in self.users]
			}

		# check if data storage exists and if not, create it
		if not os.path.isdir("data"):
			os.mkdir("data")

		# open file for storage, filename is timestamp
		with open("data/%s.json"% datetime.now(), "w+") as file:
			
			# write pretty JSON to file
			file.write( json.dumps(gen_dict, sort_keys=True,
				indent=4, separators=(',', ': ')))
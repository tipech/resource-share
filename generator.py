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

	def __init__(self, res_list=[], width=1000, height=1000,
		x_size_min=0, x_size_max=.05,
		y_size_min=0, y_size_max=.05,
		custom_seed = None, crop_circle=False,
		size_dist_func=None, pos_dist_func=None):
		"""Seed random number generator"""
		
		self.res_list = res_list
		self.width = width
		self.height = height
		self.x_size_min = x_size_min
		self.x_size_max = x_size_max
		self.y_size_min = y_size_min
		self.y_size_max = y_size_max
		self.size_dist_func = size_dist_func
		self.pos_dist_func = pos_dist_func
		self.crop_circle = crop_circle

		self.count = 0
		self.users = []


		if(custom_seed):
			random.seed(custom_seed)
		else:
			random.seed()



	def get_random_square(self):
		"""Get a square with random size, position in generator's bounds."""

		if not self.size_dist_func:
			size_random = random.uniform
		else:
			size_random = self.size_dist_func


		x_size = size_random(self.x_size_min * self.width,
							 self.x_size_max * self.width)

		y_size = size_random(self.y_size_min * self.height,
							 self.y_size_max * self.height)

		if not self.pos_dist_func:
			pos_random = random.uniform
		else:
			pos_random = self.pos_dist_func

		avail_width = self.width - x_size
		avail_height = self.height - y_size

		corner = (max(0, min(avail_width, pos_random(0, avail_width))),
				  max(0, min(avail_height, pos_random(0, avail_height))))
		
		i = 0

		if self.crop_circle:
			while ((corner[0]-avail_width/2)**2
				+ (corner[1]-avail_height/2)**2
				> (avail_width/2)**2 and i < 1000):
		
				i+=1	
				corner=(max(0, min(avail_width, pos_random(0, avail_width))),
					max(0, min(avail_height, pos_random(0, avail_height))))

		return (corner[0], corner[0] + x_size, corner[1], corner[1] + y_size)


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
		# with open("data/%s.json"% datetime.now(), "w+") as file:
		with open("data/input.json", "w+") as file:
			
			# write pretty JSON to file
			file.write( json.dumps(gen_dict, sort_keys=True,
				indent=4, separators=(',', ': ')))
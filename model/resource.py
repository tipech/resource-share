"""Resource objects

Provides container classes for the shareable resources and their type.

Classes:
  Resource -- a resource to be shared
  ResourceType -- the type of the resource

"""
import random


class ResourceType():
	"""Possible resource type."""
	
	def __init__(self, name, res_max=1, res_min=0, discrete=False,
		step=1, res_values=None):
		"""Create a resource type with specified name and parameters."""
		
		self.name = name
		self.max = res_max
		self.min = res_min
		self.discrete = discrete
		self.step = step
		self.values = res_values 


	def get_random_value(self):
		"""Get a random value from within the resource's range."""

		if not self.discrete:		# get continuous value from range
			return random.uniform(self.min, self.max)

		elif not self.values:	# get discrete value from range
			return random.randrange(self.min, self.max, self.step)

		else:						# get discrete value from list of elements
			return random.choice(self.values)


	def as_dict(self):
		"""Return a dictionary representation of the object."""
		return {"name": self.name, "max": self.max, "min": self.min,
		  "discrete": self.discrete, "step": self.step, "values": self.values}


	def __repr__(self):
		"""Get printable representation."""
		return ("ResourceType(%r)"
			% (self.name))


	def get_random_res(self):
		"""Get a Resource object with a random value."""

		return Resource(self, self.get_random_value())



class Resource():
	"""Instance of a single resource."""
	
	def __init__(self, res_type, value = None):
		"""Create a resource with appropriate type and value."""
		
		self.type = res_type
		self.value = value if value else res_type.get_random_value()


	def as_dict(self):
		"""Return a dictionary representation of the object."""
		return {"type": self.type.as_dict(), "value": self.value}


	def __repr__(self):
		"""Get printable representation."""
		return ("%r Resource(%r)"
			% (self.type.name, self.value))

"""User object

Provides a container class for a user with some shareable resources.

Classes:
  User -- a specific user with a location and resources

"""



class User():
	"""Instance of a single user"""

	def __init__(self, _id, position, res_list):
		"""Create a user with specified id and resources."""
		self.id = _id
		self.position = position
		self.resources = []

		for resource in res_list:
			
			# if only the possible resource type was given, generate randomly
			if type(resource).__name__ == "ResourceType":
				resource = resource.get_random_res()

			self.resources.append(resource)

	def to_JSON(self):
		"""Return a dictionary representation of the object."""
		return {"id": self.id, "dimension": 2,
			"dimensions": [[0,self.position[0]], [0,self.position[1]]],
			"data": [res.as_dict() for res in self.resources]
			}


	def __repr__(self):
		"""Get printable representation."""
		return ("User(%r, res=%r)"
			% (self.id, ', '.join(res.type.name for res in self.resources)))




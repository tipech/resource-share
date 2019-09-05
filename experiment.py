from model.resource import ResourceType, Resource
from model.user import User
from generator import Generator

cpu_type = ResourceType("CPU", discrete=True)


generator = Generator([cpu_type], size_min=.05, size_max=.05)


generator.create_users(100)

# print(test_generator.users)

generator.to_JSON()
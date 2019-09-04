from model.resource import ResourceType, Resource
from model.user import User
from generator import Generator

test_type = ResourceType("CPU")
test_resource = Resource(test_type)

test_user = User(1, (0,0), [test_resource])

# print(test_type)
# print(test_resource)
# print(test_user)


test_generator = Generator([test_resource])

# print(test_generator.users)

test_generator.create_users(2)

# print(test_generator.users[1].position)

test_generator.to_JSON()
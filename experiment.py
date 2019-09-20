from model.resource import ResourceType, Resource
from model.user import User
from generator import Generator

import random, math, numpy as np
import matplotlib.pyplot as plt

# cpu_type = ResourceType("CPU", discrete=True, res_max=5)


# generator = Generator([cpu_type], x_size_min=.08, x_size_max=.08,
# 								  y_size_min=.08, y_size_max=.08)



def gauss_func(start, end):
	mu = (start + end)/2
	return random.gauss(mu,.2*end)

def triangular(start, end):
	mode=.1*end
	return random.triangular(start, end, mode)

def bimodal_func(start, end):
	return random.choice([random.gauss(.3*end, 0.15*end),
						  random.gauss(.8*end, 0.1*end)])

def poisson_func(start, end):
	return .5*np.random.poisson(1500)

size_pc = 0.05


generator = Generator(crop_circle=True, pos_dist_func=gauss_func,
	x_size_max=size_pc, y_size_max=size_pc)

# generator = Generator()



generator.create_users(1000)
generator.to_JSON()


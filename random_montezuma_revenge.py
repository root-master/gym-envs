import gym
import random
import time

from gym_minigrid.register import envList
from gym_minigrid.minigrid import Grid

# Test specifically importing a specific environment
from gym_minigrid.envs import DoorKeyEnv

# Test importing wrappers
from gym_minigrid.wrappers import *


env_list = [key for key, _ in gym.envs.registry.env_specs.items()]

# https://github.com/openai/gym/wiki/Table-of-environments
# environment = 'MontezumaRevenge-ram-v0'
environment = 'MiniGrid-MultiRoom-N2-S4-v0'
env = gym.make(environment)

# image_state = env.env._get_image()
# ram_state = env.env._get_ram()

screen = env.reset()
for i in range(10000):
	env.render()
	screen, reward, terminal, step_info = env.step(env.action_space.sample())
	env.step(env.action_space.sample()) # take a random action
	time.sleep(0.2)
	if terminal:
		print('GAME OVER!')
		env.reset()

env.close()


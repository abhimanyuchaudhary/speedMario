from nes_py.wrappers import BinarySpaceToDiscreteSpaceEnv
import gym_super_mario_bros
from gym_super_mario_bros.actions import COMPLEX_MOVEMENT
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = BinarySpaceToDiscreteSpaceEnv(env, COMPLEX_MOVEMENT)
import time

done = True
for step in range(1000):
    if done:
        state = env.reset()
    state, reward, done, info = env.step(env.action_space.sample())
    time.sleep(.010)   
    # print(info)
    # print(len(info['test']))
    for i in range(12):
    	for j in range(12):
    		print(info['test'][i*12+j],end=" ")
    	print()
    print("X--------------------X")
    env.render()

env.close()
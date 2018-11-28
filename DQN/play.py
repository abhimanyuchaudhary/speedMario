from nes_py.wrappers import BinarySpaceToDiscreteSpaceEnv
import gym_super_mario_bros
from gym_super_mario_bros.actions import COMPLEX_MOVEMENT
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = BinarySpaceToDiscreteSpaceEnv(env, COMPLEX_MOVEMENT)
import time
from dqn import DQN
from mario import mario
import numpy as np
import torch
import collections



batch_size=40
maxMemory=50
network=mario(gamma=0.9, learningRate=0.003, memorySize=maxMemory)



#print(len(network.recallMemory))
while len(network.recallMemory)<maxMemory:
	s0=env.reset()
	done=False
	prev_xpos=40
	max_xpos=40
	counter=0
	killCount=0
	print(maxMemory-len(network.recallMemory))

	while 1>0:
		if done or killCount>20: #remove killCount?
			#print("***************")
			#print(np.mean(s0,axis=2))
			#print(torch.tensor(np.mean(s0,axis=2)).shape)#=[240,256]
			#print("***************")
			break

		if counter%3==0:
			act=env.action_space.sample()
		
		s1,reward,done,info=env.step(act)
		xval=info['x_pos']
		reward=xval-prev_xpos
		if info['life']<3:
			reward=reward-20
			done=True
		network.addToMemory(np.mean(s0[::2,::2],axis=2),act,reward,np.mean(s1[::2,::2],axis=2))
		
		if max_xpos>=xval:
			killCount+=1
		else:
			killCount=0
		prev_xpos=xval
		max_xpos = max(xval,max_xpos)
		s0=s1

		counter+=1
		#env.render()
#print(len(network.recallMemory))




while 1>0:
	s0=env.reset()
	done=False
	prev_xpos=40
	max_xpos=40
	trackMovement=collections.deque(maxlen=3)
	while len(trackMovement)<3:
		print(torch.tensor(np.mean(s0[::2,::2],axis=2)).shape)
		trackMovement.append(np.mean(s0[::2,::2],axis=2))
	killCount=0

	while 1>0:
		if done or killCount>20:
			#print("***************")
			#print(np.mean(s0,axis=2))
			#print(torch.tensor(np.mean(s0,axis=2)).shape)#=[240,256]
			#print("***************")
			break


		#act=env.action_space.sample()
		act=network.makeMove(trackMovement)
		

		s1,reward,done,info=env.step(act)
		xval=info['x_pos']
		reward=xval-prev_xpos
		if info['life']<3:
			reward=reward-20
			done=True

		network.addToMemory(np.mean(s0[::2,::2],axis=2),act,reward,np.mean(s1[::2,::2],axis=2))
		trackMovement.append(np.mean(s1[::2,::2],axis=2))
		
		if max_xpos>=xval:
			killCount+=1
		else:
			killCount=0
		prev_xpos=xval
		max_xpos = max(xval,max_xpos)
		s0=s1

		network.train(batch_size)
		env.render()

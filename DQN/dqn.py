import torch as t
import torch.nn as nn
import torch.nn.functional as f
import torch.optim as optim
import numpy as np
import dnq
import random

class mario():
	def __init__(self, gamma, learningRate, minEps = 0.01, memorySize = 1000, maxEps = 1.0, actionSpace = list(range(0, 12))):
		self.Gamma = gamma
		self.Eps = maxEps
		self.minEps = minEps
		self.learningRate = learningRate
		self.actionSpace = actionSpace
		self.memorySize = memorySize
		self.memoryCounter = 0
		self.Q_eval = dnq(alpha)
		self.Q_next(dnq(alpha))
		self.recallMemory = []
		for i in range(memorySize):
			recallMemory.append((0, 0, 0, 0))


	def addToMemory(self, currState, action, reward, nextState):
		self.recallMemory[self.memoryCounter] = (currState, action, reward, nextState)
		self.memoryCounter = (self.memoryCounter + 1) % self.memorySize

	def makeMove(self, state):
		moveProbability = self.Q_eval.forward(state)
		if(random.uniform(0, 1) < self.Eps):
			move = np.random.choice(self.actionSpace)
		else:
			#using the middle frame, we're using 3
			move = t.argmax(moveProbability[1]).item()

	def getBatchFromMemory(self, batchSize):
		total = self.memSize - self.memoryCounter
		if(total < batchSize):
			assert(len(self.recallMemory[memoryCounter:] + self.recallMemory[:total-batchSize]) == batchSize)
			return np.array(self.recallMemory[memoryCounter:] + self.recallMemory[:total-batchSize])
		else:
			assert(total == batchSize)
			return np.array(self.recallMemory[memoryCounter:memoryCounter + batchSize])

	def learn(self, batchSize):
		self.Q_eval.optimizer.zero()

		batch = getBatchFromMemory(self, batchSize)

		Qvaluepredicted = self.Q_eval.forward(list(batch[:, 0][:])).to(self.Q_eval.device)
		Qnextvaluepredicted = self.Q_eval.forward(list(batch[:, 3][:])).to(self.Q_eval.device)

		



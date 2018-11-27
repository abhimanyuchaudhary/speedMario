import torch as t
import torch.nn as nn
import torch.nn.functional as f
import torch.optim as optim
import numpy as np
import dnq
import _pickle as cPickle
import random
from copy import deepcopy

class mario():
	def __init__(self, gamma, learningRate, minEps = 0.01, memorySize = 1000, maxEps = 1.0, actionSpace = list(range(0, 12)), epsDecayRate = 0.001):
		self.gamma = gamma
		self.Eps = maxEps
		self.minEps = minEps
		self.learningRate = learningRate
		self.actionSpace = actionSpace
		self.memorySize = memorySize
		self.memoryCounter = 0
		self.Q_eval = dnq(alpha)
		self.Q_next = dnq(alpha)
		self.recallMemory = []
		self.steps = 0
		self.learnStepCounter = 0
		self.epsDecayRate = epsDecayRate
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
		self.steps += 1

	def getBatchFromMemory(self, batchSize):
		total = self.memSize - self.memoryCounter
		if(total < batchSize):
			assert(len(self.recallMemory[memoryCounter:] + self.recallMemory[:total-batchSize]) == batchSize)
			return np.array(self.recallMemory[memoryCounter:] + self.recallMemory[:total-batchSize])
		else:
			assert(total == batchSize)
			return np.array(self.recallMemory[memoryCounter:memoryCounter + batchSize])

	def updateEps(self):
		self.Eps = self.minEps + (1 - self.minEps) * np.exp(-self.epsDecayRate * self.Eps)

	def learn(self, batchSize):
		self.Q_eval.optimizer.zero()

		batch = getBatchFromMemory(self, batchSize)

		Qvaluepredicted = self.Q_eval.forward(list(batch[:, 0][:])).to(self.Q_eval.device)
		Qnextvaluepredicted = self.Q_eval.forward(list(batch[:, 3][:])).to(self.Q_eval.device)

		#dim = 1 because middle frame?
		bestAction = t.argmax(Qnextvaluepredicted, dim = 1).to(self.Q_eval.device)
		rewards = t.Tensor(list(batch[:, 2])).to(self.Q_eval.device)

		Qtarget = Qvaluepredicted
		Qtarget[:, bestAction] = rewards + self.gamma*t.max(Qnextvaluepredicted[1])

		updateEps()

		loss = self.Q_eval.loss(Qtarget, Qvaluepredicted).to(self.Q_eval.device)
		loss.backward()
		self.Q_eval.optimizer.step()
		self.learnStepCounter += 1

    def save(self, agentNum):
		pickle_out = open("savedAgent/agent"+str(agentNum)+".ag", "wb+")
		cPickle.dump(self, pickle_out)
	def load(self, agentNum):
		pickle_in = open("savedPopulations/generation"+str(generationNumber)+".gen", "rb")
		other = cPickle.load(pickle_in)
		self.gamma = deepcopy(other.gamma)
		self.Eps = deepcopy(other.Eps)
		self.minEps = deepcopy(other.minEps)
		self.learningRate = deepcopy(other.learningRate)
		self.actionSpace = deepcopy(other.actionSpace)
		self.memorySize = deepcopy(other.memorySize)
		self.memoryCounter = deepcopy(other.memoryCounter)
		self.Q_eval = deepcopy(other.Q_eval)
		self.Q_next = deepcopy(other.Q_next)
		self.recallMemory = deepcopy(other.recallMemory)
		self.steps = deepcopy(other.steps)
		self.learnStepCounter = deepcopy(other.learnStepCounter)
		self.epsDecayRate = deepcopy(other.epsDecayRate)





import torch
import torch.nn as nn
import numpy as np


#learningRate=0
x=200
y=200


class DQN(nn.Module):

	def __init__(self,learningRate):
		super(DQN,self).__init__()

		'''self.layerC1=nn.Conv2d()
		self.layerC2=nn.Conv2d()
		self.layerC3=nn.Conv2d()

		self.layerF1=nn.Linear()
		self.layerF2.nn.Linear()

		self.opt=torch.optim.RMSprop(self.parameters, lr=learningRate)

		self.lossFunction=nn.MSELoss()
		s='cpu'
		if torch.cuda.is_available():
			s='cuda:0'
		self.dev=torch.device(s)
		self.to(self.dev)


	def forward(self,inp):
		inp=torch.Tensor(inp).to(self.dev)
		inp=inp.reshape(-1,1,x,y)
		inp=nn.functional.relu(self.layerC1(inp))
		inp=nn.functional.relu(self.layerC2(inp))
		inp=nn.functional.relu(self.layerC3(inp))
		inp=inp.reshape(-1,x,y)
		inp=nn.functional.relu(self.layerF1(inp))
		return self.layerF2(inp)
'''



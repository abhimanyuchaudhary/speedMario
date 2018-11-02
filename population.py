from chromosome import link, chromosome
import _pickle as cPickle
from copy import deepcopy
import mutate


class population:
	def __init__(self, N):
		self.generationNumber = 0;
		self.numberOfIndividuals = N
		self.individuals = []
		self.index=0
		

	def initializePopulation(self):
		for i in range(self.numberOfIndividuals):
			temp = deepcopy(chromosome())
			temp=mutate.mutate(temp,1)
			self.individuals.append(temp)
	
	def save(self):
		pickle_out = open("savedPopulations/generation"+str(self.generationNumber)+".gen", "wb+")
		cPickle.dump(self, pickle_out)
	
	def copy(self, other):
		self.generationNumber = deepcopy(other.generationNumber)
		self.numberOfIndividuals = deepcopy(other.numberOfIndividuals)
		self.individuals = deepcopy(other.individuals)
	
	def load(self, generationNumber):
		#this initializes first and then loads, can make it efficient
		pickle_in = open("savedPopulations/generation"+str(generationNumber)+".gen", "rb")
		other = cPickle.load(pickle_in)
		self.generationNumber = deepcopy(other.generationNumber)
		self.numberOfIndividuals = deepcopy(other.numberOfIndividuals)
		self.individuals = deepcopy(other.individuals)
	
	def printPopulation(self):
		print(self.generationNumber, self.numberOfIndividuals)

	def fetchNext(self):
		if self.index==self.numberOfIndividuals:
			return;
		self.index+=1
		return self.individuals[self.index-1]


# p = population(10)
# p.printPopulation()
# p.save()
'''p = population(1)
p.printPopulation()
p.load(0)
p.printPopulation()'''



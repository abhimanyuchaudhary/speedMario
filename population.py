from chromosome import link, chromosome
import _pickle as cPickle
from copy import deepcopy
class population:
	def __init__(self, N):
		self.generationNumber = 0;
		self.numberOfIndividuals = N
		self.individuals = []
		for i in range(self.numberOfIndividuals):
			temp = deepcopy(chromosome())
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

# p = population(10)
# p.printPopulation()
# p.save()
p = population(1)
p.printPopulation()
p.load(0)
p.printPopulation()



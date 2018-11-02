import chromosome
import _pickle as cPickle
from copy import deepcopy
class population:
	def __init__(self, N):
		self.generationNumber = 0;
		self.numberOfIndividuals = N
		self.individuals = []
		for i in range(self.numberOfIndividuals):
			self.individuals.append(chromosome())
	def save(self):
		pickle_out = open("savedPopulation/generation"+str(self.generationNumber)+".gen", "wb")
		cPickle.dump(self, pickle_out)
	def copy(self, other):
		self.generationNumber = deepcopy(other.generationNumber)
		self.numberOfIndividuals = deepcopy(other.numberOfIndividuals)
		self.individuals = deepcopy(other.individuals)
	def load(self, generationNumber):
		#this initializes first and then loads, can make it efficient
		pickle_in = open("savedPopulation/generation"+str(generationNumber)+".gen", "rb")
		other = pickle.load(pickle_in)
		self.generationNumber = deepcopy(other.generationNumber)
		self.numberOfIndividuals = deepcopy(other.numberOfIndividuals)
		self.individuals = deepcopy(other.individuals)


from chromosome import link, chromosome, neuron
import _pickle as cPickle
from copy import deepcopy
import mutate
import random

COMPATIBILITY_RANGE = 3;
C1 = 1
C2 = 1
C3 = 1
def compatibilityDistance(representative, newChromosome):
	''' See excessDisjointWeight in https://github.com/basanthjenuhb/Mario-AI/blob/master/neat.py
	'''
	representativeLinks = deepcopy(representative.links)
	newChromosomeLinks = deepcopy(newChromosome.links)

	representativeLinks = sorted(representativeLinks)
	newChromosomeLinks = sorted(newChromosomeLinks)


	excess, disjoint, W, i , j = 0.0, 0.0, 0.0, 0, 0
	divisorForWeightDifference = 0
	while(i < len(representativeLinks) and j < len(newChromosomeLinks)):
		if(representativeLinks[i] == newChromosomeLinks[j]):
			W = W + abs(representativeLinks[i].weight - newChromosomeLinks[j].weight)
			divisorForWeightDifference += 1
			i = i + 1
			j = j + 1
		elif(representativeLinks[i] < newChromosomeLinks[j]):
			i = i + 1
			disjoint = disjoint + 1
		else:
			j = j + 1
			disjoint = disjoint + 1

	excess = len(representativeLinks[i:]) + len(newChromosomeLinks[j:])
	N = float( max( len(representativeLinks), len(newChromosomeLinks) ) )
	if N < 20:
		N = 1.0
	distance = float(C1 * excess / N) + float(C2 * disjoint / N) + float(C3 * W / divisorForWeightDifference) #min(i, j) to take avg
	return distance

class species:
	def __init__(self, representative):
		self.subpopulation = []
		self.representative = representative
		self.subpopulation.append(representative)
		self.numIndividuals=1
	def addChromosome(self, newChromosome):
		self.numIndividuals+=1
		self.subpopulation.append(newChromosome)

class population:
	def __init__(self, N):
		self.generationNumber = 0;
		self.numberOfIndividuals = N
		self.index=0
		self.populationSpecies = []

	def changeGeneration():
		print("ADD POPULATION CHANGE HERE")
		
	def addChromosome(self, chromosome):
		#toAdd = True
		for spec in self.populationSpecies:
			print(compatibilityDistance(chromosome, spec.representative))
			if(compatibilityDistance(chromosome, spec.representative) < COMPATIBILITY_RANGE):
				spec.addChromosome(deepcopy(chromosome))
				#toAdd = False
				return;
		#if(toAdd == True):
		self.populationSpecies.append(deepcopy(species(chromosome)))


	def initializePopulation(self):
		for i in range(self.numberOfIndividuals):
			temp = deepcopy(chromosome())
			for i in range(500):
				temp=mutate.mutate(temp,random.randrange(0,10000))
			self.addChromosome(temp)
	
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
		for i in range(len(self.populationSpecies)):
			print("Species",i,":",self.populationSpecies[i].numIndividuals)

	def fetchNext(self):
		if self.index>=self.numberOfIndividuals:
			return;
		tmp=self.index
		self.index+=1
		for species in self.populationSpecies:
			if tmp>=species.numIndividuals:
				tmp = tmp-species.numIndividuals
			else:
				return species.subpopulation[tmp]


# p = population(10)
# p.printPopulation()
# p.save()
'''p = population(1)
p.printPopulation()
p.load(0)
p.printPopulation()'''



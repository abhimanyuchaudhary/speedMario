from chromosome import link, chromosome, neuron
from random import randint
import random
from copy import deepcopy

# random.seed(1) # remove later

def mutate(chromosome, innovationNumber):
	PROBABILITY_enable = 0.4
	PROBABILITY_disable = 0.2
	PROBABILITY_linkMutate = 0.75
	PROBABILITY_pointMutate = 0.9
	PROBABILITY_nodeMutate = 0.5

	if random.random()<PROBABILITY_pointMutate:
		chromosome=pointMutate(chromosome)

	#LinkMutate usually occurs twice
	chromosome=linkMutate(chromosome,1)
	if random.random()<PROBABILITY_linkMutate:
		chromosome=linkMutate(chromosome,1)

	if random.random()<PROBABILITY_nodeMutate:
		chromosome=nodeMutate(chromosome,1)

	if random.random()<PROBABILITY_enable:
		chromosome=enableDisableMutate(chromosome,True)

	if random.random()<PROBABILITY_disable:
		chromosome=enableDisableMutate(chromosome,False)

	return chromosome



def enableDisableMutate(chromosome,enable):
	#enables/disables link
	possible=[]
	for i in range(len(chromosome.links)):
		if not chromosome.links[i].isEnabled==enable:
			possible.append(i)

	if len(possible)==0:
		return chromosome
	l=possible[random.randint(0,len(possible)-1)]
	chromosome.links[l].isEnabled=enable
	return chromosome



def pointMutate(chromosome):
	if len(chromosome.links)<=0:
		return chromosome
	perturbChance = 0.9
	step = 0.1
	#when do we decrease
	l=random.randint(0,len(chromosome.links)-1)
	if random.random() < perturbChance:
		chromosome.links[l].weight = chromosome.links[l].weight + random.random()*step*2 - step
	else:
		chromosome.links[l].weight = random.random()*4 - 2
	return chromosome



def linkMutate(chromosome, innovationNumber):#consider where to increment innovation Number
	'''
	returns link array which has to be replaced with the chromosome link array in the main mutate function
	'''
	
	n1 = random.choice(chromosome.inputNeurons + chromosome.hiddenNeurons + chromosome.outputNeurons)
	n2 = random.choice(chromosome.inputNeurons + chromosome.hiddenNeurons + chromosome.outputNeurons)

	neuron1=n1.number
	neuron2=n2.number

	#print("neuron1", neuron1)
	#print("neuron2", neuron2)

	#if same them return same link
	if neuron1 == neuron2:
		return chromosome
	#if both inputs then return same
	if neuron1 < len(chromosome.inputNeurons) and neuron2 < len(chromosome.inputNeurons):
		return chromosome

	#if neuron2 is input and 1 is not then flip
	if neuron2 < len(chromosome.inputNeurons):
		neuron1, neuron2 = neuron2, neuron1

	#if link alread exists then return
	for i in chromosome.links:
		if neuron1 == i.neuron1 and neuron2 == i.neuron2:
			return chromosome

	newLink = link(neuron1, neuron2, True, random.random()*4 - 2, innovationNumber)
	chromosome.links.append(newLink)
	chromosome.addIncomingLinkToNeurons(newLink,neuron2)
	return chromosome


def nodeMutate(chromosome, innovationNumber):
	if len(chromosome.links)<=0:
		return chromosome
	l=random.randint(0,len(chromosome.links)-1)
	if not chromosome.links[l].isEnabled:
		return chromosome

	neuron1=chromosome.links[l].neuron1
	neuron2=chromosome.links[l].neuron2


	newNeuron=neuron(len(chromosome.inputNeurons)+len(chromosome.hiddenNeurons))
	chromosome.hiddenNeurons.append(newNeuron)
	chromosome.links[l].isEnabled=False

	newLink1=link(neuron1, newNeuron.number, True, 1, innovationNumber)
	newLink2=link(newNeuron.number, neuron2, True, chromosome.links[l].weight, innovationNumber)

	chromosome.links.append(newLink1)
	chromosome.addIncomingLinkToNeurons(newLink1,newNeuron.number)
	chromosome.links.append(newLink2)
	chromosome.addIncomingLinkToNeurons(newLink2,neuron2)

	return chromosome


'''
c = chromosome()
c.showChromosome()
for i in range(10):
	c=mutate(c,1)
c.showChromosome()
'''





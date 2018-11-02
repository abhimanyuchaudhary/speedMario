from chromosome import link, chromosome
from random import randint
import random

def mutate(chromosome, innovationNumber):
	PROBABILITY_enableDisable = 1
	PROBABILITY_linkMutate = 1
	PROBABILITY_pointMutate = 1
	PROBABILITY_nodeMutate = 1



	print("her")
	return chromosome
def enableDisableMutate(link):
	#enables/disables link
	link.isDisabled != link.isDisabled
	return link

def pointMutate(link):
	perturbChance = 3
	step = 1
	#when do we decrease
	if(randint(0, 10) < perturbChance):
		link.weight = link.weight + random.random() * step*2 - step
	else:
		link.weight = random.random()*4 - 2
	return link
def linkMutate(chromosome, innovationNumber):#consider where to increment innovation Number
	'''
	returns link array which has to be replaced with the chromosome link array in the main mutate function
	'''
	
	neuron1 = random.choice(chromosome.inputNeurons + chromosome.hiddenNeurons + chromosome.outputNeurons)
	neuron2 = random.choice(chromosome.inputNeurons + chromosome.hiddenNeurons + chromosome.outputNeurons)

	#if same them return same link
	if(neuron1 == neuron2):
		return chromosome.links
	#if both inputs then return same
	if(neuron1 < 16 and neuron2 < 16):
		return chromosome.links

	#if neuron2 is input and 1 is not then flip
	if(neuron2 < 16):
		neuron1, neuron2 = neuron2, neuron1
	#if both output then returns same, idk why he didn't consider this
	if(neuron1 >= 2000 and neuron2 >= 200):
		return chromosome.links
	#fliping if neuron 1 is output
	if(neuron1 >= 2000):
		neuron1, neuron2 = neuron2, neuron1
	#if link alread exists then return
	for i in chromosome.links:
		if(neuron1 == i.neuron1 and neuron2 == i.neuron2):
			return chromosome.links

	newLink = link(neuron1, neuron2, False, random.random()*4 - 2, innovationNumber)
	chromosome.links.append(newLink)
	return chromosome.links

c = chromosome







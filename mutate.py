from chromosome import link, chromosome
from random import randint
import random

def mutate(chromosome):
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
def linkMutate(chromosome):
	



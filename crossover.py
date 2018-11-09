from chromosome import link, chromosome
from copy import deepcopy
import random

PROBABILITY_fitParent = 0.5

def crossover(c1, c2):
	child = chromosome()
	childLinks = []
	fitParent = chromosome()
	nonFitParent = chromosome()

	if(c1.fitnessValue <= c2.fitnessValue):
		fitParent = c1
		nonFitParent = c2
	else:
		fitParent = c2
		nonFitParent = c1

	fitParentLinks = deepcopy(fitParent.links)
	nonFitParentLinks = deepcopy(nonFitParent.links)

	fitParentLinks = sorted(fitParentLinks)
	nonFitParentLinks = sorted(nonFitParentLinks)

	i = 0
	j = 0
	while(i < len(fitParentLinks) and j < len(nonFitParentLinks)):
		if(fitParentLinks[i].innovation == nonFitParentLinks[j].innovation):
			if(random.random() < PROBABILITY_fitParent):
				childLinks.append(fitParentLinks[i])
			else:
				childLinks.append(nonFitParentLinks[i])
			i = i + 1
			j = j + 1

		elif(fitParentLinks[i].innovation < nonFitParentLinks[j].innovation):
			childLinks.append(fitParentLinks[i])
			i = i + 1
		else:
			j = j + 1

	child.links = deepcopy(childLinks)
	return child









	return c1
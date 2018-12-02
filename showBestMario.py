from nes_py.wrappers import BinarySpaceToDiscreteSpaceEnv
import gym_super_mario_bros
from gym_super_mario_bros.actions import COMPLEX_MOVEMENT
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = BinarySpaceToDiscreteSpaceEnv(env, COMPLEX_MOVEMENT)
import time
from chromosome import link, chromosome, neuron
from mutate import mutate
from crossover import crossover
from population import population
from copy import deepcopy
import csv
import math



#GAME RUNNING GAME RUNNING GAME RUNNING GAME RUNNING GAME RUNNING GAME RUNNING GAME RUNNING GAME RUNNING#
def show_input(inp):
    for i in range(12):
        for j in range(12):
            print(inp[i*12+j],end=" ")
        print()    

def show_info(info):
    print("coins: "+str(info['coins']),end=", ")
    print("flag_get: "+str(info['flag_get']),end=", ")
    print("life: "+str(info['life']),end=", ")
    print("score: "+str(info['score']),end=", ")
    print("stage: "+str(info['stage']),end=", ")
    print("status: "+str(info['status']),end=", ")
    print("time: "+str(info['time']),end=", ")
    print("world: "+str(info['world']),end=", ")
    print("x_pos: "+str(info['x_pos']),end=", ")
    print("y_pos: "+str(info['y_pos']),end="\n\n")


def sigmoid(S):
    if S==0:
        return 0
    return 2/(1+math.exp(-1*S))


def getNetworkOutput(nn,input):
    for i in range(len(input)):
        nn.inputNeurons[i].val=input[i]

    for i in range(len(nn.hiddenNeurons)):
        S=0
        for link in nn.hiddenNeurons[i].incomingLinks:
            if nn.links[link].isEnabled:
                #link.neuron1<link.neuron2 always
                value=nn.getValue(nn.links[link].neuron1)
                S=S+nn.links[link].weight*value
        nn.hiddenNeurons[i].val=sigmoid(S)


    maxVal=-2
    maxIndex=-1
    for i in range(len(nn.outputNeurons)):
        S=0
        for link in nn.outputNeurons[i].incomingLinks:
            if nn.links[link].isEnabled:
                #link.neuron1<link.neuron2 always
                value=nn.getValue(nn.links[link].neuron1)
                S=S+nn.links[link].weight*value
        nn.outputNeurons[i].val=sigmoid(S)
        if maxVal<nn.outputNeurons[i].val:
            maxVal=nn.outputNeurons[i].val
            maxIndex=i
    return maxIndex

def getBestMario(p):
	bestMario = p.populationSpecies[0].subpopulation[0]
	print("AAA",p.populationSpecies[0].subpopulation[0].fitnessValue)
	for i in range(len(p.populationSpecies)):#populationSpecies in p.populationSpecies:
		for j in range(len(p.populationSpecies[i].subpopulation)):#mario in populationSpecies.subpopulation:

			#if(mario.fitnessValue > 1000):
			#	print(mario.fitnessValue)
			if(bestMario.fitnessValue < p.populationSpecies[i].subpopulation[j].fitnessValue):
				bestMario = deepcopy(p.populationSpecies[i].subpopulation[j])
				print("GGGG:",p.populationSpecies[i].subpopulation[j].fitnessValue,i,j)
            # print(bestMario.fitnessValue)
        # bestMario = max(bestMario, max(populationSpecies.subpopulation))
	return bestMario

population=population(300)
# print("Enter generation number to load or -1 to randomly initialize")
# genNumber = int(input())
# if(genNumber == -1):
#     population.initializePopulation()
# else:
#     population.load(genNumber)
#population.printPopulation()
for genNumber in range(1, 600):
	count=0
	prev_xpos=0
	done = False
	start = True
	population.load(int(94))

	currentNN = getBestMario(population)
	#break;
	print(currentNN.fitnessValue)
	state = env.reset()
	state, reward, done, info = env.step(0)
	distance = 0
	while True:
	    #Checks if NN is done running or Mario stays still for 10 counts
		if info['life']<3 or done or info['stage'] != 1 or count > 25:
		    print("Generation", genNumber, "Distance", distance)
		    # currentNN.showChromosome()
		    # print(len(currentNN.links))
		    break
		  
		#use input to calculate next move M  
		M=getNetworkOutput(currentNN,info['inp'])
		if(info['x_pos'] <= 2330 and info['x_pos'] >= 2130):
		    state, reward, done, info = env.step(5)
		    state, reward, done, info = env.step(1)
		if(info['x_pos'] <= 2430 and info['x_pos'] >= 2390):
		    state, reward, done, info = env.step(5)
		    state, reward, done, info = env.step(1)
		elif(info['x_pos'] >= 2900):
		    state, reward, done, info = env.step(5)
		    state, reward, done, info = env.step(5)
		    state, reward, done, info = env.step(1)
	    
		else:
			state, reward, done, info = env.step(M)


		xval=info['x_pos']
		# print(currentNN.fitnessValue, xval)
		if prev_xpos>=xval:
			# print("here")
			count+=1
		else:
			count=0
		# print(count)	        
		prev_xpos=xval
		currentNN.fitnessValue = max(xval,currentNN.fitnessValue)
		#print(xval)

	    #show_info(info)
	    #print(len(info['inp']))
	    #show_input(info['inp'])
	    #print("X--------------------X")
		env.render()
		if(info['stage'] == 1):
			distance = info['x_pos']

env.close()

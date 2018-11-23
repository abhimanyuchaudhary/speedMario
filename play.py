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

    #print("Output: ",end='')
    #for i in nn.outputNeurons:
    #    print(i.val,end=" ")
    #print()
    #print(maxIndex)
    return maxIndex


population=population(300)
print("Enter generation number to load or -1 to randomly initialize")
genNumber = int(input())
if(genNumber == -1):
    population.initializePopulation()
else:
    population.load(genNumber)
#population.printPopulation()
count=0
prev_xpos=0
done = False
start = True
while 1>0:
    #Checks if first NN is to be loaded
    if(start):
        start = False
        state = env.reset()
        currentNN = population.fetchNext()#load new nn
        if not currentNN:
            break
        state, reward, done, info = env.step(0)

    #Checks if NN is done running or Mario stays still for 10 counts
    if info['life']<3 or done or count>25:
        #print("life",info['life'],"count",count)
        count = 0
        if currentNN.fitnessValue>population.maxFitness:
            population.maxFitness=currentNN.fitnessValue
        #print("R")
        state = env.reset()
        currentNN = population.fetchNext()#load new nn
        if not currentNN:
            #remove weak individuals, generate new population
            #break
            population.nextGen()
            currentNN=population.fetchNext()
        state, reward, done, info = env.step(0)

      
    #use input to calculate next move M  
    
    M=getNetworkOutput(currentNN,info['inp'])
    state, reward, done, info = env.step(M)#play M


    xval=info['x_pos']
    if xval==2226:
        xval=2146


    if currentNN.fitnessValue+2>=xval:
        count+=1
    else:
        count=0
    prev_xpos=xval
    currentNN.fitnessValue = max(xval,currentNN.fitnessValue)

    #show_info(info)
    #print(len(info['inp']))
    #show_input(info['inp'])
    #print("X--------------------X")
    env.render()

env.close()

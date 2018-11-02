from nes_py.wrappers import BinarySpaceToDiscreteSpaceEnv
import gym_super_mario_bros
from gym_super_mario_bros.actions import COMPLEX_MOVEMENT
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = BinarySpaceToDiscreteSpaceEnv(env, COMPLEX_MOVEMENT)
import time
from chromosome import link, chromosome
from mutate import mutate
from crossover import crossover
from population import population





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


def getNetworkOutput(nn,input):
    return env.action_space.sample()







population=population(5)
population.initializePopulation()
count=0
prev_xpos=0
done = True
for step in range(1000):
    if done or count>10:
        count=0
        print("Reset")
        state = env.reset()
        currentNN=population.fetchNext()#load new nn
        if not currentNN:
            break
        state, reward, done, info = env.step(0)

      
    #use input to calculate next move M  
    M=getNetworkOutput(currentNN,info['inp'])
    state, reward, done, info = env.step(M)#play M
    time.sleep(.010)

       
    if prev_xpos>=info['x_pos']:
        count+=1
    else:
        count=0
    prev_xpos=info['x_pos']

    #show_info(info)
    #print(len(info['inp']))
    #show_input(info['inp'])
    #print("X--------------------X")
    env.render()

env.close()
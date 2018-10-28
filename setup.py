from nes_py.wrappers import BinarySpaceToDiscreteSpaceEnv
import gym_super_mario_bros
from gym_super_mario_bros.actions import COMPLEX_MOVEMENT
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = BinarySpaceToDiscreteSpaceEnv(env, COMPLEX_MOVEMENT)
import time

class link:
    def __init__(self, neuron1, neuron2, isDisabled = False, weight = 1, generation = -1):
        self.neuron1 = neuron1
        self.neuron2 = neuron2
        self.isDisabled = isDisabled
        self.weight = weight
        self.generation = generation
    def showLink(self):
        print("Neuron 1 ", self.neuron1)
        print("Neuron 2 ", self.neuron2)
        print("weight", self.weight)
        print("Generation", self.generation)

class chromosome:
    def __init__(self):
        self.inputNeurons = []
        self.outputNeurons = []
        self.hiddenNeurons = []
        self.links = []

def mutate(chromosome):
    return chromosome
def crossover(c1, c2):
    return c1

a = link(1, 2, True)
a.showLink();



#GAME RUNNING GAME RUNNING GAME RUNNING GAME RUNNING GAME RUNNING GAME RUNNING GAME RUNNING GAME RUNNING#
# def show_input(inp):
#     for i in range(12):
#         for j in range(12):
#             print(inp[i*12+j],end=" ")
#         print()    

# def show_info(info):
#     print("coins: "+str(info['coins']),end=", ")
#     print("flag_get: "+str(info['flag_get']),end=", ")
#     print("life: "+str(info['life']),end=", ")
#     print("score: "+str(info['score']),end=", ")
#     print("stage: "+str(info['stage']),end=", ")
#     print("status: "+str(info['status']),end=", ")
#     print("time: "+str(info['time']),end=", ")
#     print("world: "+str(info['world']),end=", ")
#     print("x_pos: "+str(info['x_pos']),end=", ")
#     print("y_pos: "+str(info['y_pos']),end="\n\n")



# count=0
# prev_xpos=0
# done = True
# for step in range(1000):
#     if done or count>3:
#         count=0
#         print("Reset")
#         state = env.reset()
#         #load new nn
#         #state, reward, done, info = env.step(0)

      
#     #use input to calculate next move M    
#     state, reward, done, info = env.step(env.action_space.sample())#play M
#     time.sleep(.010)

       
#     if prev_xpos==info['x_pos']:
#         count+=1
#     else:
#         count=0
#     prev_xpos=info['x_pos']

#     show_info(info)
#     #print(len(info['inp']))
#     show_input(info['inp'])
#     print("X--------------------X")
#     env.render()

# env.close()
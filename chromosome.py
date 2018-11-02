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
        #2000 +
        self.outputNeurons = []
        self.hiddenNeurons = []
        self.links = []
        for i in range(16):
            inputNeurons.append(i)
        for i in range(2000, 2000+12):
            outputNeurons.append(i)
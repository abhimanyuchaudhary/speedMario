class link:
    def __init__(self, neuron1, neuron2, isDisabled = False, weight = 1, innovation= -1):
        self.neuron1 = neuron1
        self.neuron2 = neuron2
        self.isDisabled = isDisabled
        self.weight = weight
        self.innovation = innovation
    def showLink(self):
        print("Neuron 1 ", self.neuron1)
        print("Neuron 2 ", self.neuron2)
        print("weight", self.weight)
        print("Generation", self.innovation)

class chromosome:
    def __init__(self):
        self.inputNeurons = []
        #2000 +
        self.outputNeurons = []
        self.hiddenNeurons = []
        self.links = []
        for i in range(16):
            self.inputNeurons.append(i)
        for i in range(2000, 2000+12):
            self.outputNeurons.append(i)
    def showChromosome(self):
        print("Input", self.inputNeurons)
        print("Hidden", self.hiddenNeurons)
        print("Output", self.outputNeurons)
        for i in self.links:
            i.showLink()
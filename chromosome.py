
class neuron:
    def __init__(self,n):
        self.number=n
        self.val=0
        self.incomingLinks=[]

    def showNeuron(self):
        print(str(self.number),end=" ")

    def addLink(self,l):
        self.incomingLinks.append(l)

class link:

    def __init__(self, neuron1, neuron2, isEnabled = True, weight = 1, innovation= -1):
        self.neuron1 = neuron1
        self.neuron2 = neuron2
        self.isEnabled = isEnabled
        self.weight = weight
        self.innovation = innovation
    def __lt__(self, other):
         return self.innovation < other.innovation
    def __eq__(self, other):
        return self.innovation == other.innovation
    
    def showLink(self):
        print("Neuron 1 ", self.neuron1)
        print("Neuron 2 ", self.neuron2)
        print("weight", self.weight)
        print("Generation", self.innovation)
        print()

class chromosome:

    def __init__(self):
        self.inputNeurons = []
        #2000 +
        self.outputNeurons = []
        self.hiddenNeurons = []
        self.links = []
        self.fitnessValue = 0
        for i in range(145):
            self.inputNeurons.append(neuron(i))
        self.inputNeurons[144].val=1        #bias neuron
        for i in range(2000, 2000+12):
            self.outputNeurons.append(neuron(i))
    def __lt__(self, other):
         return self.fitnessValue < other.fitnessValue
    def __eq__(self, other):
        return self.fitnessValue == other.fitnessValue

    def showChromosome(self):
        print("Input: ",end='')
        for i in self.inputNeurons:
            i.showNeuron()
        print()
        print("Hidden: ",end='')
        for i in self.hiddenNeurons:
            i.showNeuron()
        print()
        print("Output: ",end='')
        for i in self.outputNeurons:
            i.showNeuron()
        print("\n")
        for i in self.links:
            i.showLink()

    def addIncomingLinkToNeurons(self,l,n):
        if not l.neuron2==n or n<len(self.inputNeurons):
            return
        if 2012>n and n>=2000:
            self.outputNeurons[n-2000].addLink(l)

        if len(self.hiddenNeurons)+len(self.inputNeurons)>n and n>=len(self.inputNeurons):
            self.hiddenNeurons[n-len(self.inputNeurons)].addLink(l)


    def getValue(self,n):
        if n<len(self.inputNeurons):
            return self.inputNeurons[n].val
        elif n<len(self.hiddenNeurons)+len(self.inputNeurons):
            return self.hiddenNeurons[n-len(self.inputNeurons)].val
        elif n>=2000 and n<2012:
            return self.outputNeurons[n-2000].val

        print("ERRORRRRRRRR")
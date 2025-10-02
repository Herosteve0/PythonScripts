import random
import math

def sigmoid(x: float) -> float: return 1 / (1 + math.exp(-x))
def calcError(x: float, c: float) -> float: return (x - c)**2

class NeuronConnection:
    def __init__(self, nfrom, nto, w: float = 1):
        self.nfrom = nfrom
        self.nto = nto
        self.weight = w

    def AdjustWeightBy(self, value: float):
        self.weight += value

    def Output(self) -> float:
        return self.weight * self.nfrom.value

class Neuron:
    def __init__(self, bias: float = 0):
        self.bias = bias
        self.value = 0
        self.connections = []

    def AdjustBiasBy(self, value: float):
        self.bias += value

    def Output(self, inp: float) -> float:
        r = self.bias
        for n in self.connections:
            r += n.Output()
        return sigmoid(r)

    def MakeConnection(self, *n):
        for i in n:
            if isinstance(i, type(self)):
                continue
            self.connections.append(NeuronConnection(i, self)) # connections all given n Neurons to this Neuron

    def __str__(self):
        return f"Bias: {self.bias}, Connections: {len(self.connections)}"

def Train(inpn: list[Neuron], outn: list[Neuron], inp: list[float], out: list[float]):
    return



n = [[Neuron()] * (28**2),
     [Neuron()] * 16,
     [Neuron()] * 16,
     [Neuron()] * 10
     ]
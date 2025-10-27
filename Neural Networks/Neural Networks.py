import random
from math import exp

from fontTools.subset import neuter_lookups


def sigmoid(x: float) -> float: return 1 / (1 + exp(-x))
def sigmoid_derivative(x: float) -> float: return exp(-x) / ((1 + exp(-x)) ** 2)

class NeuronConnection:
    def __init__(self, nfrom, nto, w: float = 1):
        self.nfrom = nfrom
        self.nto = nto
        self.weight = w

    def AdjustWeightBy(self, value: float):
        self.weight += value

    def Output(self) -> float:
        return self.weight * self.nfrom.value

    def CalcValue(self, inp: float) -> float:
        return self.weight * self.nfrom.Output(inp)

class Neuron:
    def __init__(self, bias: float = 0):
        self.bias = bias
        self.value = 0
        self.rawvalue = 0
        self.connections = []

    def AdjustBiasBy(self, value: float):
        self.bias += value

    def SetValue(self, value: float):
        self.value = value

    def Output(self) -> float:
        r = self.bias
        for n in self.connections:
            r += n.Output()
        return sigmoid(r)

    def UpdateData(self):
        r = self.bias
        for n in self.connections:
            r += n.Output()
        self.value = sigmoid(r)
        self.rawvalue = r

    def CalcCellValue(self, inp: float) -> float:
        if len(self.connections) == 0:
            return inp
        r = self.bias
        for neuron in self.connections:
            r += neuron.Output()
        return sigmoid(r)

    def MakeConnection(self, neurons):
        for i in neurons:
            if not isinstance(i, type(self)): continue
            if i == self: continue
            self.connections.append(NeuronConnection(i, self)) # connections all given n Neurons to this Neuron

    def __str__(self):
        return f"Bias: {self.bias}, Connections: {len(self.connections)}"

def Train(inpn: list[Neuron], outn: list[Neuron], inp: list[float], out: list[float]):
    return

def MakeConnections():
    global n

    for pack in range(len(n)-1):
        for ne in n[pack+1]:
            ne.MakeConnection(n[pack])

#n = [[Neuron()] * (28**2),
#     [Neuron()] * 16,
#     [Neuron()] * 16,
#     [Neuron()] * 10
#     ]

n = [
    [Neuron()] * 1,
    [Neuron()]
]
MakeConnections()

def GetNetworkOutcome(neurons: list[list[Neuron]], inputs: list[float]) -> list[float]:
    output = []

    length_neuron = len(neurons)
    for layer in range(length_neuron):
        length_layer = len(neurons[layer])
        for i in range(length_layer):
            if layer == 0:
                neurons[layer][i].SetValue(inputs[i])
            else:
                neurons[layer][i].UpdateData()
                if layer == length_neuron - 1:
                    output.append(neurons[layer][i].value)

    return output

def AdjustNetworkValues(goal):
    global n

    length_network = len(n)

    output = []

    for layer in range(length_network-1, 0, -1):
        length_layer = len(n[layer])
        output = [0] * len(n[layer-1])
        for index in range(length_layer):
            neuron = n[layer][index]

            if layer == length_network-1:
                cost_der = 2*(neuron.value - goal[index])
            else:
                cost_der = 2*(neuron.value - output[index])
            sigm_der = sigmoid_derivative(neuron.rawvalue)

            mult = cost_der * sigm_der

            connections = neuron.connections
            length_connections = len(connections)

            for connection_index in range(length_connections):
                w = connections[connection_index].weight
                v = connections[connection_index].nfrom.value

                connections[connection_index].AdjustWeightBy(mult * v)
                neuron.AdjustBiasBy(mult)
                output[connection_index] += mult * w # required that the connections are the same as the n[layer]

def cost(value: float, expected_value: float) -> float:
    return (value - expected_value) ** 2

def expected(x1: float, x2: float) -> float:
    return x1*x1 - x2*2 + 3

def faketrain(loops: int = 100):
    for i in range(loops):
        values = [random.random(), random.random()] * 10

        y = [expected(values[0], values[1])]
        AdjustNetworkValues(y)

faketrain(300)

print(GetNetworkOutcome(n, [3, 6]))
print(expected(3, 6))
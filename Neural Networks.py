import random
import math

def sigmoid(x: float) -> float: return 1 / (1 + math.exp(-x))
def calcError(x: float, c: float) -> float: return (x - c)**2

class NeuronConnection:
    def __init__(self, nfrom, nto, w: float):
        self.nfrom = nfrom
        self.nto = nto
        self.w = w

    def AdjustWeightBy(self, value: float): self.w += value

    def Output(self, x: float) -> float: return self.w * x

class Neuron:
    def __init__(self, weight: float, bias: float):
        self.b = bias
        self.connections = []

    def AdjustBiasBy(self, value: float): self.b += value

    def Output(self, inp: float) -> float: return self.w * inp + self.b

    def MakeConnection(self, *n):
        for i in n:
            if isinstance(i, type(self)):
                continue
            self.connections.append(NeuronConnection(i, self, 1)) # connections all given n Neurons to this Neuron

    def __str__(self):
        return f"Weight: {self.w}, Bias: {self.b}, Equation: {self.w}*input + {self.b}"


















def Data(inp: list[float]) -> float:
    if len(inp) != 2: return 0
    return inp[0]+ 2*inp[1] + 1

n = [Neuron(1, 0), Neuron(1, 0)]
n[1].MakeConnection(n[0])

for i in range(10000):
    inp = [float(random.randint(1, 20)), float(random.randint(1, 20))]
    data = Data(inp)
    prediction = 1
    for j in range(len(n)):
        prediction *= n[j].Output(inp[j])
    error = prediction - data
    for j in range(len(n)):
        n[j].AdjustWeightBy(-error * 0.001 * inp[j])
        n[j].AdjustBiasBy(-error * 0.5)

print(Data([10, 15]))
print(n[0].Output(10)*n[1].Output(15))
for i in range(len(n)):
    print(n[i])
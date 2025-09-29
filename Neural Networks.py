import random


class Neuron:
    def __init__(self, weight: float, bias: float):
        self.w = weight
        self.b = bias

    def AdjustWeightBy(self, value: float): self.w += value

    def AdjustBiasBy(self, value: float): self.b += value

    def Output(self, inp: float) -> float: return self.w * inp + self.b

def Data(inp: float) -> float: return inp/1.5

n = Neuron(1, 0)
for i in range(15):
    inp = random.randint(1, 20)
    data = Data(inp)
    prediction = n.Output(inp)
    error = prediction - data
    n.AdjustWeightBy(-error * 0.1)

print(Data(100))
print(n.Output(100))
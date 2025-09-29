import random


class Neuron:
    def __init__(self, weight: float, bias: float):
        self.w = weight
        self.b = bias

    def AdjustWeightBy(self, value: float): self.w += value

    def AdjustBiasBy(self, value: float): self.b += value

    def Output(self, inp: float) -> float: return self.w * inp + self.b

    def __str__(self):
        return f"Weight: {self.w}, Bias: {self.b}, Equation: {self.w}*input + {self.b}"

def Data(inp: float) -> float: return inp/1.5 + 5

n = Neuron(1, 0)
for i in range(1000000):
    inp = random.randint(1, 1)
    data = Data(inp)
    prediction = n.Output(inp)
    error = prediction - data
    n.AdjustWeightBy(-error * 0.1)
    n.AdjustBiasBy(-error * 0.5)

print(Data(100))
print(n.Output(100))
print(n)
class plug:
    def __init__(self, outputs):
        self.outputs = outputs

        self.outcount = len(outputs)

    def PassData(self, inp):
        for i in range(len(self.outputs)):
            self.outputs = inp

class extension(plug):
    def __init__(self, output):
        super().__init__([output])

a = extension("meow")
b = plug(["meow"])

if a.outcount == b.outcount:
    print("same count")
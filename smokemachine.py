import random

class SmokeMachine():
    def __init__(self, pos):
        self.pos = pos
        self.smoke_bubbles = []
        self.flow = 0

    def startSmoke(self):
        self.flow = 1

    def stopSmoke(self):
        self.flow = 0

    def stepChange(self, stgsize, dir):
        if self.flow == 1:
            smoke = [self.pos[0], self.pos[1], len(self.smoke_bubbles)]
            self.smoke_bubbles.append(smoke)
        for s in self.smoke_bubbles:
            r, c = 0, 0
            if dir == "right":
                if ( s[0]+100 < stgsize-10 or s[1]+20 < stgsize):
                    r = random.randint(s[0], s[0]+100)
                    c = random.randint(s[1], s[1]+20)
                else:
                    print(True)
                    r = stgsize
                    c = random.randint(s[1], stgsize)
                    print(r, c)
            elif dir == "left":
                if (s[0]-100 > 0 or s[1]+20 < stgsize):
                    r = random.randint(s[0]-100, s[0])
                    c = random.randint(s[1], s[1]+20)
                else:
                    r = 0
                    c = random.randint(s[1], stgsize)
            s[0] = r
            s[1] = c
        xvalues = [s[0] for s in self.smoke_bubbles]
        yvalues = [s[1] for s in self.smoke_bubbles]
        
        size = []
        alfa = []
        for i in range(len(self.smoke_bubbles)):
            size.append(random.randint(100, 600))
            alfa.append(1)#(i/len(self.smoke_bubbles)))
        return ([xvalues, yvalues, size, "white", alfa])

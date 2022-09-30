import random
class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for i in kwargs:
            for item in range(kwargs[i]):
                self.contents.append(i)

    def draw(self,number):
        """A draw method that accepts
        an argument indicating the number
        of balls to draw from the hat"""
        if number > len(self.contents):
            return self.contents
        showglass = []
        for ball in range(number):
            pick = self.contents.pop(random.randint(0,len(self.contents)-1))
            showglass.append(pick)

        self.contents = self.contents + showglass
        return showglass

def experiment(hat=None,expected_balls=None,num_balls=None,num_experiments=None):
    sum = 0
    for exp in range(num_experiments):
        drawn = hat.draw(num_balls)
        validity = []
        for i in expected_balls:
            if drawn.count(i) >= expected_balls[i]:
                validity.append(True)
            else:
                validity.append(False)
        if False not in validity:
            sum += 1
        else:
            sum += 0

    probability = sum/num_experiments

    return probability

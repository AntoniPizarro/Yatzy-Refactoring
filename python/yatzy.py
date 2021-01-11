class Yatzy:

    @staticmethod
    def chance(*dices):
        total = 0
        for val in dices:
            total += val
        return total

    @staticmethod
    def yatzy(dice):
        counts = [0]*(len(dice)+1)
        for die in dice:
            counts[die-1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0
    
    @staticmethod
    def ones(*dices):
        sum = 0
        for dice in dices:
            if dice == 1:
                sum += 1
        return sum
    

    @staticmethod
    def twos(*dices):
        sum = 0
        for dice in dices:
            if dice == 2:
                sum += 2
        return sum
    
    @staticmethod
    def threes(*dices):
        sum = 0
        for dice in dices:
            if dice == 3:
                sum += 3
        return sum
    

    def __init__(self, *dices):
        self.dice = [0]*len(dices)
        i = 0
        for dice in dices:
            self.dice[i] = dice
            i += 1
    
    def fours(self):
        sum = 0
        for i in range(len(self.dice)):
            if self.dice[i] == 4:
                sum += 4
        return sum
    

    def fives(self):
        sum = 0
        for i in range(len(self.dice)): 
            if (self.dice[i] == 5):
                sum += 5
        return sum
    

    def sixes(self):
        sum = 0
        for i in range(len(self.dice)): 
            if (self.dice[i] == 6):
                sum += 6
        return sum
    
    @staticmethod
    def score_pair(*dices):
        res = 0
        for dice in dices:
            if dices.count(dice) >= 2 and dice > res:
                res = dice
        return res * 2
    
    @staticmethod
    def two_pair(*dices):
        res1 = 0
        res2 = 0
        for dice in dices:
            if dices.count(dice) >= 2 and dice > res1:
                res1 = dice
        for dice in dices:
            if dices.count(dice) >= 2 and dice < res1 and dice > res2 or dices.count(dice) >= 4:
                res2 = dice
        if res1 > 0 and res2 > 0:
            return res1 * 2 + res2 * 2
        else:
            return 0
    
    @staticmethod
    def four_of_a_kind(*dices):
        res = 0
        for dice in dices:
            if dices.count(dice) >= 4 and dice > res:
                res = dice
        return res * 4
    

    @staticmethod
    def three_of_a_kind(*dices):
        res = 0
        for dice in dices:
            if dices.count(dice) >= 3 and dice > res:
                res = dice
        return res * 3
    

    @staticmethod
    def smallStraight(*dices):
        vals = list(dices)
        vals.sort()
        compr = False
        res = 0
        for i in range(len(vals)):
            if vals[i] == i + 1:
                compr = True
            else:
                compr = False
                break
            res += vals[i]
        if compr == True:
            return res
        else:
            return 0
    

    @staticmethod
    def largeStraight(*dices):
        vals = list(dices)
        vals.sort()
        compr = False
        res = 0
        for i in range(len(vals)):
            if vals[i] == i + 2:
                compr = True
            else:
                compr = False
                break
            res += vals[i]
        if compr == True:
            return res
        else:
            return 0
    

    @staticmethod
    def fullHouse(*dices):
        res1 = 0
        res2 = 0
        sum = 0
        i = 0
        while res1 == 0 and i < len(dices):
            if dices.count(dices[i]) == 2:
                res1 = dices[i]
                sum += dices[i] * 2
                break
            i += 1
        i = 0
        while res2 == 0 and i < len(dices):
            if dices.count(dices[i]) == 3:
                res2 = dices[i]
                sum += dices[i] * 3
                break
            i += 1
        if res1 != 0 and res2 != 0:
            return sum
        else:
            return 0

if __name__ == "__main__":
        assert 0 == Yatzy.fullHouse(2,3,4,5,6)
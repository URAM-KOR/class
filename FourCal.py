class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = FourCal(4,2)
b = FourCal(3,7)

print(a.add())
print(a.mul())
print(a.div())
print(a.sub())

a = MoreFourCal(4, 2)
print(a.pow())

print(b.add())
print(b.mul())
print(b.div())
print(b.sub())

b = MoreFourCal(3,7)
print(b.pow())

class ExtendedList(list):
    def __init__(self, lst):
        super().__init__(lst)
        self.lst = lst

    def avg(self):
        return sum(self.lst) / len(self.lst)

    def __add__(self, other):
        return self.lst + other.lst

    def __gt__(self, other):
        return self.avg() > other.avg()

    def __ge__(self, other):
        return self.avg() >= other.avg()

    def __lt__(self, other):
        return self.avg() < other.avg()

    def __le__(self, other):
        return self.avg() >= other.avg()

    def __eq__(self, other):
        return self.avg() >= other.avg()

    def __ne__(self, other):
        return self.avg() != other.avg()


class TypeList(ExtendedList):
    def __eq__(self, other):
        return self.lst[-1] == other.lst[-1]

    def __ne__(self, other):
        return self.lst[-1] != other.lst[-1]

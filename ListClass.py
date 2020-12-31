class ExtendedList:
    def __init__(self, list):
        self.list = list

    def avg(self):
        sum_list = 0
        for num in self.list:
            sum_list += num
        return sum_list / len(self.list)

    def __add__(self, other):
        return self.list.extend(other.list)

    def __gt__(self, other):
        if self.avg() > other.avg():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.avg() >= other.avg():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.avg() < other.avg():
            return True
        else:
            return False

    def __le__(self, other):
        if self.avg() >= other.avg():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.avg() == other.avg():
            return True
        else:
            return False

    def __ne__(self, other):
        if self.avg() != other.avg():
            return True
        else:
            return False


class TypeList(ExtendedList):
    def __eq__(self, other):
        if self.list[-1] == other.list[-1]:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.list[-1] != other.list[-1]:
            return True
        else:
            return False

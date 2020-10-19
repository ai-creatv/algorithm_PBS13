import array

class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        # self.array = array.array(...) # TODO: self.array 생성
    
    def isEmpty(self):
        pass

    def prepend(self, value):
        pass

    def append(self, value):
        pass

    def setHead(self, index):
        pass

    def access(self, index):
        pass

    def insert(self, index, value):
        pass

    def remove(self, index):
        pass

    def print(self):
        pass
        


my_list = ArrayList(8)
my_list.print()

for i in range(10):
    my_list.append(i + 1)
my_list.print()

for i in range(10):
    my_list.prepend(i + 1)
my_list.print()

value = my_list.access(3)
print('my_list.access(3) = ' + str(value))

my_list.insert(8, 128)
my_list.print()

my_list.remove(4)
my_list.print()

my_list.setHead(10)
my_list.print()

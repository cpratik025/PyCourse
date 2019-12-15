class SuperList(list):

    def accessVariable(self,i):
        print(f"Value at position {i} is {self.list[i]}")
        return 'done'

    def __len__(self):
        return 1000


lst = SuperList()

print(len(lst))
lst.append(5)
print(lst)
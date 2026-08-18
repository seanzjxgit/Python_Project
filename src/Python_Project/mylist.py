class MyList:
    def __init__(self,lst):
        self.lst=lst

    def __iter__(self):
        return MyListIterator(self)
    


class MyListIterator:
    def __init__(self,my_list: MyList):
        self.my_list = my_list
        self.index =0

    def __next__(self):
        if self.index >= len(self.my_list.lst):
            raise StopIteration()
        result = self.my_list.lst[self.index]
        self.index +=1
        return result

    def __iter__(self):
        return self

mylist = MyList([2,3,3])
for i in  mylist:
    print(i)
def myrange(n):
    print("enter myrange")
    i = 0
    while i<n:
        yield i
        i+=1

result = myrange(2)
it = result.__iter__()
print(it.__next__())
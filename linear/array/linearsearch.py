llist = [2,3,4,5,6,7]
q = 6
if len(llist) > 0:
    print("list is not empty")
    for i in llist:
        if i == q:
            print("q is present : ", i)
        else:
            print("q is not present")
else:
    print("list is empty")
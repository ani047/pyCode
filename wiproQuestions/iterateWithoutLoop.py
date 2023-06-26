lst = [20,30,40,50,10,70]
start = int(input("Start Index:"))
end = int(input("Ending Index: "))
def iterators(l,s,e):
    if s<0 or s>=e:
        return
    print(l[s])
    iterators(l,s+1,e)

iterators(lst,start,end)


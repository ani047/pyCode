class Test:
    count=0
    def __init__(self):
        Test.count = Test.count + 1


t1 = Test()
t2 = Test()
print(Test.count)
t3 = Test()
print(Test.count)
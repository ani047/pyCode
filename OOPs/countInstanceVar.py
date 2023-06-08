class Test:
    a=0
    def __init__(self):
        self.a = self.a
        a = a + 1


t1 = Test()
t2 = Test()
print(Test.a)



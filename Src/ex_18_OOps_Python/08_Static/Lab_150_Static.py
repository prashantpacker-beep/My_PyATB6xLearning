class TestCounter:
    count= 0

    def __init__(self):
        TestCounter.count += 1

t1 = TestCounter()
t2 = TestCounter()
print(TestCounter.count)

#Each time the object is created counter is getting increased

#count is shared across all the objects

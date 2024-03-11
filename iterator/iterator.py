#example 1
print("="*10)

mytuple = ("Beans", "Toast", "Eggs")
myit = iter(mytuple)

for i in myit:
    print(i)

#example 2
print("="*10)

text = "bananas"
myit = iter(text)

for i in myit:
    print(i)

#example 3
print("="*10)
    
class MyClass:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyClass()
myiter = iter(myclass)

print(next(myiter))

#example 4 - stops after 20 iterations
print("="*10)

class MyClass2:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
myclass2 = MyClass2()
myiter2 = iter(myclass2)

for x in myiter2:
    print(x)
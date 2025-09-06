#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#cosntructor name should be__init__
#new keyword is not required when you're creating object

class Calculator:
    num = 100

    def __init__(self,a,b):
        self.FirstNum=a
        self.SecondNum=b
        print("I am called automatically when object is created")
    
    def GetData(self):
        print("I am not executing as a method in class")

    def Summation(self):
            return self.FirstNum+self.SecondNum + self.num

        
obj = Calculator(2, 3)
#obj.GetData()
#print(obj.Summation())

obj1 = Calculator(4, 9)
#obj1.GetData()
#print(obj1.Summation())
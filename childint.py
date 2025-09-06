#create a possibility to inherid everything from oopsdemo.py to this file - whicl will be child classes
#no need to declare everything from the beginning if these files're in the same folder
from OopsDemo import Calculator

class ChildImp(Calculator):
    num2=200

    def __init__(self, a, b):
        super().__init__(a, b)
        
    def getCompleteData(self):
        return self.num2 + self.num+self.Summation()
    
obj=ChildImp(2,4)
print(obj.getCompleteData())
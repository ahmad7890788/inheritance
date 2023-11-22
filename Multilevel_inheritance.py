class Grandfather1:  
  
    def __init__(self, grandfathername1):  
        self.grandfathername1 = grandfathername1  
  

class Father1(Grandfather1):  
    def __init__(self, fathername1, grandfathername1):  
        self.fathername1 = fathername1  
  
   
        Grandfather1.__init__(self, grandfathername1)  
  

class Son1(Father1):  
    def __init__(self,sonname1, fathername1, grandfathername1):  
        self.sonname1 = sonname1  
  
      
        Father1.__init__(self, fathername1, grandfathername1)  
  
    def print_name(self):  
        print('Grandfather name is :', self.grandfathername1)  
        print("Father name is :", self.fathername1)  
        print("Son name is :", self.sonname1)  
  

s1 = Son1('Ahmad', 'Nawaz', 'Ahmad')  
print (s1.grandfathername1)  
s1.print_name()  
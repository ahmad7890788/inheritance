
class Animal:  
    def func_1(self):  
        print ("Loin")  

class Birds1(Animal):  
    def func_2(self):  
        print ("lOVEBirds")  
  
 
class Birds2(Animal ):  
    def func_3(self):  
        print ("Lovebirds")  

object1 = Birds1()  
object2 = Birds2()  
object1.func_1()  
object1.func_2()  
object2.func_1()  
object2.func_3()  
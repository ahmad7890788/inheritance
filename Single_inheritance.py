###### Single inheritance
class Parent1:  
    def func_1(self):    
        print ("Hello")  
  
class Child1(Parent1):  
    def func_2(self):  
        print ("Ahmad Rajpoot")  

object = Child1()  
object.func_1()  
object.func_2()  

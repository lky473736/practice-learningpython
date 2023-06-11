class parent :
      def __init__ (self, a, b) :
            self.a = a
            self.b = b
      
      def printall (self) :
            print (self.a, self.b)
 
class child (parent) :
       def __init__ (self, a, b, k) :
             super().__init__ (a, b)
             self.k = k

p = child (1, 2, 3)
p.printall()
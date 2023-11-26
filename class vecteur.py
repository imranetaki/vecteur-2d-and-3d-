import math
class vecteur2D :
    _static_nbrv=0 
    def __init__(self , x , y) :  # def __init(self): 
        self.__x = x                #    self.x = 0
        self.__y = y                #    self.y = 0
        vecteur2D._static_nbrv += 1
    
    def getx(self) :
        return self.__x
     
    def gety(self) :
        return self.__y
     
    def getstatic_nbrv(self) :
        return self._static_nbrv
    
    def setx(self , x) :
        self.__x = x

    def sety(self , y) :
        self.__y = y

    def ToString(self) :
        return " abssice : " + str(self.__x) + " ordonnné : " + str(self.__y)
    
    def Equals (self , vec) :
        if self.__x == vec.getx() and self.__y == vec.gety() :
            return True
        else :
            False
    
    def Norme(self) :
        return math.sqrt(self.__x ** 2 + self.__y ** 2 ) 
    

class vecteur3D (vecteur2D) :
    def __init__(self, x , y , z):
        super().__init__( x , y  ) 
        self.__z = z 
    
    def getz(self) :
        return self.__z

    def setz(self , z) :
        self.__z = z

    def ToString(self):
        return super().ToString() + " 3 eme dimension : " + str(self.__z)
    
    def Equals(self, vec):
         if self.getx() == vec.getx() and self.gety() == vec.gety() and self.getz() == vec.getz() :
            return True
         else :
            False
        

    def Norme(self):
        return math.sqrt(self.getx() ** 2 + self.gety() ** 2 + self.getz() ** 2)

vec = vecteur2D(12 , 9)
vec1 = vecteur2D(12 , 9)
print(vec.Equals(vec1)) 
vec2 = vecteur3D(12 , 9  , 5)
vec4 = vecteur3D(12 , 9 , 5)
print(vec2.Equals(vec4)) 
print(vec4.getstatic_nbrv())





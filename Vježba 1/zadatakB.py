# b) Implementirati dvije klase (Point2D i Polar2D) koje predstavljaju dvodimenzionalnu točku u prostoru kao par kartezijevih i par polarnih koordinata. Obje klase će imati iduće funkcionalnosti koje će :
# -	Inicijailizaciju sa dvije koordinate za Point2D ili (kut, magntuda) za Polar2D 
# -	Pretvaranje u/iz polarnih koordinata u kartezijeve. Metoda vraća odgovarajuću klasu.
# -	Metodu __repr__ za pretvaranje u string
# -	Negaciju koordinate (unarni operator -) odnosno vektora. Metoda vraća novi objekt iste klase. 
# -	Zbroj dvije koordinate (binarni operator +) kao da su vektori. Metoda vraća novi objekt iste klase.
# -	Euklidova udaljenost među koordinatama
# -	Usporedbu == i !=
# Formule za pretvaranje u polarne koordinate:
# kut, magnituda = atan2(y, x), (x**2+y**2) ** 0.5
# Formule za pretvaranje u kartezijeve koordinate:
# x, y = cos(kut)*magnituda, sin(kut)*magnituda 
# Sve metode i operatori rade podjednako za obje klase u bilo kojoj kombinaciji. Za usporedbe jednakosti koristiti abs(a-b) < 0.01 umjesto a == b zbog ograničene preciznosti decimalnih brojeva.

# Funkcije i klase testirati na priloženom kôdu.
from math import atan2, cos, sin

class Polar2D:
    def __init__(self, kut, magnituda):
        self.kut = kut
        self.magnituda = magnituda

    def kart(self):
        x, y = cos(self.kut)*self.magnituda, sin(self.kut)*self.magnituda 
        return Point2D(x,y)
    
    def __repr__(self):
        return "Polar2D: " +str(self.kut)+" "+ str(self.magnituda)
    
    def udaljenost(self):
        return self.magnituda
    
    def __eq__(self,other):
        if isinstance(other,Point2D):
            other=other.polar()
        return abs(self.kut-other.kut) < 0.01 and abs(self.magnituda-other.magnituda) < 0.01
    
    def __ne__(self,other):
        if isinstance(other,Point2D):
            other=other.polar()
        return abs(self.kut-other.kut) > 0.01 or abs(self.magnituda-other.magnituda) > 0.01
    
    def __add__(self,other):
        if isinstance(other,Point2D):
            other=other.polar()
        return Polar2D(self.kut+other.kut,self.magnituda+other.magnituda)
    
    def __neg__(self,other):
        if isinstance(other,Point2D):
            other=other.polar()
        return Polar2D(self.x+other.kut,self.magnituda+other.magnituda)

#####

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def polar(self):
        kut, magnituda = atan2(self.y, self.x), pow((pow(self.x,2)+pow(self.y,2)), 0.5)
        return Polar2D(kut,magnituda)
    
    def __repr__(self):
        return "Point2D: " +str(self.x)+" "+ str(self.y)
    
    def udaljenost(self):
        return ((self.x - 0) ** 2 + (self.y - 0) ** 2) ** 0.5
    
    def __eq__(self,other):
        if isinstance(other,Polar2D):
            other=other.kart()
        return abs(self.x-other.x) < 0.01 and abs(self.y-other.y) < 0.01
    
    def __ne__(self,other):
        if isinstance(other,Polar2D):
            other=other.kart()
        return abs(self.x-other.x) > 0.01 or abs(self.y-other.y) > 0.01
    
    def __add__(self,other):
        if isinstance(other,Polar2D):
            other=other.kart()
        return Point2D(self.x+other.x,self.y+other.y)
    
    def __neg__(self,other):
        if isinstance(other,Polar2D):
            other=other.kart()
        return Point2D(self.x+other.x,self.y+other.y)


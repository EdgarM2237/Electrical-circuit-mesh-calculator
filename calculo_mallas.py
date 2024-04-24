"""
    Utilizacion del metodo Cramer para analisis de Mallas en circuitos electricos.
    En esta clase se hacen los calculos correspondientes al metodo Cramer haciendo
    el buen uso de los calculos de ecuaciones lineales.
"""

class MallaTec():
    def __init__(self,r1,r2,r3,v1,v2):
        self.r1=r1
        self.r2=r2
        self.v1=v1
        self.r3=r3
        self.v2=v2

    def kramer(self):
        a1=self.r1+self.r2
        b1=self.r2*-1
        c1=self.v1*-1

        a2=self.r2*-1
        b2=self.r2+self.r3
        c2=self.v2*-1
        det=(a1*b2)-(a2*b1)
        self.x=((b2*c1) - (b1*c2))/det
        self.y=((a1*c2) - (a2*c1))/det
        return self.x, self.y


G=6.61*10**-11
m_1=float(input("Enter mass of first object\n"))
m_2=float(input("Enter mass of second object\n"))
R=float(input("Enter distance between objects\n"))
def Gravitation_Force(m1,m2,r):
    F = (G*m1*m2)/(r*r)
    print(F)
Gravitation_Force(m_1,m_2,R)
import ord_E as o
import x3_y3 as r


def ord_a(a,b,x,y,p):
    for i in range(o.ord_E(a,b,p)):
        print(r.R(a,x,y,i*x,i*y,p))
    
a= 6#int(input("a: "))
b= 9#int(input("b: "))
# x= #int(input("x: "))
# y= #int(input("y: "))
p= 13#int(input("mod: "))
e = [(0,3),(0,10),(1,4),(1,9),(2,4),(2,9),(6,1),(6,12),(7,2),(7,11),(8,6),(8,7),(9,5),(9,8),(10,4),(10,9)]
for i in range(len(e)):
    ord_a(a,b,e[i][0],e[i][1],p)
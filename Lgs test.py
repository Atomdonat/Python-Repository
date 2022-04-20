def modinv(a):
    for i in range(1, 257):
        if((a%257)*(i%257) % 257==1):
            return i

s1  = 29
s2  = 19 
s3  = 57
s4  = 62
s5  = 149
s21 = 230
s31 = 248
s41 = 228

l01 = (s3*s21-s4*s31)%257
m01 = (modinv(s1*s21-s2*s31))%257
n01 = (s3*s21-s5*s41)%257
o01 = (modinv(s1*s21-s3*s41))%257
p01 = s21-s31
q01 = modinv(s1*s21-s2*s31)
r01 = s21-s41
s01 = modinv(s1*s21-s3*s41)
t01 = modinv(p01*q01)
u01 = r01*s01
v01 = t01-u01
w01 = ((l01*m01)-(n01*o01))*v01
c   = w01%257 #12

l02 = (s3*s21-s4*s31)%257
m02 = (modinv(s1*s21-s2*s31))%257
o02 = (s21-s31)%257
p02 = (modinv(s1*s21-s2*s31))%257
q02 = l02*m02
r02 = o02*p02
s02 = c*r02
t02 = (q02-s02)%257
b = t02


l3 = (s3*s21)%257
m3 = b*(s1*s21)%257
n3 = c*(s21)%257
a = (l3-m3-n3)%257

print("c:",c)
print("b:",b)
print("a:",a)

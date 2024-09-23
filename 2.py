import math
x=17.421
y=10.365 * 10**(-3)
z=0.828 * 10**(5)
a=(y + (x - 1)**(1/3))**(1/4)
b=abs(x - y) * ((math.sin(z)**2) + math.tan(z))
s=a/b
print(float("{0:.6f}".format(s)))

#No 1
n=int(input("Enter year of birth"))
m=2024-n
print(f"You are {m} years old")


#No 2
A=int(input("Enter a no:"))
B=float(input("Enter another no:"))
sum=A+B
product=A*B
print(f"the sum and product of {A} , {B} is {A+B},{A*B}")


#No 3
n=float(input("Enter a number whose square is to be got:"))
print(f"The square of {n} is {n**2} ")


#No 4
L=float(input("Enter lenghth of the rectangle"))
B=float(input("Enter breadth of the rectangle"))
print(f"The perimeter and area of the rectangle are {2*(L+B)} , {L*B}")


#No 5
n=float(input("Enter a celcius value:"))
F=(1.8*n)+32
print(f"{n} in degrees celcius is {F}")


#No 6
n=float(input("Enter radius"))
p=3.14
print(f"The diameter is {2*n}\nThe circumference is {p*2*n}\nThe area is {p*n**2}")


#No 7
a=float(input("side one:"))
b=float(input("side two:"))
c=(a**2+b**2)**.5
print(f"a triangle of sides {a},{b} has hypotenuse of {c}")


#No 8
n=float(input("Enter price:"))
v=.1722
print(f"The price with vat added is {n+(n*v)}")


#No 9
i=float(input("Input intial speed"))
f=float(input("Input final speed"))
l=10.0
speed_per_litre=(f-i)/l
print(f"speed per litre is {speed_per_litre}")


#No 10
m_1=float(input("Input first mass"))
m_2=float(input("Input second mass"))
r=float(input("Input Radius"))
G=(6.7*10**-11*m_1*m_2)/r**2
print(f"the gravitational force is {G} ")


#No 11
p=43000000.0
m=0.123
y_1=p+(p*m)
y_2=y_1+(y_1*m)
y_3=y_2+(y_2*m)
print(f"The population grows as:\n 2025={y_1}\n2026={y_2}\n2027={y_3}")


#No 12
x=5
N=(x**4-x**3+x**2-x)/((x+1)**2-x**.5)
print(f"Answer is {N}")


#No 13
x2=float(input("Input x2:"))
x1=float(input("Input x1:"))
y2=float(input("Input y2:"))
y1=float(input("Input y1:"))
d=((x2-x1)**2+(y2-y1)**2)**.5
print(f"The distance between these points is {d}")


#No 14
s=int(input("Enter the seconds:"))
h=s//3600
m=(s%3600)//60
remaining_seconds=s%60
print(f"{s} seconds is {h} hours {m} minutes {remaining_seconds} seconds")


#No 15
x2=float(input("Enter integer:"))
x1=float(input("Enter integer:"))
y2=float(input("Enter integer:"))
y1=float(input("Enter integer:"))
G=(y2-y1)/(x2-x1)
print(f"The gradient is {G}")

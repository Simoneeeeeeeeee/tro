#dichiaro le variabili e stampo
x = 5
y = "John"
print(x)
print(y)
#attribuisco alla variabile il type
z=int(3)
print(type(x)) #stampo il tipo di variabile
print(z)
#le variabili devono iniziare con una lettera o minuscola
# assegno adiverse variabili dei valori
g,h,l ="giovanni", "esseba","gino"
print(g)
print(h)
print(l)
#assegno apiu variabili stesso nome
r=t=o = "fino"
print(r)
print(t)
print(o)
#assegno a ogni valore di una lista una variabile e la stampo
capello = ["biondo","moro","rosso"]
q,a,z = capello
print(q)
print(a)
print(z)
#creare una variabile fuori da una funzione e usarla dentro la funzione
m = "awesome"

def myfunc():
  print("Python is " + m)

myfunc()
#scrivo due variabili diverse una dentro la funzione una no
p = "bello"

def myfunc():
  p = "fantastico"
  print("Anas è " + p)

myfunc()

print("anas è " + p)
#il comando global rene una variabile all'interno di una variabile global
def myfunc():
  global m
  m = "rotto"

myfunc()

print("simone è " + m)
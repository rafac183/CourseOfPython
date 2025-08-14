frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)
    
i = 0
while i != 5:
    i += 1
    print(i)
    
a = 0
while True:
    print(a)
    a += 1
    
    if a > 6:

        break

""" 
range(fin)
range(inicio, fin)
range(inicio, fin, intervalo?) """

        
for i in range(10):
    if i % 2 == 0:
        continue
    print(i) 
    
for i in range(5):
    pass
    
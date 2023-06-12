import random

senha = []

for i in range(random.randint(2,4)) :
  numeros = random.randrange(9)
  senha.append(numeros)

for i in range(random.randint(1,3)) : 
  maiuscula = chr(random.randint(65,90))
  senha.append(maiuscula)

for i in range(random.randint(2,4)) :
  minuscula = chr(random.randint(97,122))
  senha.append(minuscula)

for i in range(random.randint(0,1)) :
  especial = chr(random.randint(33,47))
  senha.append(especial)
  
for i in range(random.randint(0,1)) :  
  especial2 = chr(random.randint(58,64))
  senha.append(especial2)


random.shuffle(senha)
senha = str(senha) [1:-1]
senha = senha.replace(',','')
senha = senha.replace("'",'')
senha = senha.replace(' ','')
print(" Sua nova senha é :", senha)

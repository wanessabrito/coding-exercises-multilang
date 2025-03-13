def maior_numero(a,b,c):
    if a > b and a>=c:
        return a 
    elif b > a and b>=c:
        return b 
    else:
        return c 
maior1= maior_numero(10,20,30)
maior2= maior_numero(40,50,60)
maior3= maior_numero(70,80,90)
resposta = maior_numero(30,60,90)
print(resposta)



#variable de control
numero=0

#acumulador
suma=0

#declaro el ciclo
while(numero>=0):
    
    #pedir un numero
    numero=int(input("Digite un numero: "))
    if(numero>=0):
        suma=suma+numero
    else:
        print(f'la suma fue: {suma}')
        break
else:
    print("chao")
print(f'la suma fue: {suma}')
        
        
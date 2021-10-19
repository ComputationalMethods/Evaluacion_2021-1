#!/usr/bin/env python3

def  binario(numero):

    lista=[]
    binario = []
    
    numero2 = numero 

    #Comienza la parte que convierte de entero a Binario
    while numero2 != 0:
        modulo = numero2 % 2
        binario.append(modulo)
        numero2= numero2 // 2
                
     #Finaliza la conversión de entero a Binario   
        

    lista = binario[::-1]
    

    #Comienza el código que agrega los ceros al inicio
    
    cantidad = int(len(lista))
 
    adicion=0

    while cantidad < 8:
        cantidad += 1
        binario.append(adicion)

     #Finaliza el código que agrega los ceros al inicio
     
     
    lista = binario[::-1]
    

    cadena = ''.join([str(_) for _ in lista])

    

    return cadena 

    



if __name__=='__main__':

    print("\n\n")
    print( __name__)
    
    n= int(input("\n\nIngrese el numero : "))
    a = binario(n)


    print("\n\n%d convertido a binario es :"%(n))
    print("\n")
    print(a)
    print("\n")
      
    

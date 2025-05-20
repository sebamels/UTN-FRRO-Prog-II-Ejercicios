"""
O(n)=2*n

"""

if __name__ == '__main__':
    palabra: str = input("> Ingrese una frase: ")
    
    palabra = palabra.lower().replace(" ", "")
    
    palabra_auxiliar: str = ""
    
    contador_vocales: int = 0

    for caracter in palabra:
        if caracter.isalpha() and caracter not in '1234567890':
            palabra_auxiliar += caracter
    
    for caracter in palabra_auxiliar:
        if caracter in 'aeiou':
            contador_vocales += 1
        
    print(f"Cantidad de vocales: {contador_vocales}")
    print(f"Cantidad de consonantes: {len(palabra_auxiliar) - contador_vocales}")     
    



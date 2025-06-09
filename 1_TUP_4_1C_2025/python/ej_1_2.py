if __name__ == '__main__':
    palabra: str = input("> Ingrese una frase: ").lower().replace(" ", "")
    
    contador_vocales = len([caracter for caracter in palabra \
        if caracter in 'aeiou'])
    
    print(f"Cantidad de vocales: {contador_vocales}")
    print(f"Cantidad de consonantes: {len(palabra) - contador_vocales}")     
    

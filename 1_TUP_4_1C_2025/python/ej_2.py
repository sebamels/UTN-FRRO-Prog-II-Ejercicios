if __name__ == '__main__':
    palabra: str = input("> Ingrese una frase: ")
    
    palabra_invertida: str = ""
    
    idx: int = len(palabra) - 1
    
    while idx >= 0:
        palabra_invertida += palabra[idx]
        
        idx -= 1
        
    print(f"Palabra: {palabra}")
    print(f"Palabra invertida: {palabra_invertida}")
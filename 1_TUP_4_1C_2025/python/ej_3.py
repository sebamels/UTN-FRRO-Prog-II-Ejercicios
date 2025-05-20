if __name__ == "__main__":
    frase: str = input("> Ingrese una frase: ")
    numero: int = int(input("> Ingrese un numero: "))
    
    print([palabra for palabra in frase.split(" ")\
        if len(palabra) >= numero])
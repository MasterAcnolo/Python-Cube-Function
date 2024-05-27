def cube(nombre):
   
    return nombre ** 3 # <- Change this value if you want to change exponent

def main():
   
    try:
        nombre = float(input("Entrez un nombre : "))
      
        resultat = cube(nombre)
        
        print(f"Le cube de {nombre} est : {resultat}")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    main()
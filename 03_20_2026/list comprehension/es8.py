#dict comprehension: data una stringa conta quante volte compare ogni parola

if __name__ == "__main__":
    
    
    word = input("Inserisci una frase: ")
    
    list = word.replace(",", " ").replace(";", " ").replace(".", " ").replace("?", " ").replace("!", " ").replace("\n", " ").split(" ")
    
    res = {n: list.count(n) for n in list }
    
    print(f"Word: {word}")
    print(f"List: {list}")
    
    print(f"Res: {res}")

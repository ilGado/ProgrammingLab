#data una lista di numeri, usa una list comprehension per ritornare i numeri dispari

import randomList as rl

if __name__ == "__main__":
    
    list = rl.getRandomList()
    
    odds = [n for n in list if n % 2 != 0]
    
    print(f"Original: {list}")
    print(f"Odds: {odds}")
    
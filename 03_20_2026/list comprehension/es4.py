#trova le terne pitagoriche da 1 a 20 con una list comprehension


if __name__ == "__main__":
    
    res = [(a,b,c) for a in range (1, 21) for b in range (1,21) for c in range (1,21) if a**2 + b**2 == c**2 and a <= b]
    
    print(f"Res: {res}")
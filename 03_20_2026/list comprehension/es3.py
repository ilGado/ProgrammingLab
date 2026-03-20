import randomList as rl


if __name__ == "__main__":
    
    list1 = rl.getRandomList(3, 6)
    list2 = rl.getRandomList(3)
    
    res = [x * y for x in list1 for y in list2 if x * y > 10]
    
    print(f"First list: {list1}")
    print(f"Second list: {list2}")
    print(f"Res: {res}")
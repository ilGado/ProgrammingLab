#lista di liste deve diventare una lista unica

import randomList as rl

if __name__ == "__main__":
    
    list = [rl.getRandomList(), rl.getRandomList(), rl.getRandomList()]

    
    res = [n for l in list for n in l]
    
    print(f"Original: {list}")
    print(f"Res: {res}")
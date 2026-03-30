import MovingAverage as ma

if __name__ == "__main__":
    
    x = [2,4,8,16]
    movAv = ma.MovingAverage(2)
    
    res = movAv.computate(x)
    print(res)
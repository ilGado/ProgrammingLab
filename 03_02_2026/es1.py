#Scrivere una funzione che sommi tutti gli elementi di una lista
import randomArray

def getSum(list):
    
    sum = 0
    
    for number in list:
        sum += number
        
    return sum



list = randomArray.getRandomList()
sum = getSum(list)

print(f"List: {list}")
print(f"Sum: {sum}")

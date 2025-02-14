numbers = [3 , 12 , 6 , 15 ,10]
even = []
for number in numbers :
    if number % 2 == 0:
        even.append(number)
       
even.sort()        
print(even)
    
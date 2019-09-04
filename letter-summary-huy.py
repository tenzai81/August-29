word = input()
y = dict()
for x in word:
    if x not in y :
         y[x] = 1  
    else:
         y[x] = y[x]+1   
print(y)
numbers = ['Mahmoud', 'Ahmed', 'Mohamed', 'Ziad', 'Aly', 'Magda', 'Aly']
numbers2 = []
i=0
#print(len(numbers))
while i<len(numbers):
    name = numbers[i]
    if name not in numbers2:
        numbers2.append(name)
    i+=1
print(numbers2)
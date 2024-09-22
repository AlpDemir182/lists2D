fruits = [["peach","apple","pear"],["banana","pineapple","mango"],["dragonfruit","orange","grapes"]]
print(fruits)
for i in fruits:
    print(i)
for i in range(0,len(fruits)):
    for j in range(0,len(fruits[0])):
        print(fruits[i][j], end = " ")
    print()

numbers = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(0, len(numbers)):
    for j in range(0, len(numbers[0])):
        print(numbers [i][j], end = " ")
    print()

print(fruits[0][1])
print(fruits[2][2])

fruits[0][1] = "kiwi"
print(fruits)
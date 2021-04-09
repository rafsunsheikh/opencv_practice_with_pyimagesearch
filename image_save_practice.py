file = open('number.txt', 'r')
number = int(file.read())
print(number)
file.close()

number = 100
file2 = open('number.txt', 'w')
file2.write(str(number))
file2.close()
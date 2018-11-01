def LCM_of_Three_LCM(numbers):
    numbers.sort()
    worstcase = numbers[0] * numbers[1] * numbers[2]
    for i in range (numbers[2], worstcase + 1, numbers[2]):
        if((i % numbers[0] == 0)  and (i % numbers[1] == 0)):
            return i

#numbers = [3, 2, 16]
numbers = []  # create empty list

first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
third_num = int(input('Enter third number: '))

numbers.append(first_num)
numbers.append(second_num)
numbers.append(third_num)
print (str(LCM_of_Three_LCM(numbers)))
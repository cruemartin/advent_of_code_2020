
expenses = []

f = open("day_1\expense_report.txt", "r")

for line in f:
    expenses.append(int(line.strip())) 

f.close()

num_1_index = -1
num_2_index = -1

for x in range(0, len(expenses)):
    temp =  2020 - expenses[x]

    if temp in expenses:
        num_1_index = x
        num_2_index =  expenses.index(temp)

answer = expenses[num_1_index] * expenses[num_2_index]

print("1. Answer = ", answer)


#Prolly can be inproved but I'm lazy

for x in expenses:
    for y in expenses:
        for z in expenses:
            if x + y + z == 2020:
                answer = x * y * z

print("2. Answer = ", answer)
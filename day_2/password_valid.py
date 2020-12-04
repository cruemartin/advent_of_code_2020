passwords = []

f = open('day_2\password_info.txt','r')

for line in f:
    temp = line.strip().split(" ")

    occurrence = temp[0].split("-")
    letter =  temp[1].strip(":")
    password = temp[2].strip()

    passwords.append({'occurrence' : occurrence, 'letter': letter, 'password': password, 'length': len(password)})


f.close()

#
#
#part 1
#
#
#print(passwords)

valid_count= 0

for x in passwords:
    count = x['password'].count(x['letter'])

    if count >= int(x['occurrence'][0]) and count <= int(x['occurrence'][1]):
        valid_count += 1


print("1. Valid passwords = ", valid_count)


#
#
#Part 2
#
#
count = 0

for x in passwords:

    #if the larger of the index is less then the length of the password string
    if x['length'] >= int(x['occurrence'][1]):
        if x['password'][int(x['occurrence'][0])-1] == x['letter'] and x['password'][int(x['occurrence'][1])-1] != x['letter']:
            count += 1
        elif x['password'][int(x['occurrence'][0])-1] != x['letter'] and x['password'][int(x['occurrence'][1])-1] == x['letter']:
            count += 1

    # if the larger of the index is greater than the length of the password string      
    else:
        if x['password'][int(x['occurrence'][0])-1] == x['letter']:
            count += 1 

print("2. Valid passwords  = ", count)






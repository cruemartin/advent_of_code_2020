import re

class Passport:
    def __init__(self, birth_year = None, issue_year = None, experation_year = None, height = None, hair_color = None, eye_color = None, passport_id = None, country_id = None):
        self.birth_year = birth_year
        self.issue_year = issue_year
        self.experation_year = experation_year
        self.height = height
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.passport_id =  passport_id
        self.country_id = country_id

    def is_valid(self):
        valid = True
        if self.birth_year is None: 
            valid = False
        elif self.issue_year is None:
            valid = False
        elif self.experation_year is None:
            valid = False
        elif self.height is None:
            valid = False
        elif self.hair_color is None:
            valid = False
        elif self.eye_color is None:
            valid = False
        elif self.passport_id is None:
            valid = False
        return valid

    def is_valid_part_2(self):

        if self.is_valid() is False:
            return False
        #years    
        # if len(self.birth_year) != 4 or len(self.issue_year) != 4 or len(self.experation_year) != 4:
        #     return False
        if len(self.birth_year) != 4:
            # print(self.birth_year)
            return False
        if len(self.issue_year) != 4:
            # print(self.issue_year)
            return False
        if len(self.experation_year) != 4:
            # print(self.experation_year)
            return False
        if (int(self.birth_year) >= 1920 and int(self.birth_year) <= 2002) is False:
            # print(self.birth_year)
            return False
        if (int(self.issue_year) >= 2010 and int(self.issue_year) <= 2020) is False:
            # print(self.issue_year)
            return False
        if (int(self.experation_year) >= 2020 and int(self.experation_year) <= 2030) is False:
            # print(self.experation_year)
            return False
        
        # #height
        match = re.search(r'((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)',self.height)
        # print(match)
        if not match:
            # print(self.height)
            return False
        # #hair color
        match = re.search(r'^#([0-9]|[a-f]){6}', self.hair_color) 
        if not match:
            # print(self.hair_color)
            return False
        # #eye color
        match = re.search(r'(amb|blu|brn|gry|grn|hzl|oth)', self.eye_color)
        if not match:
            # print(self.eye_color)
            return False
        # #pid
        match = re.search(r'\d{9}', self.passport_id) 
        if not match:
            print(self.passport_id)
            return False
        
        return True

#Read in data
passport_data = []
passport_data.append(Passport())
index = 0

f = open('day_4\passport_data.txt','r')

for line in f:
    
    if line[0] == '\n':
        passport_data.append(Passport())
        index += 1   
        continue
  
    line_elements = line.strip().split(' ')

    for elements in line_elements:
        temp =  elements.strip().split(':')

        if temp[0] == 'byr':
            passport_data[index].birth_year =  temp[1]
        elif temp[0] == 'iyr':
            passport_data[index].issue_year =  temp[1]   
        elif temp[0] == 'eyr':
            passport_data[index].experation_year =  temp[1]
        elif temp[0] == 'hgt':
            passport_data[index].height =  temp[1]
        elif temp[0] == 'hcl':
            passport_data[index].hair_color =  temp[1]
        elif temp[0] == 'ecl':
            passport_data[index].eye_color =  temp[1]
        elif temp[0] == 'pid':
            passport_data[index].passport_id =  temp[1]
        elif temp[0] == 'cid':
            passport_data[index].country_id =  temp[1]

count = 0

#part 1

for x in passport_data:
    if x.is_valid():
        count += 1

print('1. Number of valid passports = ', count)

#part 2

count = 0

for x in passport_data:
    if x.is_valid_part_2():
        count += 1

print('2. Number of valid passports = ', count)
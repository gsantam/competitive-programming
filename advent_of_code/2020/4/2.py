import re
lines = open("input.txt").readlines()
passport = {}
n_valid = 0

def is_valid(passport):
    try:
        if int(passport["byr"]) <1920 or int(passport["byr"])>2002:
            return False
        if int(passport["iyr"]) <2010 or int(passport["iyr"])>2020:
            return False
        if int(passport["eyr"]) <2020 or int(passport["eyr"])>2030:
            return False
        if passport["hgt"][-2:]=="cm":
            if int(passport["hgt"][:-2]) <150 or int(passport["hgt"][:-2])>193:
                return False
        elif passport["hgt"][-2:]=="in":
            if int(passport["hgt"][:-2]) <59 or int(passport["hgt"][:-2])>76:
                return False
        else:
            return False
        if re.match("^[\#][0-9a-f]{6}$",passport["hcl"]) is None:
            return False
        if passport["ecl"] not in ["amb","blu","brn", "gry", "grn", "hzl", "oth"]:
            return False
        if re.match("^[0-9]{9}$",passport["pid"]) is None:
            return False
        return True
    except:
        return False
        
    
for line in lines:
    if line == "\n":
        if is_valid(passport):
            n_valid+=1
        passport = {}
    else:
        line = line.strip().split(" ")
        passport = {**{i.split(":")[0]:i.split(":")[1] for i in line},**passport}
        
if is_valid(passport):
    n_valid+=1
    
print(n_valid)

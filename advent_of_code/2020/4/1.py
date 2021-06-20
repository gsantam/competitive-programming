lines = open("input.txt").readlines()
passport = {}
n_valid = 0
required_fields = set(["byr","iyr","eyr","hgt","hcl","ecl","pid"])
for line in lines:
    if line == "\n":
        if len(required_fields&passport.keys())>=len(required_fields):
            n_valid+=1
        passport = {}
    else:
        line = line.strip().split(" ")
        passport = {**{i.split(":")[0]:i.split(":")[1] for i in line},**passport}
if len(required_fields&passport.keys())>=len(required_fields):
    n_valid+=1
    
print(n_valid)

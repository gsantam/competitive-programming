mass = open("input.txt","r").read().split("\n")

def get_total_fuel(fuel):
    total_fuel = -fuel
    while fuel>0:
        total_fuel+=fuel
        fuel = int(fuel / 3)- 2
    return total_fuel


print(sum([get_total_fuel(int(x)) for x in mass if x !='']))

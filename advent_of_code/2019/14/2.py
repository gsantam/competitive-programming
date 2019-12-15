formulas = open("input.txt").read().strip("\n").split("\n")
def total_ore_for_n_fuel(n_fuel):
    import math

    formula_dict = dict()
    remaining = {"ORE":0}
    used = {"ORE":0}

    for formula in formulas:
        formula = formula.split(" => ")
        result = formula[1].split(" ")
        if result[1] not in formula_dict:
            formula_dict[result[1]] = {}
            formula_dict[result[1]]["output"] = int(result[0])
            remaining[result[1]] = 0
            used[result[1]] = 0
            for element in formula[0].split(","):
                element =element.strip().split(" ")
                formula_dict[result[1]][element[1]] = int(element[0])

    formula_dict["ORE"] = {"output":1}
    needed = {"FUEL":n_fuel}
    total_ore = 0

    while len(needed)>0:
        first_key = list(needed.keys())[0]
        if remaining[first_key]>=needed[first_key]:
            remaining[first_key]-=needed[first_key]
            del needed[first_key]
        else:
            if first_key=="ORE":
                total_ore+=needed[first_key]

            need_minus_remaining = (needed[first_key]-remaining[first_key])
            total_times = math.ceil(need_minus_remaining / formula_dict[first_key]["output"])
            for element in formula_dict[first_key]:
                if element =="output":
                    remaining[first_key]  += formula_dict[first_key]["output"]*total_times
                else:
                    if element not in needed:
                        needed[element] = 0
                    needed[element]+=formula_dict[first_key][element]*total_times
    return total_ore
    

ore = 10**12
def binary_search_on_fuel(l,r):
    mid = (r+l)//2
    if (l + 1) == r:
        return l


    mid_ore = total_ore_for_n_fuel(mid)

    if mid_ore>ore:
        return binary_search_on_fuel(l,mid)
    else:
        return binary_search_on_fuel(mid,r)

print(binary_search_on_fuel(l = 1,r = 10**12))

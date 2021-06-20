def run_ins(inss):
    seen = set()
    i = 0
    acc = 0
    while i not in seen and i<len(inss):
        ins = inss[i]
        seen.add(i)
        if ins[0] == "acc":
            acc+=int(ins[1])
            i+=1
        if ins[0]=="jmp":
            i+=int(ins[1])
        if ins[0]=="nop":
            i+=1
    end = False
    if i >= len(inss):
        end = True
    return acc,end

inss= [x.strip().split(" ") for x in open("input.txt").readlines()]
print(run_ins(inss)[0])

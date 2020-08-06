def rotLeft(a, d):
    assert type(a) == list
    assert type(d) == int
    if len(a) == 0: 
        return a
    
    return [a[(i+d)%len(a)] for i in range(len(a))]

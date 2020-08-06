def is_colourful(number):
    seen_numbers = set()
    number_str = str(number)
    
    for i,digit_str in enumerate(number_str):
        product = 1
        for j in range(i,len(number_str)):
            product=int(number_str[j]) * product
            if not (i==0 and j == len(number_str)-1):
                if product in seen_numbers:
                    return False
                seen_numbers.add(product)
    return True


print(is_colourful(3245))

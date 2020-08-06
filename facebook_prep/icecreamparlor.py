def icecreamParlor(m, arr):
    seen_prices = dict()
    for i,flavour_price in enumerate(arr):
        if (m-flavour_price) in seen_prices:
            return [arr[m-flavour_price][0],i+1]
        
        if flavour_price not in seen_prices:
            seen_prices[flavour_price] = []
        seen_prices[flavour_price].append(i+1)

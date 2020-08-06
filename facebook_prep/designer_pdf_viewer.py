def designerPdfViewer(h,w):
    assert type(h) == list
    assert type(w) == str
    
    letter_dict_height = {}
    for i,height in enumerate(h):
        letter = chr(ord("a") + i)
        letter_dict_height[letter] = int(height)
    max_height = -1
    for letter in w:
        assert letter in letter_dict_height
        max_height = max(max_height,letter_dict_height[letter])
    return max_height*len(w)



        



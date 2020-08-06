
def merge_ordered_arrays(array1,array2):
    j = 0
    k = 0
    final_length = len(array1) + len(array2)
    ordered_array = []
    while j + k < final_length:
        if j<len(array1):
            if k<len(array2) and array2[k]<=array1[j]:
                ordered_array.append(array2[k])
                k+=1
            else:
                ordered_array.append(array1[j])
                j+=1                
        else:
            ordered_array.append(array2[k])
            k+=1
    return ordered_array


def merge_sort(array):
    if len(array)==1:
        return array
    
    left_array = merge_sort(array[0:len(array)//2])
    right_array = merge_sort(array[len(array)//2:])
    
    return merge_ordered_arrays(left_array,right_array)

print(merge_sort([3,4,1,3,6,7,9,3,1,2,9,10]))

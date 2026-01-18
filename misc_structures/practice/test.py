def binary_search(arr,target):
    i = 0
    j = len(arr)-1
    while True:
        if j<i:
            return None
        mid = (i+j)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            i = mid + 1
        else:
            j = mid - 1

def binary_search_closest(arr,target):
    i = 0
    j = len(arr)-1
    while True:
        if j<i:
            if j>=0 and abs(arr[j]-target)<=abs(arr[i]-target):
                return j
            return i
        mid = (i+j)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            i = mid + 1
        else:
            j = mid - 1 


if __name__ == "__main__":
    print(binary_search_closest([1,5],-1))
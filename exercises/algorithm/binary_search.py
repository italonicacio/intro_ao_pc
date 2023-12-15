

def binary_search(arr, value):

    max_ = len(arr) - 1
    min_ = 0
    

    while(True):

        mean = (max_+min_)//2

        if arr[mean] == value:
            break

        if min_ >= max_:
            return False

        if arr[mean] > value:
            max_ = mean-1
        
        if arr[mean] < value:
            min_ = mean + 1



    return True

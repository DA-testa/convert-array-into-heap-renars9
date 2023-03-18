# python3
def swapping(data,n,i):
    swaps = []
    min = i  
    left = 2 * i + 1  
    right = 2 * i + 2 

    if left < n and data[left] < data[min]:
        min = left

    if right < n and data[right] < data[min]:
        min = right

    if min != i:
        data[i], data[min] = data[min], data[i]
        swaps.append((i, min))
        sub_swaps = swapping(data, n, min)
        swaps.extend(sub_swaps)

    return swaps

def build_heap(arr, n):
   
    swaps = []
    for i in range(n // 2 - 1, -1, -1):
        sub_indices = swapping(arr, n, i)
        swaps.extend(sub_indices)

    return swaps


def main():
    
    filename = "test/"
    check = input()
    if( 'I' in check):
        n = int(input())
        data = list(map(int, input().split()))

    elif('F' in check):
        filename = filename + input()

        if('a' in filename[-1]):
            print("invalid filename")
            return
        
        with open(filename) as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data,n)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()


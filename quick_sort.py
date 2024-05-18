def quick_sort(num:list, start:int=0, end:int|None=None) -> list:
    if end is None:
        end = len(num) - 1
        num = list(num)

    if start < end:
        pivot = partition(num, start, end)
        quick_sort(num, start=pivot+1, end=end)
        quick_sort(num, start=start, end=pivot-1)

    return num

def partition(num:list, start:int=0, end:int|None=None) -> int:
    if end is None:
        end = len(num) - 1

    l, r = start, end - 1

    while l < r:
        if num[l] <= num[end]:
            l+=1
        elif num[r] > num[end]:
            r-=1
        else:
            num[l], num[r] = num[r], num[l]

    if num[l] > num[end]:
        num[l], num[end] = num[end], num[l]
        return l
    return end


if __name__ == "__main__":
    lst = [4,6,2,1,9,3,7,4,0,8,4,1,7,4,8]
    print(quick_sort(lst)==sorted(lst))
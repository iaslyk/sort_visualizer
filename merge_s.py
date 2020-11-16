def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def merge_sort(nums, left, right):
    if(right <= left):
        return
    elif(left < right):
        mid = (left + right)//2
        yield from merge_sort(nums, left, mid)
        yield from merge_sort(nums, mid+1, right)
        yield from merge(nums, left, mid, right)
        yield nums


def merge(nums, left, mid, right):
    new = []
    i = left
    j = mid+1
    while(i <= mid and j <= right):
        if(nums[i] < nums[j]):
            new.append(nums[i])
            i += 1
        else:
            new.append(nums[j])
            j += 1
    if(i > mid):
        while(j <= right):
            new.append(nums[j])
            j += 1
    else:
        while(i <= mid):
            new.append(nums[i])
            i += 1
    for i, val in enumerate(new):
        nums[left+i] = val
        yield nums

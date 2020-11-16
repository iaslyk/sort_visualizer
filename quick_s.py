def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def quick_sort(nums, lo, hi):
    if(lo >= hi):
        return
    # pivot
    piv = nums[hi]
    pivindx = lo
    for i in range(lo, hi):
        if(nums[i] < piv):
            swap(nums, i, pivindx)
            pivindx += 1
        yield nums
    swap(nums, hi, pivindx)
    yield nums

    yield from quick_sort(nums, lo, pivindx-1)
    yield from quick_sort(nums, pivindx+1, hi)

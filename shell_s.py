def shell_sort(nums):
    sub_list_count = len(nums)//2
    while sub_list_count > 0:
        for start_position in range(sub_list_count):
            gap_insertion_sort(nums, start_position, sub_list_count)
            yield nums
        sub_list_count = sub_list_count // 2


def gap_insertion_sort(nlist, start, gap):
    for i in range(start + gap, len(nlist), gap):
        current_value = nlist[i]
        position = i
        while position >= gap and nlist[position-gap] > current_value:
            nlist[position] = nlist[position-gap]
            position = position-gap

        nlist[position] = current_value

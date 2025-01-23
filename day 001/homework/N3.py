def finding_max_in_arr(arr):
    maximum = arr[0]
    if arr[1] > maximum:
        maximum = arr[1]
    if arr[2] > maximum:
        maximum = arr[2]
    if arr[3] > maximum:
        maximum = arr[3]
    if arr[4] > maximum:
        maximum = arr[4]
    return maximum
arr = [56,19,18,977,2777]
print(finding_max_in_arr(arr))
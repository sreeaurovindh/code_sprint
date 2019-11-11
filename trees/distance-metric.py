from collections import defaultdict
def getDistanceMetrics(arr):

    if len(arr) == 0:
        return arr
    if len(arr) == 1:
        return [0]

    final_array = [0]*len(arr)
    val_idx_dict = defaultdict(list)

    for idx,value in enumerate(arr):
        if value in val_idx_dict:
            val_idx_dict[value].append(idx)
        else:
            val_idx_dict[value] = [idx]

    for value, idx_list in val_idx_dict.items():
        total_idx_list = len(idx_list)
        total_sum = sum(idx_list)
        if total_idx_list == 1:
            final_array[idx_list[0]] = 0
            continue
        else:
            for idx,idx_val in enumerate(idx_list):
                final_array[idx_val] = abs(idx_val * (total_idx_list -1) - (total_sum - idx_val))

    print(final_array)
    return final_array


getDistanceMetrics([1,2,1,1,2,3])
getDistanceMetrics([1,2,2,1,5,1])
def count_positives_sum_negatives(arr):
    positiveNums = 0;
    negativeNums = 0;
    if arr == [] or len(arr) == 0:
        return [];
    else:
        for num in arr:
            if num > 0:
                positiveNums += 1
            else:
                negativeNums += num

    return [positiveNums , negativeNums];
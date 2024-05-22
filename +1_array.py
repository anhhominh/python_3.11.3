def up_array(arr):
    arr.reverse()
    ans = []
    tmp = 0
    if arr == []:
        return None
    for i in range(0,len(arr)):
        if arr[i] < 0 or arr[i] >= 10:
            return None
        else:
            print(tmp)
            if i == 0:
                arr[i] = arr[i] + 1
            arr[i] = arr[i] + tmp
            tmp = 0
            if arr[i] >= 10:
                tmp = tmp + int(str(arr[i])[0])
                arr[i] = (arr[i] % 10) 
            else:
                tmp = 0
            ans.append(arr[i])
    if tmp != 0 :
        ans.append(tmp)
    ans.reverse()
    return ans
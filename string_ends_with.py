def solution(text, ending):
    end = ''
    for i in range(len(text) - 1,len(text) - len(ending) - 1, -1):
        end = end + text[i]
    print(end)
    end = end[::-1]
    return end == ending
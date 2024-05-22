def custom_key(elems):
    return -len(elems), elems.lower()

def mix(s1, s2):
    s1 = sorted(s1.replace(' ', '').replace(',', '').replace("'", ''))
    s2 = sorted(s2.replace(' ', '').replace(',', '').replace("'", ''))
    s1set = set(s1)
    s2set = set(s2)
    unionset = s1set.union(s2set)
    lst = list()
    for letter in unionset:
        if letter.isalpha() and bool(letter.islower()) == True:
            if s1.count(letter) > 1 or s2.count(letter) > 1:
                if s1.count(letter) > s2.count(letter):
                    lst.append('1:'+str(letter*s1.count(letter)))
                elif s1.count(letter) < s2.count(letter):
                    lst.append('2:'+str(letter*s2.count(letter)))
                elif s1.count(letter) == s2.count(letter):
                    lst.append('=:'+str(letter*s1.count(letter)))
    lst = sorted(lst, key=custom_key)
    return '/'.join(lst)

# Cách khác
# def mix(s1, s2):
#     hist = {}
#     for ch in "abcdefghijklmnopqrstuvwxyz":
#         val1, val2 = s1.count(ch), s2.count(ch)
#         if max(val1, val2) > 1:
#             which = "1" if val1 > val2 else "2" if val2 > val1 else "="
#             hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
#     return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))
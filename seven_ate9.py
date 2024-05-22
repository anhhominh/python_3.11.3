def seven_ate9(str_):
    ans = ""
    for i in range(0,len(str_)):
        try:
            if(i != len(str_) - 1  and str_[i] == '9' and str_[i - 1] == '7' and str_[i+1] == '7'):
                continue
            else:
                print(i)
                ans = ans + str_[i]
        except Exception as e:
            print(str(e))
    return ans


# def seven_ate9(str_):
#    while str_.find('797') != -1:
#        str_ = str_.replace('797','77')
#    return str_
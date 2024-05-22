def last(x):
    x_list = (x.split(' '))
    x_list.sort(key=lambda x:x[-1])
    return x_list
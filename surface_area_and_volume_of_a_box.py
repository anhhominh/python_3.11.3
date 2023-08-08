def get_size(w,h,d):
    total_area = w*h*2 + w*d*2 + h*d*2
    volume = w * h * d
    return [total_area,volume]
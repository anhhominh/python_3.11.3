def remove_url_anchor(url):
    ans = ""
    for i in url:
        if( i == '#'):
            break;
        else:
            ans = ans + i
    return ans
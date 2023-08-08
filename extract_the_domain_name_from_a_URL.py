def domain_name(url):
    ans = url.replace('http://','').replace('https://','').replace('www.','')
    str = ans.split('.')
    return str[0]
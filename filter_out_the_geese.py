geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    for i in range(0,len(geese)):
        for item in birds:
            if geese[i] == item:
                birds.remove(item)
    return birds
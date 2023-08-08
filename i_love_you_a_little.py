def how_much_i_love_you(nb_petals):
    str = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
    if nb_petals <= 6:
        return str[nb_petals - 1]
    if nb_petals > 6:
        return str[nb_petals % 6 - 1]
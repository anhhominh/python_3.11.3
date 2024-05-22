def uefa_euro_2016(teams, scores):
    teamA = teams[0]
    teamB = teams[1]

    if scores[0] > scores[1]:
        return 'At match ' + teamA + ' - ' + teamB + ', ' + teamA + ' won!'
    elif scores[0] < scores[1]:
        return 'At match ' + teamA + ' - ' + teamB + ', ' + teamB + ' won!'
    elif scores[0] == scores[1]:
        return 'At match ' + teamA + ' - ' + teamB + ', teams played draw.'
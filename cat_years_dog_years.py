def human_years_cat_years_dog_years(human_years):
    catYears = 0
    dogYears = 0
    for i in range (1,human_years+1):
        if i == 1:
            catYears = catYears + 15
            dogYears = dogYears + 15
        
        if i == 2:
            catYears = catYears + 9
            dogYears = dogYears + 9
        
        if i > 2:
            catYears = catYears + 4
            dogYears = dogYears + 5
        
    
    return  [human_years,catYears,dogYears]
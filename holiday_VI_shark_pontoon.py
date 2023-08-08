def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    you = pontoon_distance / you_speed
    if dolphin == True:
        shark = shark_distance / (shark_speed / 2) 
    else:
        shark = shark_distance / shark_speed
    if you < shark:
        return "Alive!"
    return "Shark Bait!"
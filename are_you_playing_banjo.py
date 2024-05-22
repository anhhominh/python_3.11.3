def areYouPlayingBanjo(name):
    return "{} plays banjo".format(name) if name.startswith("R") or name.startswith("r") else "{} does not play banjo".format(name)
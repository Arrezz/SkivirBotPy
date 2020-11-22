commands = []

def handleCommand(arguments):
    """Arguments should come in the form of a list of strings."""
    if len(arguments) > 1:
        return constructMultiQueryURL(argumens[1:])
    elif len(arguments) == 1:
        return constructSingleSummonerURL(arguments[0])
    else:
        return "Need at least one summonername."
        

def constructSingleSummonerURL(name):
    """Takes a summonername and returns its op.gg profile."""
    return "https://euw.op.gg/summoner/userName=" + name.lower()

def constructMultiQueryURL(names):
    """Takes a list of names and creates a multiquery for their
    summonernames."""
    url = "https://euw.op.gg/multi/query="
    for name in names[:-1]:
        url += name.lower() + "%2C"

    return url + names[-1].lower()

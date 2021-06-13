def func4(x):
    OutputList = []
    for a in x:         
        OutputList.append(Sim(a))
    return OutputList
def Sim(tup):
    HelpTup = tup
    while HelpTup[1] != 0:
        HelpTup = (HelpTup[1], HelpTup[0] % HelpTup[1])
    return (int(tup[0]/ HelpTup[0]), int(tup[1]/ HelpTup[0]))    
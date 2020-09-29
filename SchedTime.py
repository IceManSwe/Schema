import SchedParse, array

def getTimes(id, host):
    sched = SchedParse.getSched(id, host)
    timeStampCords = [[]]
    prog = 0

    for item in sched:
        timeStampCords[prog][0] = int(str(item["x"]))
        timeStampCords[prog][1] = int(str(item["y"]))
        prog += 1
    
    print(timeStampCords)

getTimes(200206077753, "it-gymnasiet.skola24.se")
import getSignatureKey, getRenderKey, getSchedule, re, json


def getSched(id, host, week, year, uGuid):

    x = getSchedule.schedule(getRenderKey.renderKey(host), getSignatureKey.key(host, id), uGuid ,week ,host, year)
    print(x)
    if(x["data"]["timetableJson"] != None):
        #x = json.loads(x)
        x = x["data"]["timetableJson"]
        #print(temp["textList"])
        for item in x["textList"]:
            if item["text"] == '':
                print(x)
                x["textList"].remove(item)


        return(x["textList"])
    else :
        print("Error getting shed")
        exit(1)
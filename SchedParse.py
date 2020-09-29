import getSignatureKey, getRenderKey, getSchedule, re, json


def getSched(ID, host):

    x = getSchedule.schedule(getRenderKey.renderKey(), getSignatureKey.key(ID), host)
    #x = json.loads(x)
    x = x["data"]["timetableJson"]

    temp = json.loads(x)
    #print(temp["textList"])
    for item in temp["textList"]:
        if item["text"] == '':
            temp["textList"].remove(item)


    return(temp["textList"])


#print(getSchedule.schedule(getRenderKey.renderKey(), getKey.key(ID), host))
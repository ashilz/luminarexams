




f=open("covidexam","r")

dict = {}
for lines in f:
    data = lines.rstrip("\n").split(",")

    state = data[1]
    cases = data[4]
    recoverd = data[6]
    death = data[5]

    if(state not in dict):
        dict[state] = {"confirmcases":cases,"recoverd":recoverd,"death":death}
    else:
        dict[state] = {"confirmcases": cases, "recoverd": recoverd, "death": death}


#for k,v in dict.items():
#    print(k,",",v)


def Fetchdata(**kwargs):
    for k,v in dict.items():
        if (k == kwargs["state"]):
            print("Total cases:",v["confirmcases"])
        else:
            break




Fetchdata(state="Kerala",parameter="")
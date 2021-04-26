import ZODB
import transaction

class discordItem:
    def __init__(self,name,desc,price,keyword):
        self.name = name
        self.desc = desc
        self.price = price
        self.keyword = keyword
#itemdb = ZODB.DB("itemdb.json")
#itemconn = itemdb.open()

#itroot = itemconn.root()
def inx():
    

    phreakbox = discordItem("The Phreakbox", "A super phreak in a box lol", 100000, "phreakbox")
    pepecrown = discordItem("Pepe Crown", "The antique crown of the Pepe King",1,"pepec")
    itemlist = [pepecrown, phreakbox]
    itemdict = []
    for item in itemlist:
        itemdict.append(item)

    itroot['items'] = itemdict
    transaction.commit()
    print(itroot)
    
def ini():
    for x in itroot['items']:
        itroot[x.keyword]={}

#inx()
#ini()
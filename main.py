import discord
from discord.ext import commands
import pickledb as dbms
from random import randint as rand
import ZODB
import transaction
import objinit
from server import keep_alive

keep_alive()

itemdb = ZODB.DB("itemdb.json")
itemconn = itemdb.open()

print (itemconn.root)

db = dbms.load('playersbal.json', True)
pepec = dbms.load('pepec.json', True)
itroot = itemconn.root()
bot = commands.Bot(command_prefix='#')

transaction.commit()
print(itroot)

for x in itroot['items']:
    itroot[x.keyword]={}

client = discord.Client()
async def getuser(id):
    x = await client.fetch_user(int(id))
    return x
async def respond(message, resmsg, sendmsg):
    if resmsg in message.content.lower():
        await message.channel.send(sendmsg)
async def emb(message,title,desc):
    await message.channel.send(embed=discord.Embed(title=title, description=desc))
async def ownernotif(message):
    owner = await client.fetch_user(642390951008010268)
    await owner.send(message)
@bot.command()
async def checkBal(message, user, name):
    print(db.get(str(user)))
    if (db.get(str(user))==False):
        embedx = discord.Embed(title="Welcome to the Bank, "+str(name), description="Balance is now 500 dollars")
        await message.channel.send(embed=embedx)
        db.set(user, 500)
    else:
        embedx = discord.Embed(title="Balance of user "+ str(name), description="Balance of user is **"+str(db.get(str(user)))+"**")
        await message.channel.send(embed=embedx)
async def earn(message, amount):
    amc = int(db.get(str(message.author.id))) + amount
    db.set(str(message.author.id), amc)
async def flex(message, item):
    try:
        flex = discord.Embed(title=str(message.author)+''+" is flexing their pepe crowns!", description="They have "+str(itroot['pepec'][str(message.author.id)])+" of them, what a loser!")
        await message.channel.send(embed=flex)
        await message.author.dm_channel.send("Dont flex bro")
    except Exception as e:
        await message.channel.send("You dont have the item lol!")
        await ownernotif(str(e))
        print(e)
async def rob(message, u=''):
    if (u==''):
        await message.channel.send(embed=discord.Embed(title="Are ye mad?", description="Mention someone to rob!"))
        pass
    else:
        if (db.get(str(u)) == False):
            await message.channel.send(embed=discord.Embed(title="Sorry ya", description="The members isnt playing money money"))
        else:
            if (rand(1,1000)%2==0):
                xc = int(db.get(str(u)))
                amr = rand(1, xc - 1)
                db.set(str(u), xc - amr)
                db.set(str(message.author.id), (db.get(str(message.author.id))+amr))
                await message.channel.send(embed=discord.Embed(title="Rob success yeah!", description="You looted **" + str(amr) + "**"))
            else:
                await emb(message, "Sorry you were caught", ":(")
async def printItems(message):
    itr = discord.Embed(title="Items (In development))")
    dic = itroot['items']
    for item in dic:
        itr.add_field(name=str(item.name)+" - " +str(item.price),value=item.desc,inline=True)
    await message.channel.send(embed=itr)

async def buyItem(message,item,amount):
    bs = False
    dic = itroot['items']
    for itemxx in dic:
      if(item==itemxx.keyword):
          bs = True
          s = False
          if ((itemxx.price*amount)>db.get(str(message.author.id))):
              await emb(message, "Hey bro! Listen!", "Hey you don have enough balance man")
              pass
          else:
              money = itemxx.price*amount
              try:
                  itroot[itemxx.keyword][str(message.author.id)]
                  a = itroot[itemxx.keyword][str(message.author.id)]
                  amc = a + amount
                  itroot[itemxx.keyword][str(message.author.id)] = amc
                  db.set(str(message.author.id), int((db.get(str(message.author.id)))-money))
                  bs = True
                  s = True
                  itroot._p_changed = 1
                  transaction.commit()
                  await emb(message,"Successful Purchase", "You have successfully bought **"+str(amount)+"** " + str(itemxx.name))
              except Exception as e:
                  itroot[itemxx.keyword][str(message.author.id)] = amount
                  db.set(str(message.author.id), (db.get(str(message.author.id))-money))
                  await emb(message,"Successful Purchase", "You have successfully bought **"+str(amount)+"** " + str(itemxx.name))
                  bs = True
                  s = True
                  itroot._p_changed = 1
                  transaction.commit()
                  
                  await ownernotif(str(e))
          if bs == True:
              break
#        if s == True:
#           await message.channel.send("Successful purchase")
    if (bs == False) :
        await emb(message, "Are ye mad?", "Man that item isnt even in the shop bro")
async def inventory(message):
    emb = discord.Embed(title="Yer Inventory", description="See yourself")
    for item in itroot['items']:
        try:
            na = item.name
            va = itroot[item.keyword][str(message.author.id)]
            desc = "You have **" + str(va) + "** "+ na
            emb.add_field(name=na,value=desc,inline=False)
        except Exception as e:
            await ownernotif(str(e))
            pass

    await message.channel.send(embed=emb)
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await ownernotif("Online! :thumbs_up:")
    print(await getuser(270904126974590976))

@client.event
async def on_message(message):
  
    if message.author == client.user:
        return
bot.run("ODMzOTU1ODk5MzgyMTY5NjMw.YH539A.61zqE2qmwUbHqu_CexHDgfI5_dw", bot="true")

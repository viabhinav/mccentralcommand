    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')
    if '!createserver' in message.content.lower():
        await message.channel.send('Ok, please tell me the name if da server!')
    await respond(message, "hi", "hi")
    await respond(message, "how are you", "We are fine!")
    await respond(message, "xls bal", "bal: inf")
    if (message.content.lower()).startswith("x bal"):
        try:
            userxy = message.content.split()
            userx = userxy[2]
            userx = userx.replace('<', '')
            userx = userx.replace('>','')
            userx=userx.replace('@','')
            userx=userx.replace('!','')
            ux = userx.strip()
            print(ux)
            print(await client.fetch_user(ux))
            await checkBal(message, str(ux), (await client.fetch_user(ux)))
        except Exception as e:
            print(e)
            await checkBal(message, str(message.author.id), str(message.author))
    if message.content.lower()== 'x beg':
        earnamc = rand(100, 1000)
        await message.channel.send(embed=discord.Embed(title="Yo beggar!", description="Yo begged and got **" + str(earnamc) + "**"))
        await earn(message, earnamc)
    await respond(message, "lets fart", "Sorry outta gas now")
    mcx = message.content.lower()
    print(mcx)
    mcs = mcx.split()
    print(mcs)
    if (message.content.lower()).startswith("x rob"):
        x = message.content.split()
        user = x[2].replace('<', '')
        user = user.replace('>','')
        user=user.replace('@','')
        user=user.replace('!','')
        u = user.strip()
        await rob(message, u)
    if message.content.lower()=='x items':
        await printItems(message)
    if message.content.lower() == 'x inv':
        await inventory(message)
    if (message.content.lower()).startswith('x buy'):
        x = message.content.split()
        await buyItem(message, x[2], int(x[3]))
    if message.content.lower() == "x use pepec" :
        await flex(message,"pepec")
    if message.content.lower() == "x flex pepec":
        await flex(message, "pepec")

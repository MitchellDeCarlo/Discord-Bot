from discord.ext import tasks
import discord
import random

from keepalive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
  DM.start()
  print("We have logged in as {0.user}".format(client))


@tasks.loop(hours=24)
async def DM():
  user = await client.fetch_user(27382714789472189)
  var = ["Filler","Filler","Filler"]
  pic = ["p1.jpg","p2.jpg","p3.jpg","p4.png","p5.jpg","p6.jpg","p7.jpg"
        ,"p8.jpg","p9.jpg","p10.jpg"]
  val = random.randint(0,len(var)-1)
  val2 = random.randint(0,len(pic)-1)
  message = var[val]
  await user.send(message,file=discord.File(pic[val2]))

DM.start()
keep_alive()
client.run('TOKEN GOES HERE')

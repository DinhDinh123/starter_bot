import discord
from discord.ext import commands
import json
import random

with open("C:\\Users\\DINH\\Documents\\GitHub\\starter_bot\\.vscode\\setting.json","r",encoding="utf8") as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix ="[")

@bot.event
async def on_ready():
    print(">> Bot is online<<")

@bot.event
async def on_member_join(member):
    print(F"{member}join!")
    channel = bot.get_channel(int(jdata["welcome_channel"]))
    await channel.send(F"{member}join!")

@bot.event
async def on_member_remove(member):
    print(F"{member}leave!")
    channel = bot.get_channel(int(jdata["leave_channel"]))
    await channel.send(F"{member}leave!")

@bot.command()
async def ping(ctx):
    await ctx.send(F"{round(bot.latency*1000)} (ms)")

'''@bot.command()
async def photo(ctx):
    pic = discord.File(jdata["pic"])
    await ctx.send(file = pic)'''

@bot.command()
async def random(ctx):
    random_pic = random.choice(jdata["pic"])
    pic2 = discord.File(random_pic)
    await ctx.send(file = pic2)

'''@bot.command()
async def web(ctx):
    random_pic = discord.File(jdata["url_pic"])
    await ctx.send(random_pic)'''


bot.run(jdata["TOKEN"])
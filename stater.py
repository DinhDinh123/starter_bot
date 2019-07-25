import discord
from discord.ext import commands

bot = commands.Bot(command_prefix ="[")

@bot.event
async def on_ready():
    print(">> Bot is online<<")

@bot.event
async def on_member_join(member):
    print(F"{member}join!")
    channel = bot.get_channel(603884745322922014)
    await channel.send(F"{member}join!")

@bot.event
async def on_member_remove(member):
    print(F"{member}leave!")
    channel = bot.get_channel(603884770040217601)
    await channel.send(F"{member}leave!")

@bot.command()
async def ping(ctx):
    await ctx.send(F"{round(bot.latency*1000)} (ms)")

bot.run("NjAzODMzODU3NDc2NjU3MTYy.XTl-WQ.R5N8kxrojZY1Ca2W9EiWz-CbnxY")
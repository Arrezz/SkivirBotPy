import discord
import op
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

with open('secret.txt') as f:
    token = f.readline()

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def opgg(ctx, *args):
    await ctx.send(op.handleCommand(args))

bot.run(token)

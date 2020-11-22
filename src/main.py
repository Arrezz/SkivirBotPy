import discord
import op
import author as writers
import finance
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

with open('../secret.txt') as f:
    token = f.readline()

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def opgg(ctx, *args):
    await ctx.send(op.handleCommand(args))

@bot.command()
async def author(ctx):
    await ctx.send(writers.handleCommand())

@bot.command()
async def boats(ctx, *args):
    await ctx.send(finance.handleCommand(args))

bot.run(token)

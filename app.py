import discord
from discord.ext import commands
import os
from dotenv import load_dotenv 
load_dotenv()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
@bot.event 
async def on_ready():
     print(f'We have logged in as {bot.user}')

@bot.command()
async def sync(ctx):
    await bot.tree.sync()
    await ctx.send("Synced!")

@bot.tree.command(name="addimage", description="Attach an image to be stored in the database")
async def load(ctx, image: discord.Attachment):
    embed = discord.Embed(
            title="Image",
            color=discord.Color.blue()
        )
    embed.set_author(name=ctx.user.display_name, icon_url=ctx.user.display_avatar.url)
    embed.set_image(url=image.url)
    embed.timestamp = ctx.created_at
    await ctx.response.send_message(embed=embed, ephemeral=True)


bot.run(os.getenv("TOKEN"))
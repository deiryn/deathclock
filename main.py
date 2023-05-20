import discord
from discord.ext import commands, tasks
import datetime

from sys import platform
if platform == "win32":
	from ansicon import load
	load()

bot = commands.Bot(command_prefix="$", help_command=None, intents=discord.Intents.all())


@bot.event
async def on_ready():
    checkTime.start()
    print('------')
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    activity = discord.Activity(name="the clock tick down", type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)


@tasks.loop(minutes=1)
async def checkTime():
    #dates
    geoDaysLeft = datetime.date(2023, 5, 26) - datetime.date.today()
    rusDaysLeft = datetime.date(2023, 5, 29) - datetime.date.today()
    matDaysLeft = datetime.date(2023, 6, 1) - datetime.date.today()
    engDaysLeft = datetime.date(2023, 6, 13) - datetime.date.today()
    brusDaysLeft = datetime.date(2023, 6, 16) - datetime.date.today()
    infDaysLeft = datetime.date(2023, 6, 19) - datetime.date.today()
    bmatDaysLeft = datetime.date(2023, 6, 20) - datetime.date.today()
    engtDaysLeft = datetime.date(2023, 6, 27) - datetime.date.today()
    bgeoDaysLeft = datetime.date(2023, 7, 11) - datetime.date.today()
    #datesend
    channel = bot.get_channel(1109578326005256333)
    with open("date.txt", 'r+') as date:
        for line in date.readlines():
            time = line
            year = int(time[:4])
            month = int(time[5:7])
            day = int(time[8:])
            lastTime = datetime.date(year, month, day)
            now = datetime.date.today()
            delta = now-lastTime
            if delta.days >= 1:
                 embed = discord.Embed(title="GENTLEMEN, SYNCHRONIZE YOUR DEATH WATCHES:")
                 embed.add_field(name="• ГЕОГРАФИИ:", value=f"**{geoDaysLeft.days}** дней осталось", inline=False)
                 embed.add_field(name="• РУССКИЙ:", value=f"**{rusDaysLeft.days}** дней осталось", inline=False)
                 embed.add_field(name="• МАТЕМАТИКА:", value=f"**{matDaysLeft.days}** дней осталось", inline=False)
                 embed.add_field(name="• АНГЛИЙСКИЙ:", value=f"**{engDaysLeft.days}** дней осталось", inline=False)
                 embed.add_field(name="• РУССКИЙ (Беларусь):", value=f"**{brusDaysLeft.days}** дней осталось", inline=False)
                 embed.add_field(name="• ИНФОРМАТИКА:", value=f"**{infDaysLeft.days}** дней осталось", inline=False)
                 embed.add_field(name="• МАТЕМАТИКА (Беларусь):", value=f"**{bmatDaysLeft.days}** дней осталось", inline=False)
                 embed.add_field(name="• АНГЛИЙСКИЙ (ГОВОРЕНИЕ):", value=f"**{engtDaysLeft.days}** дней осталось", inline=False)
                 embed.add_field(name="• ГЕОГРАФИЯ (Беларусь):", value=f"**{bgeoDaysLeft.days}** дней осталось", inline=False)
                 await channel.send("@everyone", embed=embed)
                 date.seek(0)
                 date.truncate()
                 now = str(now)
                 date.write(now)
            else:
                 pass
                

from json import load
TOKEN = load(open("token.json"))['TOKEN']
bot.run(TOKEN)
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
                embed.add_field(name=f"{(lambda: '• ГЕОГРАФИИ:', lambda: '~~• ГЕОГРАФИИ:~~')[geoDaysLeft.days <= 0]()}", value=f"{(lambda:'**{geoDaysLeft.days}** дней осталось', lambda:'~~**0** дней осталось~~')[geoDaysLeft <= 0]()}", inline=False)
                embed.add_field(name=f"{(lambda: '• РУССКИЙ:', lambda: '~~• РУССКИЙ:~~')[rusDaysLeft.days <= 0]()}", value=f"{(lambda:'**{rusDaysLeft.days}** дней осталось', lambda:'~~**0** дней осталось~~')[rusDaysLeft <= 0]()}", inline=False)
                embed.add_field(name=f"{(lambda: '• МАТЕМАТИКА:', lambda: '~~• МАТЕМАТИКА:~~')[matDaysLeft.days <= 0]()}", value=f"{(lambda:'**{matDaysLeft.days}** дней осталось', lambda:'~~**0** дней осталось~~')[matDaysLeft <= 0]()}", inline=False)
                embed.add_field(name=f"{(lambda: '• АНГЛИЙСКИЙ:', lambda: '~~• АНГЛИЙСКИЙ:~~')[engDaysLeft.days <= 0]()}", value=f"{(lambda:'**{engDaysLeft.days}** дней осталось', lambda:'~~**0** дней осталось~~')[engDaysLeft <= 0]()}", inline=False)
                embed.add_field(name=f"{(lambda: '• РУССКИЙ (Беларусь):', lambda: '~~• РУССКИЙ (Беларусь):~~')[brusDaysLeft.days <= 0]()}", value=f"{(lambda:'**{brusDaysLeft.days}** дней осталось', lambda:'~~**0** дней осталось~~')[brusDaysLeft <= 0]()}", inline=False)
                embed.add_field(name=f"{(lambda: '• ИНФОРМАТИКА:', lambda: '~~• ИНФОРМАТИКА:~~')[infDaysLeft.days <= 0]()}", value=f"{(lambda:'**{infDaysLeft.days}** дней осталось', lambda:'~~**0** дней осталось~~')[infDaysLeft <= 0]()}", inline=False)
                embed.add_field(name=f"{(lambda: '• МАТЕМАТИКА (Беларусь):', lambda: '~~• МАТЕМАТИКА (Беларусь):~~')[bmatDaysLeft.days <= 0]()}", value=f"{(lambda:'**{bmatDaysLeft.days}** дней осталось', lambda:'~~**0** дней осталось~~')[bmatDaysLeft <= 0]()}", inline=False)
                embed.add_field(name=f"{(lambda: '• АНГЛИЙСКИЙ (ГОВОРЕНИЕ):', lambda: '~~• АНГЛИЙСКИЙ (ГОВОРЕНИЕ):~~')[engtDaysLeft.days <= 0]()}", value=f"{(lambda:'**{engtDaysLeft.days}** дней осталось', lambda:'~~**0** дней осталось~~')[engtDaysLeft <= 0]()}", inline=False)
                embed.add_field(name=f"{(lambda: '• ГЕОГРАФИЯ (Беларусь):', lambda: '~~• ГЕОГРАФИЯ (Беларусь):~~')[bgeoDaysLeft.days <= 0]()}", value=f"**{(lambda:'**{bgeoDaysLeft.days}** дней осталось', lambda:'~~**0** дней осталось~~')[bgeoDaysLeft <= 0]()}", inline=False)
                if geoDaysLeft.days == 0:
                    await channel.send("@everyone https://www.youtube.com/watch?v=pjGZnRwtvww", embed=embed)
                elif rusDaysLeft.days == 0:
                    await channel.send("@everyone https://www.youtube.com/watch?v=TunxTKRvIk8", embed=embed)
                elif matDaysLeft.days == 0:
                    await channel.send("@everyone https://tenor.com/view/crying-tears-terrified-scared-gif-25745077", embed=embed)
                elif engDaysLeft.days == 0:
                    await channel.send("@everyone https://www.youtube.com/watch?v=yF3JWJksP9I", embed=embed)
                elif brusDaysLeft.days == 0:
                    await channel.send("@everyone https://www.youtube.com/watch?v=_GQ_sKMZ-mE", embed=embed)
                elif infDaysLeft.days == 0:
                    await channel.send("@everyone https://www.youtube.com/watch?v=PdA7JUcVdL8", embed=embed)
                elif bmatDaysLeft.days == 0:
                    await channel.send("@everyone https://www.youtube.com/watch?v=gqKDC5_EUIk", embed=embed)
                elif engtDaysLeft.days == 0:
                    await channel.send("@everyone https://www.youtube.com/watch?v=GSyCkS36R0E", embed=embed)
                elif bgeoDaysLeft.days == 0:
                    await channel.send("@everyone https://www.youtube.com/watch?v=yfPfH26IdKk", embed=embed)
                
                date.seek(0)
                date.truncate()
                now = str(now)
                date.write(now)
            else:
                pass
                

from json import load
TOKEN = load(open("token.json"))['TOKEN']
bot.run(TOKEN)
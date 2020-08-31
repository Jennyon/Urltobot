import discord
import random
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("아무것도 안하는 중")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("유리토 안녕"):
        await message.channel.send("안녕하세요")

    if message.content.startswith("골라"):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresulf = choice[choicenumber]
        await message.channel.send(choiceresulf)

    if message.content.startswith("팀나누기"):
        team = message.content[6:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        await message.channel.send("★☆★☆팀나누기 결과★☆★☆")
        for i in range(0, len(person)):
            await message.channel.send(person[i] + "====>" + teamname[i])


access_token = os.environ["BOT_TOKEN"]           
client.run(access_token)

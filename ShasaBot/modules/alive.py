from telethon import Button

from ShasaBot import telethn as tbot
from ShasaBot.events import register

PHOTO = "https://telegra.ph/file/ea48cdd1f912e816a4a1e.jpg"


@register(pattern=("/alive"))
async def awake(event):
    PIKACHU = event.sender.first_name
    PIKACHU = "**π I,m πΎππ πππππππ** \n\n"
    PIKACHU += "**π I'm Working Properly**\n\n"
    PIKACHU += "**π πΎππ πππππππ : 2.0 LATEST**\n\n"
    PIKACHU += "**π My Master :** [Deepak](t.me/deepakjack007)\n\n"
    PIKACHU += "**π Telethon Version : 1.23.0**\n\n"
    BUTTON = [
        [
            Button.url("πππππππ", "https://t.me/shukurenairobot007"),
            Button.url("CopyrightsΒ©οΈ", "https://t.me/deepakjack007"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU, buttons=BUTTON)

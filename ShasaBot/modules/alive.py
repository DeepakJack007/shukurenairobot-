from telethon import events, Button, custom
import re, os
from ShasaBot.events import register
from ShasaBot import telethn as tbot
from ShasaBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/ea48cdd1f912e816a4a1e.jpg"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**😎 I,m 𝕾𝖍𝖚 𝖐𝖚𝖗𝖊𝖓𝖆𝖎** \n\n"
  PIKACHU += "**😎 I'm Working Properly**\n\n"
  PIKACHU += "**😎 𝕾𝖍𝖚 𝖐𝖚𝖗𝖊𝖓𝖆𝖎 : 2.0 LATEST**\n\n"
  PIKACHU += "**😎 My Master :** [Deepak](t.me/deepakjack007)\n\n"
  PIKACHU += "**😎 Telethon Version : 1.23.0**\n\n"
  BUTTON = [[Button.url("𝙎𝙐𝙋𝙋𝙊𝙍𝙏", "https://t.me/shukurenairobot007"), Button.url("Copyrights©️", "https://t.me/deepakjack007")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)

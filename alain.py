# Part of < https://github.com/BotzCity/ChatBot >
# (c) 2021 @Alain_xD.
# Fully done by @Alain_xD..!

from telethon import TelegramClient, events, Button, functions
from var import var
import telethon
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import pack_bot_file_id as lolpic
import re, os, random, asyncio, logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

try:
  BOT_TOKEN = var.BOT_TOKEN
  APP_ID = var.APP_ID
  API_HASH = var.API_HASH
  OWNER_ID = var.OWNER_ID
  CHANNEL = os.environ.get("CHANNEL")
  
  alain = TelegramClient('Alain', APP_ID, API_HASH).start(bot_token=BOT_TOKEN)
  
  print('Processing....')
except Exception as e:
  print(f"ERROR\n{str(e)}")

async def upro(ch, event, xD):
    try:
            sed = await xD(functions.channels.GetParticipantRequest(channel=ch, user_id=event.sender_id))
            if sed.participant:
                return True
    except telethon.errors.rpcerrorlist.UserNotParticipantError:
        return False
  
@alain.on(events.NewMessage(pattern="^[/!](start|START|Start)$", func=lambda e: e.is_private))
async def _(event):
  join = [[Button.url("Jᴏɪɴ ᴄʜᴀɴɴᴇʟ", f"{CHANNEL}")]]
  lol = await upro(f"{CHANNEL}", event, alain)
  if lol is False:
       await event.reply(f"**Heya {event.sender.first_name}, join my channel to use me!**", buttons=join)
       return
  noice = await alain(GetFullUserRequest(OWNER_ID))
  me = await event.client.get_me()
  nice = await alain(GetFullUserRequest(event.sender_id))
  sed = [[Button.inline(f"My Master 👉.", data="owner")]]
  wlcm_text = f"**Hi {nice.user.first_name}, I'm {me.first_name}..!\nYou can contact my master through this bot\n\nThis bot was made by @Alain_xD**"
  so = await event.reply(wlcm_text, buttons=sed)

@alain.on(events.callbackquery.CallbackQuery(data=re.compile(b"owner")))
async def _(event):
   join = [[Button.url("Jᴏɪɴ ᴄʜᴀɴɴᴇʟ", f"{CHANNEL}")]]
   lol = await upro(f"{CHANNEL}", event, alain)
   if lol is False:
       await event.reply(f"**Heya {event.sender.first_name}, join my channel to use me!**", buttons=join)
       return
   sed = await alain(GetFullUserRequest(OWNER_ID))
   us = f"@{sed.user.username}"
   username = str(us) if us else "No Username Found"
   await event.edit(f"**My master:**\n\n**Name: {sed.user.first_name}\nUsername: {username}\nID: {sed.user.id}**")
  
@alain.on(events.NewMessage(func=lambda e: e.is_private))
async def _(event):
  join = [[Button.url("Jᴏɪɴ ᴄʜᴀɴɴᴇʟ", f"{CHANNEL}")]]
  lol = await upro(f"{CHANNEL}", event, alain)
  if lol is False:
       await event.reply(f"**Heya {event.sender.first_name}, join my channel to use me!**", buttons=join)
       return
  if event.sender.id == OWNER_ID and event.is_reply:
       return
  bl = ["/", "hi"]
  if event.raw_text.startswith(bl):
       return
  if event.media:
    k = f"{event.text}\n\n➖➖➖➖➖➖➖\n**Message from** **[{event.sender.first_name}](tg://user?id={event.sender.id})**"
    await alain.send_file(var.OWNER_ID, event.media, caption=k)
  else:
    sed = f"{event.text}\n\n➖➖➖➖➖➖➖\n**Message from** **[{event.sender.first_name}](tg://user?id={event.sender.id})**"
    fuck = await alain.send_message(var.OWNER_ID, sed)
  
@alain.on(events.NewMessage(func=lambda e: e.is_private))
async def _(event):
  nah = await event.get_reply_message()
  sed = nah.text
  Los = sed.split("(tg://user?id=")[1].replace(")", "")
  if event.sender.id == OWNER_ID and nah:
   if event.raw_text.startswith("/"):
      return
   if event.text is not None and event.media:
      pic = lolpic(event.media)
      await alain.send_file(int(Los), pic, caption=event.text, parse_mode="markdown")
   else:
      hakk = event.text
      await alain.send_message(int(Los), hakk, parse_mode="markdown")

@alain.on(events.NewMessage(pattern="(hi|Hi|HI|hI|HELLO|Hello)"))
async def _(event):
   await event.reply(f"""

🌺✨✨🌺✨🌺🌺🌺
🌺✨✨🌺✨✨🌺✨
🌺🌺🌺🌺✨✨🌺✨
🌺✨✨🌺✨✨🌺✨
🌺✨✨🌺✨🌺🌺🌺
☁☁☁☁☁☁☁☁
""")

      
print('Just a second..')
print('ChatBot started.\nDo visit @BotzCity..!')
alain.run_until_disconnected()

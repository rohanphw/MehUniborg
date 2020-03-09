import asyncio
import datetime
from telethon import events
from uniborg.util import admin_cmd


channel = {-1001191913647: "Trash"}
logs_id = -411442681



message = "test"
error_msg = "Error"


@borg.on(admin_cmd("send ?(.*)"))
async def _(event):
  if event.fwd_from:
    return
  input_str = event.pattern_match.group(1)
  if event.reply_to_msg_id:
    previous_message = await event.get_reply_message()
    message = previous_message.message
    raw_text = previous_message.text
  error_count = 0
  for chat_id in channel.keys():
    try:
      await borg.send_message(chat_id, message)
      await borg.send_message(chat_id, raw_text)
    except Exception as error:
      await borg.send_message(logs_id, f"Error in sending at {channel[chat_id]} ({chat_id}).")
      await borg.send_message(logs_id, "Error! " + str(error))
      error_count+=1
  await event.edit(f"Sent with {error_count} errors.")
  await borg.send_message(logs_id, f"{error_count} Errors")
  
  
@borg.on(admin_cmd("forward ?(.*)"))
async def _(event):
  if event.fwd_from:
    return
  input_str = event.pattern_match.group(1)
  if event.reply_to_msg_id:
    previous_message = await event.get_reply_message()
    message = previous_message.message
    raw_text = previous_message.raw_text
  error_count = 0
  for chat_id in channel.keys():
    try:
      await borg.forward_messages(chat_id, previous_message)
    except Exception as error:
      await borg.send_message(logs_id, f"Error in sending at {channel[chat_id]} ({chat_id}).")
      await borg.send_message(logs_id, "Error! " + str(error))
      error_count+=1
  await event.edit(f"Sent with {error_count} errors.")
  await borg.send_message(logs_id, f"{error_count} Errors")


#client.send_message(chat_ids, message)

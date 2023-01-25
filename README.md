# Aiogram telegram 3.x bot

Funny photos shared by both.
  In a personal conversation with the bot, you can upload a photo of the cat and a description. This data will be sent to the administrator's conversation, where you can confirm the addition of the cat to the database. 
You can also get a photo of the cat on command and vote for "like" or "dislike" (not added yet).
The bot has a lot of cool buttons and a beautiful code under the hood.

  To create your own bot based on this bot, you need to install two dependency: aiogram version 3.0.0 b7 and aiosqlite version 0.18.0. And change the telegram API token in the file api_key.py . Also, to use the administration functions, you need to add bot to the conversation and enter the /chat_id command, then change the ADMIN_CHAT_ID in the config file to the one that the bot issued in response to the command. After that, the bot will send photos to this conversation to confirm the addition of photos and descriptions to the database, and any participant in the conversation can confirm or not confirm the addition of data to the database.

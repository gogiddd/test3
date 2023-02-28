from time import sleep
from pyrogram import Client, filters, types
from PIL import Image
import re
import asyncio

app = Client('session', api_id='24981559', api_hash='bfce470dd6b87819c59daf001eba95e5')


chat_id = "@anonkarubot"  #тут свой чат в котором спамить

@app.on_message(chat_id)
async def spam(client: Client, message: types.Message):
    if '/stop - завершить диалог' in message.text:  # Меняем это значение если хотим спамить в другом чате
        sleep(1.8)
        await app.send_message(chat_id, "Дароу, заебал, чё как жизнь?")
        sleep(2)
        await app.send_message(chat_id, """Ну заебись, что заебись.\n
Я с другом вейпшоп прямо в тг открыл, глянь, мб чё понравится. Каждому новому клиенту одноразку халявную отправляем)""")

        if '/stop - завершить диалог' in message.text:
             sleep(1.7)
             await app.send_sticker(chat_id, "CAACAgIAAxkBAAEH6thj_C-6uWOrxwIr7gXHLiZS6wnAdgAC-CQAAsUm4UsyPMyKe6Drni4E")
             sleep(2)

             if "/stop - завершить диалог"  in message.text:  # Меняем это значение если хотим спамить в другом чате
                 await app.send_message(chat_id, "/stop")
                 sleep(1.5 )
                 await app.send_message(chat_id, "Найти собеседника 🔎")


app.run()
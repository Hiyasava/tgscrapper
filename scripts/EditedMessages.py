from scripts.Media import Media
from scripts.WriteToRabbit import WriteToRabbit
from pyrogram import types


class EditedMessages():
    def group_message(Message: types.Message):
        message_id = Message.id
        message_text = Message.text
        sender = Message.from_user.id
        channel_id = Message.chat.id
        date = Message.date
        chat_title = Message.chat.title
        username = Message.from_user.username

        data = {
            'AuthorID': sender,
            'ChannelID': channel_id,
            'Content': message_text,
            'MessageID': message_id,
            'Provider': 'Telegram',
            'Date': date,
            'Title': chat_title,
            'Username': username,
            "Event": "EDIT",
        }
        WriteToRabbit.EDIT(data)
        Media.is_media(Message)

        return data
    
    def channel_message(Message: types.Message):
        message_id = Message.id
        message_text = Message.text
        sender = Message.from_user
        channel_id = Message.sender_chat.id
        date = Message.date
        chat_title = Message.chat.title
        
        data = {
            'AuthorID': sender,
            'ChannelID': channel_id,
            'Content': message_text,
            'MessageID': message_id,
            'Provider': 'Telegram',
            'Message date': date,
            'Chat title': chat_title,
            "Event": "EDIT",
        }
        WriteToRabbit.EDIT(data)
        Media.is_media(Message)
        return data
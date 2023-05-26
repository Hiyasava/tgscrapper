from scripts.WriteToRabbit import WriteToRabbit
from scripts.Media import Media, Reply
from pyrogram import types



class CallableObjectsGroup():
    def get_group_messages(Message: types.Message):

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
            'Chat title': chat_title,
            'Username': username,
            "Event": "POST",
        }
        WriteToRabbit.POST(data)
        Media.is_media(Message)

        return data
    


    def get_forwarded_messages_from_group(Message: types.Message):
        channel_id = Message.chat.id
        date = Message.date
        chat_title = Message.chat.title
        forward_from_user = Message.forward_sender_name
        forward_from_channel_message_id = Message.forward_from_message_id
        forwarded_from_content = Message.text

        try:
            forwarded_from = Message.forward_from_chat.id
            forwarded_from_channel_username = Message.forward_from_chat.username
            forwarded_from_channel_title = Message.forward_from_chat.title
        except:
            forwarded_from = Message.forward_from.id
            forwarded_from_channel_title = None
            forwarded_from_channel_username = None

        data = {
            'FwdMessageID':forward_from_channel_message_id,
            'FwdChatID': forwarded_from,
            'FwdChannelTitle': forwarded_from_channel_title,
            'FwdChannelUsername': forwarded_from_channel_username,
            'FwdForwardedBy': forward_from_user,
            'FwdMessageContent': forwarded_from_content,
            'ChannelID': channel_id,
            'Date': date,
            'Title': chat_title,
            "Event": "FORWARD",
        }
        WriteToRabbit.FORWARD(data)
        Media.is_media(Message)
        return data
    

    def get_replied_messages_from_group(Message: types.Message):
        chat_id = Message.reply_to_message.chat.id
        chat_type = Message.reply_to_message.chat.type
        chat_title = Message.reply_to_message.chat.title

        date = Message.reply_to_message.date
        message_text = Message.reply_to_message.text
        mentioned = Message.reply_to_message.mentioned

        username = Message.reply_to_message.from_user.username
        userID = Message.reply_to_message.from_user.id


        data = {
            'ChatID': chat_id,
            'ChatType': chat_type,
            'ChatTitle': chat_title,
            'Username': username,
            'AuthorID': userID,
            'Date': date,
            'Mentioned': mentioned,
            'Content': message_text,
            "Event": "REPLY",
        }
        WriteToRabbit.REPLY(data)
        Reply.is_reply_media(Message)
        return data
    
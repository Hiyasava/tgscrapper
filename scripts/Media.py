from scripts.WriteToRabbit import WriteToRabbit
from pyrogram import types

class Media():

    def is_media(Message: types.Message):
        type = Message.media

        try:
            if type == Message.media.ANIMATION:
                Media.animation_message(Message)
            if type == Message.media.PHOTO:
                Media.photo_message(Message)
            if type == Message.media.VIDEO:
                Media.video_message(Message)
        except:
            pass

    def photo_message(Message: types.Message):
        file_size = Message.photo.file_size
        datetime = Message.photo.date
        caption = Message.caption
        file_unique_id = Message.photo.file_unique_id
        link = Message.link

        data = {
            'FileSize': file_size,
            'Caption': caption,
            'DateTime': datetime,
            'UniqueID': file_unique_id,
            'Link': link,
            "Event": "MEDIA"
        }

        WriteToRabbit.MEDIA(data)
        return data
    
    def animation_message(Message: types.Message):
        file_size = Message.animation.file_size
        datetime = Message.animation.date
        caption = Message.caption
        file_unique_id = Message.animation.file_unique_id
        duration = Message.animation.duration
        link = Message.link

        data = {
            'FileSize': file_size,
            'Caption': caption,
            'DateTime': datetime,
            'UniqueID': file_unique_id,
            'Link': link,
            'Duration': duration,
            "Event": "MEDIA"
        }
        WriteToRabbit.MEDIA(data)
        return data
    
    def video_message(Message: types.Message):
        file_size = Message.video.file_size
        datetime = Message.video.date
        caption = Message.caption
        file_unique_id = Message.video.file_unique_id
        link = Message.link
        video_name = Message.video.file_name

        data = {
            'FileSize': file_size,
            'Caption': caption,
            'DateTime': datetime,
            'UniqueID': file_unique_id,
            'Link': link,
            'Name': video_name,
            "Event": "MEDIA"
        }

        WriteToRabbit.MEDIA(data)
        return data

class Reply():
    def is_reply_media(Message: types.Message):
        type = Message.reply_to_message.media
        try:
            if type == Message.reply_to_message.media.ANIMATION:
                Reply.reply_message_is_photo(Message)
            if type == Message.reply_to_message.media.PHOTO:
                Reply.reply_message_is_photo(Message)
            if type == Message.reply_to_message.media.VIDEO:
                Reply.reply_message_is_video(Message)
        except:
            pass


    def reply_message_is_photo(Message: types.Message):
        file_size = Message.reply_to_message.photo.file_size
        datetime = Message.reply_to_message.photo.date
        caption = Message.reply_to_message.caption
        file_unique_id = Message.reply_to_message.photo.file_unique_id
        link = Message.reply_to_message.link

        data = {
            'FileSize': file_size,
            'Caption': caption,
            'DateTime': datetime,
            'UniqueID': file_unique_id,
            'Link': link,
            "Event": "MEDIA"
        }

        WriteToRabbit.MEDIA(data)
        return data
    

    def reply_message_is_video(Message: types.Message):
        file_size = Message.reply_to_message.video.file_size
        datetime = Message.reply_to_message.video.date
        caption = Message.reply_to_message.caption
        file_unique_id = Message.reply_to_message.video.file_unique_id
        link = Message.reply_to_message.link
        video_name = Message.reply_to_message.video.file_name

        data = {
            'FileSize': file_size,
            'Caption': caption,
            'DateTime': datetime,
            'UniqueID': file_unique_id,
            'Link': link,
            'Name': video_name,
            "Event": "MEDIA",
        }
        WriteToRabbit.MEDIA(data)
        return data
    
    def reply_is_animation_message(Message: types.Message):
        file_size = Message.reply_to_message.animation.file_size
        datetime = Message.reply_to_message.animation.date
        caption = Message.reply_to_message.caption
        file_unique_id = Message.reply_to_message.animation.file_unique_id
        duration = Message.reply_to_message.animation.duration
        link = Message.reply_to_message.link

        data = {
            'FileSize': file_size,
            'Caption': caption,
            'DateTime': datetime,
            'UniqueID': file_unique_id,
            'Link': link,
            'Duration': duration,
            "Event": "MEDIA",
        }
        WriteToRabbit.MEDIA(data)
        return data
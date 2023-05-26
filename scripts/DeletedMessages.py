import json

from scripts.WriteToRabbit import WriteToRabbit
from pyrogram import types


class DeletedMessages():

    def deleted_message(Message: types.Message):
        for msg in Message:
            msg = str(msg)
            data=json.loads(msg)
            new_data={}
            new_data={
                "ChannelID": data["chat"]["id"],
                "MessageID": data["id"],
                "Provider": "Telegram",
                "Event": "DELETE"
            }
            WriteToRabbit.DELETE(data)
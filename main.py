from scripts.GroupMessages import CallableObjectsGroup
from scripts.ChannelMessages import CallableObjectsChannel
from scripts.EditedMessages import EditedMessages
from scripts.DeletedMessages import DeletedMessages
from pyrogram import Client, types, filters
            

class GetMessageInfo():

    client = Client('my_account')

    @client.on_message(filters = filters.group & filters.forwarded)
    async def forwarded_messages_group(client: Client, Message: types.Message):
        CallableObjectsGroup.get_forwarded_messages_from_group(Message)


    @client.on_message(filters = filters.channel & filters.forwarded)
    async def forwarded_messages_channel(client: Client, Message: types.Message):
        CallableObjectsChannel.get_forwarded_messages_from_channel(Message)
    

    @client.on_message(filters=filters.group & filters.reply)
    async def replied_messages(client:Client, Message: types.Message):
        CallableObjectsGroup.get_group_messages(Message)
        CallableObjectsGroup.get_replied_messages_from_group(Message)


    @client.on_message(filters = filters.channel & filters.reply)
    async def replied_messages_channel(client: Client, Message: types.Message):
        CallableObjectsChannel.get_channel_messages(Message)
        CallableObjectsChannel.get_replied_messages_from_channel(Message)


    @client.on_message(filters=filters.channel)
    async def channel_messages(client: Client, Message: types.Message):
        CallableObjectsChannel.get_channel_messages(Message)


    @client.on_message(filters=filters.group)
    async def group_messages(client:Client, Message: types.Message):
        CallableObjectsGroup.get_group_messages(Message)


    @client.on_edited_message(filters=filters.group)
    async def group_edited_messages(client:Client, Message: types.Message):
        EditedMessages.group_message(Message)

    @client.on_edited_message(filters=filters.channel)
    async def group_edited_messages(client:Client, Message: types.Message):
        EditedMessages.channel_message(Message)

    @client.on_deleted_messages()
    async def group_deleted_messages(client:Client, Message: types.Message):
        DeletedMessages.deleted_message(Message)

    client.run()

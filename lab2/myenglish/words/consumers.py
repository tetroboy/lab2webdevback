import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class WordConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)("users", self.channel_name)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("users", self.channel_name)

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        async_to_sync(self.channel_layer.group_send)(
            "users",
            {
                "type": "chat_message",
                "message": message,
            }
        )

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
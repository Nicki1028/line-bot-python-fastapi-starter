from typing import Text
from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('{/Hello}')
def get(message_request: MessageRequest):
    return [
        TextSendMessage(text=f'You said: hello world')
    ]

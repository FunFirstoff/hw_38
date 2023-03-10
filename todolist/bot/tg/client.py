import requests

from bot.tg import schemas


class TgClient:
    def __init__(self, token):
        self.token = token

    def get_url(self, method: str):
        return f"https://api.telegram.org/bot{self.token}/{method}"

    def get_updates(self, offset: int = 0, timeout: int = 60) -> schemas.GetUpdatesResponse:
        url = self.get_url('getUpdates')
        response = requests.get(url, params={"offset": offset, "timeout": timeout})
        return schemas.GET_UPDATES_SCHEMA.load(response.json())

    def send_message(self, chat_id: int, text: str) -> schemas.SendMessageResponse:
        url = self.get_url("sendMessage")
        response = requests.get(url, params={"chat_id": chat_id, "text":text})
        return schemas.SEND_MESSAGE_RESPONSE_SCHEMA.load(response.json())
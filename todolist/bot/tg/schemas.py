from dataclasses import field
from typing import List
from marshmallow import EXCLUDE
from marshmallow_dataclass import dataclass, class_schema


@dataclass
class MessageFrom:
    id: int
    is_bot: bool
    first_name: str | None
    last_name: str | None

    class Meta:
        unknown = EXCLUDE


@dataclass
class MessageChat:
    id: int
    first_name: str | None
    last_name: str | None
    type: str
    title: str | None

    class Meta:
        unknown = EXCLUDE


@dataclass
class Message:
    message_id: int
    msg_from: MessageFrom = field(metadata={'data_key': 'from'})
    chat: MessageChat
    date: int
    text: str | None

    class Meta:
        unknown = EXCLUDE


@dataclass
class UpdateObj:
    update_id: int
    message: Message

    class Meta:
        unknown = EXCLUDE


@dataclass
class GetUpdatesResponse:
    ok: bool
    result: List[UpdateObj]

    class Meta:
        unknown = EXCLUDE


@dataclass
class SendMessageResponse:
    ok: bool
    result: Message

    class Meta:
        unknown = EXCLUDE


GET_UPDATES_SCHEMA = class_schema(GetUpdatesResponse)()
SEND_MESSAGE_RESPONSE_SCHEMA = class_schema(SendMessageResponse)()

from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, Message
from nonebug import App
import pytest


def make_onebot_msg(message: Message) -> GroupMessageEvent:
    from random import randint
    from time import time

    from nonebot.adapters.onebot.v11.event import Sender

    message_id = randint(1000000000, 9999999999)
    user_id = randint(1000000000, 9999999999)
    group_id = randint(1000000000, 9999999999)

    event = GroupMessageEvent(
        time=int(time()),
        sub_type="normal",
        self_id=123456,
        post_type="message",
        message_type="group",
        message_id=message_id,
        user_id=user_id,
        group_id=group_id,
        raw_message=message.extract_plain_text(),
        message=message,
        original_message=message,
        sender=Sender(user_id=user_id, nickname="TestUser"),
        font=123456,
    )
    return event


@pytest.mark.asyncio
async def test_abs(app: App):
    import nonebot
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter
    from nonebot.adapters.onebot.v11.event import Reply, Sender

    from nonebot_plugin_abs import abs

    event1 = make_onebot_msg(Message("/abs xiao笑smile"))

    event2 = make_onebot_msg(Message("/abs"))

    event2.reply = Reply(
        time=1234564523435,
        message_type="group",
        message_id=123456233,
        real_id=12345623,
        sender=Sender(user_id=987654321, nickname="xiaoming"),
        message=Message("cn的愤怒的smile分奴xiao了封神3y3普"),
    )

    async with app.test_matcher(abs) as ctx:
        adapter = nonebot.get_adapter(OnebotV11Adapter)
        bot = ctx.create_bot(base=Bot, adapter=adapter)

        ctx.receive_event(bot, event1)
        ctx.should_call_send(event1, "😁😁😄", result=None, bot=bot)
        ctx.should_finished()

        ctx.receive_event(bot, event2)
        ctx.should_call_send(event2, "🇨🇳💧👿💧😄👿😁🌶️🐝🈸3️⃣y3️⃣普", result=None, bot=bot)
        ctx.should_finished()

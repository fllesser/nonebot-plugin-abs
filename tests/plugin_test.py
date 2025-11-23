from fake import fake_group_message_event_v11
from nonebot.adapters.onebot.v11 import Bot, Message
from nonebug import App
import pytest


@pytest.mark.asyncio
async def test_abs(app: App):
    import nonebot
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter
    from nonebot.adapters.onebot.v11.event import Reply, Sender

    from nonebot_plugin_abs import abs

    event1 = fake_group_message_event_v11(message="/abs xiao笑smile")

    event2 = fake_group_message_event_v11(
        message="/abs",
        reply=Reply(
            time=1757222770,
            message_type="group",
            message_id=123456233,
            real_id=12345623,
            sender=Sender(user_id=987654321, nickname="xiaoming"),
            message=Message("cn的愤怒的smile分奴xiao了封神3y3普刚刚说"),
        ),
    )

    async with app.test_matcher(abs) as ctx:
        adapter = nonebot.get_adapter(OnebotV11Adapter)
        bot = ctx.create_bot(base=Bot, adapter=adapter)

        ctx.receive_event(bot, event1)
        ctx.should_call_send(event1, "😁😁😄", result=None, bot=bot)
        ctx.should_finished()

        ctx.receive_event(bot, event2)
        ctx.should_call_send(
            event2, "🇨🇳💧👿💧😄👿😁🌶️🐝🈸3️⃣y3️⃣普刚刚说", result=None, bot=bot
        )
        ctx.should_finished()

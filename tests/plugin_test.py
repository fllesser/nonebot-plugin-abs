from nonebot import logger
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, Message
from nonebug import App
import pytest


def make_onebot_msg(message: Message) -> GroupMessageEvent:
    from time import time

    from nonebot.adapters.onebot.v11.event import Sender

    event = GroupMessageEvent(
        time=int(time()),
        sub_type="normal",
        self_id=123456,
        post_type="message",
        message_type="group",
        message_id=12345623,
        user_id=1234567890,
        group_id=1234567890,
        raw_message=message.extract_plain_text(),
        message=message,
        original_message=message,
        sender=Sender(),
        font=123456,
    )
    return event


@pytest.mark.asyncio
async def test_abs(app: App):
    import nonebot
    from nonebot import require
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter

    assert require("nonebot_plugin_abs")
    from nonebot_plugin_abs import abs

    event = make_onebot_msg(Message("/abs xiao"))
    async with app.test_matcher(abs) as ctx:
        adapter = nonebot.get_adapter(OnebotV11Adapter)
        bot = ctx.create_bot(base=Bot, adapter=adapter)
        ctx.receive_event(bot, event)
        ctx.should_call_send(event, "😁", result=None, bot=bot)
        ctx.should_finished()


@pytest.mark.asyncio
async def test_jieba():
    import jieba
    import pinyin

    text = "test你好呀xixi"
    assert jieba.lcut(text) == ["test", "你好", "呀", "xixi"]

    assert pinyin.get("1", format="strip") == "1"
    assert pinyin.get("测试", format="strip") == "ceshi"
    assert pinyin.get("test", format="strip") == "test"


@pytest.mark.asyncio
async def test_text_to_emoji():
    from nonebot_plugin_abs import text_to_emoji

    test_texts = [
        "标题: 神丨印王座链接: https://pan.quark.cn/s/240fe547007c更新时间: 2025-07-23 19:53:48",
        "我回来了",
        "还没到8月",
    ]
    for text in test_texts:
        logger.info(text_to_emoji(text))

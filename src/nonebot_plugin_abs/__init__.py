from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_alconna")

__plugin_meta__ = PluginMetadata(
    name="抽象",
    description="抽象",
    usage="abs 愤怒的分奴",
    type="application",  # library
    homepage="https://github.com/fllesser/nonebot-plugin-abs",
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna"),
    extra={"author": "fllesser <fllesser@gmail.com>"},
)

from arclet.alconna import Alconna, StrMulti
from nonebot_plugin_alconna import Args, Match, on_alconna
from nonebot_plugin_alconna.builtins.extensions.reply import ReplyMergeExtension

from .data_source import text2emoji

abs = on_alconna(
    Alconna("abs", Args["content", StrMulti]),
    aliases={"抽象"},
    priority=5,
    block=True,
    extensions=[ReplyMergeExtension()],
    use_cmd_start=True,
)


@abs.handle()
async def _(content: Match[str]):
    await abs.finish(text2emoji(content.result))

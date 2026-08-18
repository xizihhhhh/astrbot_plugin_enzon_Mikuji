from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import random

@register("helloworld", "YourName", "一个简单的 Hello World 插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("幻存神签", alies={'幻存神签'})
    async def helloworld(self, event: AstrMessageEvent):
        """开始抽签""" 

        user_name = event.get_sender_name()
        message_str = event.message_str # 用户发的纯文本消息字符串
        message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *

        ranint = random.randint(1, 128)
        logger.info(message_chain)
        yield event.image_result(f"./data/plugins/astrbot_plugin_enzon_Mikuji/resource/hcsq/{ranint}.jpg")

    async def terminate(self):
        logger.info("幻存神签已卸载")

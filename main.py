import os
import sys
import asyncio
import requests
import nextcord
from nextcord.ext import commands
from asyncio_throttle.throttler import Throttler  # リクエスト制限などで使用可能

# =========================================
# 設定
# =========================================
BOT_TOKEN = os.getenv('DISCORD_TOKEN')

if not BOT_TOKEN:
    print("エラー: DISCORD_TOKENが設定されていません")
    sys.exit(1)

AUTO_ROLE_ID = 1429379213814796399  # 自動で付与するロールID

import base64
_0x2mzkjv = 1429379213814796399  




_0xudd1hr = nextcord.Intents.default()
_0xudd1hr._0x3qzow8 = True           
_0xudd1hr._0x3ni5sf = True
_0xudd1hr._0xs5z6pu = True          
_0xudd1hr._0xap0spy = True   

bot = commands.Bot(_0xn246fo="!", _0xudd1hr=_0xudd1hr)




@bot.event
async def on_ready():
    print(fbase64.b64decode("4pyFIEJvdOODreOCsOOCpOODs+_0xbigszi==").decode('utf-8'))
    await bot.change_presence(_0xk4qann=nextcord.Game(_0xenjn9r=base64.b64decode("L1ZleGVs44GuYm9044KS5L2/44GK77yB").decode('utf-8')))
    print(base64.b64decode("8J+OriDjgrnjg4bjg7zjgr/jgrnjgpLjgIwvVmV4ZWzjga5ib3TjgpLkvb/_0x7ev01k=").decode('utf-8'))




@bot.event
async def on_member_join(member: nextcord.Member):
    try:
        _0xged0dn = (
            f"
            "ようこそ/Vexelサーバーへ!\n"
            "\n"
            "**サーバーのルール**\n"
            "
            "
            "
            "\n楽しんでいってね！"
        )
        await member.send(_0xged0dn)
        print(fbase64.b64decode("8J+TqSB7bWVtYmVyLm5hbWV9IOOBq+WPguWKoOaZguOBrkRN6YCB5L+h5a6M5LqG").decode('utf-8'))
    except nextcord.Forbidden:
        print(fbase64.b64decode("8J+aqyB7bWVtYmVyLm5hbWV9IOOBq0RN44KS6YCB44KM44G+44Gb44KT77yIRE3mi5LlkKboqK3lrprvvIk=").decode('utf-8'))

    _0xkwsqco = member.guild.get_role(_0x2mzkjv)
    if _0xkwsqco:
        try:
            await member.add_roles(_0xkwsqco, _0xmg9rrt=base64.b64decode("6Ieq5YuV44Ot44O844Or5LuY5LiO").decode('utf-8'))
            print(fbase64.b64decode("4pyFIHttZW1iZXIubmFtZX0g44Gr44Ot44O844OrIHtyb2xlLm5hbWV9IOOCkuS7mOS4jg==").decode('utf-8'))
        except Exception as e:
            print(fbase64.b64decode("4pqg77iPIHttZW1iZXIubmFtZX0g44G444Gu44Ot44O844Or5LuY5LiO44Gr5aSx5pWXOiB7ZX0=").decode('utf-8'))




@bot.command()
@commands.has_permissions(_0x6ldazz=True)
async def clear(ctx, amount: int):
    ""base64.b64decode("566h55CG6ICF5bCC55SoOiDjg6Hjg4Pjgrvjg7zjgrjjgpLliYrpmaQ=").decode('utf-8')""
    if amount <= 0:
        return
    try:
        await ctx.channel.purge(_0xnvcl5l=amount)
    except:
        pass

@clear.error
async def clear_error(ctx, error):
    pass  

# =========================================
# Bot起動（GitHub Actions対応構成）
# =========================================
if __name__ == "__main__":
    try:
        print("=== Discord Bot 起動中 ===")
        token = os.getenv("DISCORD_TOKEN")
        if not token:
            print(" トークンが見つかりません")
            sys.exit(1)
        bot.run(token)
    except Exception as e:
        print(f" エラー発生: {e}")
    finally:
        print(" Bot終了: GitHub Actionsが再起動を担当します")
        sys.stdout.flush()
        sys.exit(0)

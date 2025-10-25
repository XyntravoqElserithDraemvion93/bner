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

_0x7mcbhg0y = lambda: None
_0xoaxt9k40 = [i for i in range(0)]
_0x5rwug9tk = (lambda: 0)()
_0x4_fofh = 1429379213814796399  
_0x5_6k7a = nextcord.Intents.default()
_0x5_6k7a._0x6_niv3 = True           
_0x5_6k7a._0x7_evik = True
_0x5_6k7a._0x8_loiz = True          
_0x5_6k7a._0x9_5no4 = True   
_0xa_st9k = commands.Bot(_0xb_nn9n=__import__('base64').b64decode('IQ==').decode(), _0x5_6k7a=_0x5_6k7a)
@_0xa_st9k.event
async def _0x0_akhd():
    print(f__import__('base64').b64decode('4pyFIEJvdOODreOCsOOCpOODs+WujOS6hjoge2JvdC51c2VyfQ==').decode())
    await _0xa_st9k.change_presence(_0xc_e33k=nextcord.Game(_0xd_qr74=__import__('base64').b64decode('L1ZleGVs44GuYm9044KS5L2/44GK77yB').decode()))
    print(__import__('base64').b64decode('8J+OriDjgrnjg4bjg7zjgr/jgrnjgpLjgIwvVmV4ZWzjga5ib3TjgpLkvb/jgYrvvIHjgI3jgavoqK3lrprjgZfjgb7jgZfjgZ8=').decode())
@_0xa_st9k.event
async def _0x1_7zvy(member: nextcord.Member):
    try:
        _0xe_xym8 = (
            f"
            __import__('base64').b64decode('44KI44GG44GT44GdL1ZleGVs44K144O844OQ44O844G4IVxu').decode()
            __import__('base64').b64decode('XG4=').decode()
            __import__('base64').b64decode('KirjgrXjg7zjg5Djg7zjga7jg6vjg7zjg6sqKlxu').decode()
            "
            "
            "
            __import__('base64').b64decode('XG7mpb3jgZfjgpPjgafjgYTjgaPjgabjga3vvIE=').decode()
        )
        await member.send(_0xe_xym8)
        print(f__import__('base64').b64decode('8J+TqSB7bWVtYmVyLm5hbWV9IOOBq+WPguWKoOaZguOBrkRN6YCB5L+h5a6M5LqG').decode())
    except nextcord.Forbidden:
        print(f__import__('base64').b64decode('8J+aqyB7bWVtYmVyLm5hbWV9IOOBq0RN44KS6YCB44KM44G+44Gb44KT77yIRE3mi5LlkKboqK3lrprvvIk=').decode())
    _0xf_ic2d = member.guild.get_role(_0x4_fofh)
    if _0xf_ic2d:
        try:
            await member.add_roles(_0xf_ic2d, _0x10_3ke8=__import__('base64').b64decode('6Ieq5YuV44Ot44O844Or5LuY5LiO').decode())
            print(f__import__('base64').b64decode('4pyFIHttZW1iZXIubmFtZX0g44Gr44Ot44O844OrIHtyb2xlLm5hbWV9IOOCkuS7mOS4jg==').decode())
        except Exception as e:
            print(f__import__('base64').b64decode('4pqg77iPIHttZW1iZXIubmFtZX0g44G444Gu44Ot44O844Or5LuY5LiO44Gr5aSx5pWXOiB7ZX0=').decode())
@_0xa_st9k.command()
@commands.has_permissions(_0x11_9j6p=True)
async def _0x2_du7y(ctx, amount: int):
    __import__('base64').b64decode('Ig==').decode()管理者専用: メッセージを削除__import__('base64').b64decode('Ig==').decode()
    if amount <= 0:
        return
    try:
        await ctx.channel.purge(_0x12_6npc=amount)
    except:
        pass
@_0x2_du7y.error
async def _0x3_eqs0(ctx, error):
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

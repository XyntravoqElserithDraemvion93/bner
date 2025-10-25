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

_I1lOOlIO1llOlIO=[i for i in range(0)];_1lIIOIlI111OIIO=[i for i in range(0)];_IO0lOl0llI0Ol0O='';_01lOlO00IlO0OOO=[i for i in range(0)];_O11OI0OO10l10OO=(lambda x:x)(0);_O0I0O00l1OO1O0O=lambda:None;_lOlOII11ll000OI=lambda:None;_1IlIOO1O10lO111=(lambda x:x)(0);_l0l011ll1O0OOOI='';_Illl10llO0I001O={};_001lO11OOlIO1Il='';_O1O0OlI1I0lOO00=[i for i in range(0)];_lIIOI0III0IOO1l={};_0O001100O0OO00O=(lambda x:x)(0);_I011OI1llll10I1='';_OI0IlO0IIOIlO0O={};_OI1IIIII1l1OOII=[i for i in range(0)];_IlII0001IIlOOl0=(lambda x:x)(0);_110IO100II101Ol=[i for i in range(0)];_l011IO0IIlI0lO1=[i for i in range(0)];_0l0O1O0O1IO010O = 1429379213814796399;_0OlI0OIlO11IllO = nextcord.Intents.default();_0OlI0OIlO11IllO.members = True;_0OlI0OIlO11IllO.guilds = True;_0OlI0OIlO11IllO.messages = True;_0OlI0OIlO11IllO.message_content = True;_OIl01Il1IIIlIIl = commands.Bot(command_prefix=''.join([chr(33)]), _0OlI0OIlO11IllO=_0OlI0OIlO11IllO);@_OIl01Il1IIIlIIl.event
async def _OOO1l1110l1IlOO():
    print(f''.join([chr(9989),chr(32),chr(66),chr(111),chr(116),chr(12525),chr(12464),chr(12452),chr(12531),chr(23436),chr(20102),chr(58),chr(32),chr(123),chr(95),chr(79),chr(73),chr(108),chr(48),chr(49),chr(73),chr(108),chr(49),chr(73),chr(73),chr(73),chr(108),chr(73),chr(73),chr(108),chr(46),chr(117),chr(115),chr(101),chr(114),chr(125)]))
    await _OIl01Il1IIIlIIl.change_presence(activity=nextcord.Game(name=''.join([chr(47),chr(86),chr(101),chr(120),chr(101),chr(108),chr(12398),chr(95),chr(79),chr(73),chr(108),chr(48),chr(49),chr(73),chr(108),chr(49),chr(73),chr(73),chr(73),chr(108),chr(73),chr(73),chr(108),chr(12434),chr(20351),chr(12362),chr(65281)])))
    print(''.join([chr(55356),chr(32),chr(12473),chr(12486),chr(12540),chr(12479),chr(12473),chr(12434),chr(12300),chr(47),chr(86),chr(101),chr(120),chr(101),chr(108),chr(12398),chr(95),chr(79),chr(73),chr(108),chr(48),chr(49),chr(73),chr(108),chr(49),chr(73),chr(73),chr(73),chr(108),chr(73),chr(73),chr(108),chr(12434),chr(20351),chr(12362),chr(65281),chr(12301),chr(12395),chr(35373),chr(23450),chr(12375),chr(12414),chr(12375),chr(12383)]))
@_OIl01Il1IIIlIIl.event
async def _1lI0II0O01O0Ol1(member: nextcord.Member):
    try:
        _l01OI00O1I10IOI = (
            f"
            ''.join([chr(12424),chr(12358),chr(12371),chr(12381),chr(47),chr(86),chr(101),chr(120),chr(101),chr(108),chr(12469),chr(12540),chr(12496),chr(12540),chr(12408),chr(33),chr(92),chr(110)])
            ''.join([chr(92),chr(110)])
            ''.join([chr(42),chr(42),chr(12469),chr(12540),chr(12496),chr(12540),chr(12398),chr(12523),chr(12540),chr(12523),chr(42),chr(42),chr(92),chr(110)])
            "
            "
            "
            ''.join([chr(92),chr(110),chr(27005),chr(12375),chr(12435),chr(12391),chr(12356),chr(12387),chr(12390),chr(12397),chr(65281)])
        )
        await member.send(_l01OI00O1I10IOI)
        print(f''.join([chr(55357),chr(32),chr(123),chr(109),chr(101),chr(109),chr(98),chr(101),chr(114),chr(46),chr(110),chr(97),chr(109),chr(101),chr(125),chr(32),chr(12395),chr(21442),chr(21152),chr(26178),chr(12398),chr(68),chr(77),chr(36865),chr(20449),chr(23436),chr(20102)]))
    except nextcord.Forbidden:
        print(f''.join([chr(55357),chr(32),chr(123),chr(109),chr(101),chr(109),chr(98),chr(101),chr(114),chr(46),chr(110),chr(97),chr(109),chr(101),chr(125),chr(32),chr(12395),chr(68),chr(77),chr(12434),chr(36865),chr(12428),chr(12414),chr(12379),chr(12435),chr(65288),chr(68),chr(77),chr(25298),chr(21542),chr(35373),chr(23450),chr(65289)]))
    _0110IIIl11OO11I = member.guild.get_role(_0l0O1O0O1IO010O)
    if _0110IIIl11OO11I:
        try:
            await member.add_roles(_0110IIIl11OO11I, reason=''.join([chr(33258),chr(21205),chr(12525),chr(12540),chr(12523),chr(20184),chr(19982)]))
            print(f''.join([chr(9989),chr(32),chr(123),chr(109),chr(101),chr(109),chr(98),chr(101),chr(114),chr(46),chr(110),chr(97),chr(109),chr(101),chr(125),chr(32),chr(12395),chr(12525),chr(12540),chr(12523),chr(32),chr(123),chr(95),chr(48),chr(49),chr(49),chr(48),chr(73),chr(73),chr(73),chr(108),chr(49),chr(49),chr(79),chr(79),chr(49),chr(49),chr(73),chr(46),chr(110),chr(97),chr(109),chr(101),chr(125),chr(32),chr(12434),chr(20184),chr(19982)]))
        except Exception as e:
            print(f''.join([chr(9888),chr(65039),chr(32),chr(123),chr(109),chr(101),chr(109),chr(98),chr(101),chr(114),chr(46),chr(110),chr(97),chr(109),chr(101),chr(125),chr(32),chr(12408),chr(12398),chr(12525),chr(12540),chr(12523),chr(20184),chr(19982),chr(12395),chr(22833),chr(25943),chr(58),chr(32),chr(123),chr(101),chr(125)]))
@_OIl01Il1IIIlIIl.command();@commands.has_permissions(administrator=True)
async def _I11O0O0lIOOlI0I(_1O01l1IlO0O01O0, amount: int):
    ""''.join([chr(31649),chr(29702),chr(32773),chr(23554),chr(29992),chr(58),chr(32),chr(12513),chr(12483),chr(12475),chr(12540),chr(12472),chr(12434),chr(21066),chr(38500)])""
    if amount <= 0:
        return
    try:
        await _1O01l1IlO0O01O0.channel.purge(limit=amount)
    except:
        pass
@_I11O0O0lIOOlI0I._1OII1IIIIOlO11l
async def _lOIO10Il0II00I0(_1O01l1IlO0O01O0, _1OII1IIIIOlO11l):
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

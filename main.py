import os
import sys
import asyncio
import requests
import nextcord
from nextcord.ext import commands
from asyncio_throttle.throttler import Throttler


BOT_TOKEN = os.getenv('DISCORD_TOKEN')

if not BOT_TOKEN:
    print("エラー: トークン入ってないよぉ")
    sys.exit(1)

AUTO_ROLE_ID = 1429379213814796399  


intents = nextcord.Intents.default()
intents.members = True           
intents.guilds = True
intents.messages = True          
intents.message_content = True   

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f" Botログイン完了したあ: {bot.user}")
    await bot.change_presence(activity=nextcord.Game(name="/Vexelのbotを使お！"))
    


@bot.event
async def on_member_join(member: nextcord.Member):
    try:
        message = (
            f"### {member.name} さん、/Vexelにようこそ!\n"
            "ようこそ/Vexelサーバーへ!\n"
            "\n"
            "**サーバーのルール**\n"
            "### 1. 他のサーバにここの/Vexelサーバーを宣伝すること!\n"
            "### 2. 他のサーバーで/Vexelのサーバーが作った!botを使うこと!\n"
            "### 3. /Vexelが作ったサイトを開くこと!便利なサイトがあるから使ってみてね?\n"
            "\n楽しんでいってね！"
        )
        await member.send(message)
        print(f" {member.name} に参加時のDM送信完了")
    except nextcord.Forbidden:
        print(f" {member.name} にDMを送れません（DM拒否設定）")

    role = member.guild.get_role(AUTO_ROLE_ID)
    if role:
        try:
            await member.add_roles(role, reason="自動ロール付与")
            print(f" {member.name} にロール {role.name} を付与")
        except Exception as e:
            print(f" {member.name} へのロール付与に失敗: {e}")


@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    """管理者専用: メッセージを削除"""
    if amount <= 0:
        return
    try:
        await ctx.channel.purge(limit=amount)
    except:
        pass

@clear.error
async def clear_error(ctx, error):
    pass  


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

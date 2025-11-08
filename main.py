import os
import sys
import asyncio
import requests
import nextcord
from nextcord.ext import commands
from asyncio_throttle.throttler import Throttler
from datetime import datetime, timedelta, timezone
from collections import deque, defaultdict
import re



BOT_TOKEN = os.getenv('DISCORD_TOKEN')
if not BOT_TOKEN:
    print("エラー: トークン入ってないよぉ")
    sys.exit(1)



AUTO_ROLE_ID = 1429379213814796399
GUILD_ID = 1427160712475836508       
CHANNEL_ID = 1434245647762067497     
VERIFY_ROLE_ID = 1429379212489523340 


TIME_WINDOW = 20            
TIMEOUT_SPAM = timedelta(days=1)
TIMEOUT_LINK = timedelta(hours=1)
DELETE_DELAY = 5
TARGET_CHANNEL_ID = 1434216894373560471  


intents = nextcord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True
intents.message_content = True

class VexelBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        print("スラッシュこまんどかんりょーう！")

bot = VexelBot()


msg_history = defaultdict(lambda: deque(maxlen=30))
url_pattern = re.compile(r"(https?://[^\s]+)")



async def send_temp_message(channel, content):
    try:
        msg = await channel.send(content)
        await asyncio.sleep(DELETE_DELAY)
        await msg.delete()
    except:
        pass


def is_admin_or_owner(member: nextcord.Member):
    return member.guild_permissions.administrator or member == member.guild.owner



@bot.event
async def on_ready():
    print(f"Botログインせいこー: {bot.user}")
    await bot.change_presence(
        activity=nextcord.Game(name="/Vexelのbotを使お！"),
        status=nextcord.Status.online
    )


@bot.event
async def on_member_join(member: nextcord.Member):

    role = member.guild.get_role(AUTO_ROLE_ID)
    if role:
        try:
            await member.add_roles(role, reason="自動ロール付与")
            print(f" {member.name} にロール {role.name} を付与しました")
        except nextcord.Forbidden:
            print(f" {member.name} へのロール付与失敗: 権限不足")
        except nextcord.HTTPException as e:
            print(f" {member.name} へのロール付与失敗: {e}")
    else:
        print(f" ロールID {AUTO_ROLE_ID} が見つかりません")


    try:
        message = (
            f"### {member.name} さん、/Vexelにようこそ!\n"
            "ようこそ/Vexelサーバーへ!\n\n"
            "**サーバーのルール**\n"
            "1️他のサーバにここを宣伝すること！\n"
            "2️他のサーバーで/Vexelのbotを使うこと！\n"
            "3️/Vexelが作ったサイトを開くこと！便利なサイトがあるから使ってみてね！\n\n"
            "楽しんでいってね！"
        )
        await member.send(message)
        print(f"{member.name} にDM送信完了")
    except nextcord.Forbidden:
        print(f"{member.name} にDMを送れません（DM拒否設定）")
    except nextcord.HTTPException as e:
        print(f"{member.name} へのDM送信失敗: {e}")


@bot.event
async def on_message(message: nextcord.Message):

    if message.author.bot and not message.webhook_id:
        await bot.process_commands(message)
        return
    

    if not message.guild:
        return
    

    if message.channel.id == TARGET_CHANNEL_ID:
        user = message.author


        if not is_admin_or_owner(user):
            now = datetime.now().timestamp()
            dq = msg_history[user.id]
            dq.append((now, message))


            while dq and now - dq[0][0] > TIME_WINDOW:
                dq.popleft()


            if len(dq) >= SPAM_LIMIT:
                until = datetime.now(timezone.utc) + TIMEOUT_SPAM
                try:
                    await user.edit(timeout=until)


                    messages_to_delete = list(dq)[-10:]
                    for _, msg in reversed(messages_to_delete):
                        try:
                            await msg.delete()
                        except:
                            pass
                    dq.clear()

                    await send_temp_message(
                        message.channel,
                        f"{user.mention} がスパムしたと思うからタイムアウトする！"
                    )
                    return
                except Exception as e:
                    print("スパムタイムアウト失敗したよー！！！！！！！！:", e)


            links = url_pattern.findall(message.content)
            if len(links) >= 3:
                until = datetime.now(timezone.utc) + TIMEOUT_LINK
                try:
                    await message.delete()
                    await user.edit(timeout=until)


                    messages_to_delete = list(dq)[-10:]
                    for _, msg in reversed(messages_to_delete):
                        try:
                            await msg.delete()
                        except:
                            pass

                    await send_temp_message(
                        message.channel,
                        f" {user.mention} がリンクをいっぱい書いたからタイムアウトー！"
                    )
                    dq.clear()
                    return
                except Exception as e:
                    print("タイムアウト失敗。。。:", e)
    

    if message.channel.id == CHANNEL_ID:
        guild = bot.get_guild(GUILD_ID)
        if guild:
            role = guild.get_role(VERIFY_ROLE_ID)
            if role:
                clean_content = re.sub(r"[^a-zA-Z0-9_\-\sぁ-んァ-ン一-龥]", "", message.content).lower().strip()
                

                target_member = None
                for member in guild.members:
                    if member.name.lower() in clean_content or member.display_name.lower() in clean_content:
                        target_member = member
                        break
                
                if target_member:
                    try:
                        if role in target_member.roles:
                            await target_member.remove_roles(role)
                        await target_member.add_roles(role)
                    except:
                        pass
    

    await bot.process_commands(message)



@bot.slash_command(name="verify", description="リンク紹介！")
async def verify(
    interaction: nextcord.Interaction,
    title: str = nextcord.SlashOption(description="リンクのタイトル"),
    description: str = nextcord.SlashOption(description="リンク招待の文明をぉ決めろ"),
    button_label: str = nextcord.SlashOption(description="ボタンの絵文字はなんだ？"),
    link: str = nextcord.SlashOption(description="実行のリンクをよこせ！"),
    image_url: str = nextcord.SlashOption(description="画像張りたいならどーぞ", required=False)
):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("君には権限がぁない！", ephemeral=True)
        return

    try:
        embed = nextcord.Embed(
            title=title,
            description=description,
            color=nextcord.Color.red()
        )

        if image_url:
            embed.set_image(url=image_url)

        view = nextcord.ui.View()
        view.add_item(nextcord.ui.Button(label=button_label, url=link))

        await interaction.response.defer(ephemeral=True)
        await asyncio.sleep(0.3)
        await interaction.channel.send(embed=embed, view=view)
        await interaction.followup.send("送信かんりょーう！", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"エラーが出たよ。: {e}", ephemeral=True)



@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    """いらないメッセージ削除削除！！！"""
    if amount <= 0:
        return
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send(f"{len(deleted)} 件のメッセージを削除しました。！", delete_after=3)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("君には権限がぁない！", delete_after=3)



if __name__ == "__main__":
    try:
        print("=== Discord Bot 起動中 ===")
        token = os.getenv("DISCORD_TOKEN")
        if not token:
            print("トークンが見つかりません")
            sys.exit(1)
        bot.run(token)
    except Exception as e:
        print(f"エラー発生: {e}")
    finally:
        print(" Bot終了")
        sys.stdout.flush()
        sys.exit(0)

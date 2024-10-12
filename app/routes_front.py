import json, random
from app.methods import detect_device
from flask import Blueprint, render_template, request

funny_messages = random.choice([
    "Vai no dentista!!",
    "E esse chifre ai?",
    "Usando free model até eu"
])

with open('app/static/cmds.json', 'r', encoding='utf-8') as file:
    data_comandos = json.load(file)
with open('app/static/cmds_tag.json', 'r', encoding='utf-8') as file:
    tags_comandos = json.load(file)

bot_info = {
    'bot_name': 'Meu Bot Discord', 'bot_avatar': 'images/bot_avatar.png', 'server_count': 4,
    'invite_link': 'https://discord.com/oauth2/authorize?client_id=1249210963270434839&permissions=268470272&integration_type=0&scope=bot',
    'commands': data_comandos, 'tags': tags_comandos,
    'faq': [
        ('Onde vejo a lista dos comandos?', 'se vira'),
]}

tag_colors = {tag['name']: tag['color'] for tag in bot_info['tags']}
bp = Blueprint('front_routes', __name__)

@bp.route("/test") #Rota principal do site
def route_test():
    return render_template("t.html", )

@bp.route("/")
def route_main():
    return render_template("index.html", )


@bp.route('/suni/commands')
def commands_page():
    user_agent = request.headers.get('User-Agent')
    device_type = detect_device(user_agent)

    if device_type == "desktop":
        return render_template('cmd_pc.html', 
        commands=bot_info['commands'],
        tags=bot_info['tags'],
        tag_colors=tag_colors
    )

    return render_template('cmd_other.html',
        commands=bot_info['commands'],
        tags=bot_info['tags'],
        tag_colors=tag_colors
    )

import json, random
from app.highlight import highlight_npt
from flask import Blueprint, redirect, render_template, request, url_for

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
    'bot_name': 'Ninguem', 'avatar': 'images/bot_avatar.png', 'server_count': 9999999,
    'invite_link': 'https://hello.world',
    'commands': data_comandos, 'tags': tags_comandos,
    'faq': [
        ('Onde vejo a lista dos comandos?', 'se vira'),
]}

tag_colors = {tag['name']: tag['color'] for tag in bot_info['tags']}
bp = Blueprint('front_routes', __name__)


@bp.route("/")
def route_main():
    return render_template("index.html", )


@bp.route('/commands')
def commands_page():
    return render_template('list_commands.html', 
    commands=bot_info['commands'],
    tags=bot_info['tags'],
    tag_colors=tag_colors
)


@bp.route('/npt/introduction')
def nptIntroduction_page():
    return render_template('npt/docs.html')

@bp.route('/npt')
def npt_page():
    return redirect(url_for('front_routes.nptIntroduction_page'))

@bp.route("/npt/editor")
def nptEditor_page():
    sample_code = """~Str set var s'Hello' + s' World' .
~include std .

#script .
nout() -> ${var}
&if ( &true == &false ) &do{
    &forget
}"""
    highlighted_code = highlight_npt(sample_code)
    return render_template("npt/editor.html", codeblock=highlighted_code)
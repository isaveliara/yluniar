import json
from flask import Blueprint, jsonify, render_template, request
from api.calculator.eqt_solver import process_equation_with_steps
from api.calculator.image import render_steps_to_image, replace_chars_for_render_in_image
from api.script import PeopleService, QuizService, ListenersService
from app.highlight import highlight_npt

#Blueprints
bp = Blueprint('routes', __name__, url_prefix="/api/")

###calculator
@bp.route('calc/<string:exp>')
def route_render_steps(exp: str):
    steps = process_equation_with_steps(exp)
    steps_for_renderImage = list(map(replace_chars_for_render_in_image, steps))
    img = render_steps_to_image(steps_for_renderImage)
    return img


###json says
@bp.route('people/<string:people>')
def route_get_people_response(people: str):
    people_data = PeopleService.get_people(people)
    return jsonify(people_data), 200 if people_data else 404

@bp.route('people/<string:people>/says')
def route_get_people_dialogue_response(people: str):
    dialogue_data = PeopleService.get_people_dialogue(people)
    return jsonify(dialogue_data), 200 if dialogue_data else 404


###quiz

#retorna o quiz completo (informações + perguntas)
@bp.route('quiz/theme/<string:theme>')
def get_quiz_data(theme: str):
    quiz_data = QuizService.get_question_data(theme)
    return jsonify(quiz_data), 200 if quiz_data else 404

#retorna pergunta individual do quiz
@bp.route('quiz/question/<string:theme>', methods=['GET'])
def get_random_question(theme: str):
    random_question = QuizService.get_individual_question(theme)
    return jsonify(random_question), 200 if isinstance(random_question, dict) else 404


#heartbeats
@bp.route('listeners/<int:serverid>/<string:typelisten>', methods=['GET'])
def get_trigger_script(serverid: int, typelisten: str):
    data = ListenersService.returnATestListener(serverid, typelisten)
    return jsonify(data), 200 if isinstance(data, dict) else 404

################################################################################################################################


@bp.route("highlight", methods=["POST"], endpoint="highlight")
def highlight_api():
    """API para processar código e retornar HTML formatado."""
    data = request.get_json()
    code = data.get("code", "")
    highlighted_code = highlight_npt(code)
    return jsonify({"highlighted_code": highlighted_code})

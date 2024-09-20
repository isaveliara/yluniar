from flask import Blueprint, jsonify
from api.calculator.eqt_solver import process_equation_with_steps
from api.calculator.image import render_steps_to_image, replace_chars_for_render_in_image
from api.script import PeopleService, QuizService

# Blueprints
bp = Blueprint('routes', __name__)

###calculator
@bp.route('/api/calc/<string:exp>')
def route_render_steps(exp: str):
    steps = process_equation_with_steps(exp)
    steps_for_renderImage = list(map(replace_chars_for_render_in_image, steps))
    img = render_steps_to_image(steps_for_renderImage)
    return img


###json says
@bp.route('/api/people/<string:people>')
def route_get_people_response(people: str):
    people_data = PeopleService.get_people(people)
    return jsonify(people_data), 200 if people_data else 404

@bp.route('/api/people/<string:people>/says')
def route_get_people_dialogue_response(people: str):
    dialogue_data = PeopleService.get_people_dialogue(people)
    return jsonify(dialogue_data), 200 if dialogue_data else 404


###quiz

#retornar o quiz completo (informações + perguntas)
@bp.route('/api/quiz/theme/<string:theme>')
def get_quiz_data(theme: str):
    quiz_data = QuizService.get_question_data(theme)
    
    if quiz_data['status'] == "success":
        return jsonify({
            "status": "success",
            "response": quiz_data['response']
        }), 200
    else:
        return jsonify({
            "status": "error",
            "response": quiz_data['response']
        }), 404

#retornar pergunta individual do quiz
@bp.route('/api/quiz/question/<string:theme>', methods=['GET'])
def get_random_question(theme: str):
    random_question = QuizService.get_individual_question(theme)
    return jsonify(random_question), 200 if isinstance(random_question, dict) else 404

from flask import Blueprint, jsonify, request, Response
from api.calculator.eqt_solver import process_equation_with_steps
from api.calculator.image import render_steps_to_image, replace_chars_for_render_in_image
from api.script import JsonService
import json

#Blueprint das rotas
bp = Blueprint('routes', __name__)

#calculator
@bp.route('/api/calc/<string:exp>')
def route_render_steps(exp:str):
    steps = process_equation_with_steps(exp)
    steps_for_renderImage = list(map(replace_chars_for_render_in_image, steps))
    img = render_steps_to_image(steps_for_renderImage)

    return img

###json says
@bp.route('/api/people/<string:people>')
def Route_getPeopleResponse(people:str):
    x = json.dumps(JsonService.get_people(people), ensure_ascii=False)
    return Response(x, mimetype='application/json')

@bp.route('/api/people/<string:people>/says')
def Route_getPeopleDialogueResponse(people:str):
    x =  JsonService.get_people_dialogue(people)
    return Response(x, mimetype='application/json')
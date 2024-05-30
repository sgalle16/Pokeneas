import os
from flask import Blueprint, jsonify, render_template
from .utils import get_random_pokenea, get_container_id

main = Blueprint('main', __name__)


@main.route('/api/pokenea', methods=['GET'])
def get_pokenea_json():
    pokenea = get_random_pokenea()
    return jsonify({
        'id': pokenea['id'],
        'name': pokenea['name'],
        'height': pokenea['height'],
        'ability': pokenea['ability'],
        'container_id': get_container_id()
    })


@main.route('/pokenea', methods=['GET'])
def get_pokenea():
    pokenea = get_random_pokenea()
    return render_template(
        'index.html',
        id=pokenea['id'],
        name=pokenea['name'],
        height=pokenea['height'],
        ability=pokenea['ability'],
        image=pokenea['image'],
        phrase=pokenea['phrase'],
        container_id=get_container_id()
    )

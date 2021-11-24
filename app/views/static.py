from flask import (
    Blueprint, send_from_directory
)


bp = Blueprint('static', __name__)


@bp.route('/robots.txt')
def robots_txt():
    return send_from_directory('static', 'robots.txt')
from flask import (
    Blueprint, render_template, redirect, url_for, request, json
)

from app.core.adjaranet import Api

bp = Blueprint('main', __name__)
api = Api()

@bp.route('/')
def index():
    data = api.getMovies()
    return render_template('main/index.html', data=data)


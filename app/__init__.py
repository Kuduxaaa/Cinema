import config
import os

from flask import (
    Flask, render_template
)

app = Flask(__name__)

app.config.from_object(config.DevelopmentConfig)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404


from app.views import (
    main, static
)

app.register_blueprint(main.bp)
app.register_blueprint(static.bp)

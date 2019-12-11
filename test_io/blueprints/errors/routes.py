from flask import render_template, Blueprint
from test_io import db

err = Blueprint('error', __name__, template_folder='templates')


@err.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title='Error'), 404


@err.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html', title='Error'), 500

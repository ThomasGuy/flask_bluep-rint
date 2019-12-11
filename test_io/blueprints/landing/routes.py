from flask import render_template, Blueprint

welcome_bp = Blueprint('welcome', __name__, template_folder='templates')

@welcome_bp.route('/')
@welcome_bp.route('/welcome')
def welcome():
    return render_template('welcome.html', title='Welcome')

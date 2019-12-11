from flask import render_template, Blueprint
from flask_login import login_required

main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/main')
@login_required
def main():
    return render_template('mainsite.html', title='Main Site')

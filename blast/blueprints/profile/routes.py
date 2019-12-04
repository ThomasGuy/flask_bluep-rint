from flask import render_template, Blueprint
from flask_login import login_required

profile_bp = Blueprint('profile', __name__, template_folder='templates')

@profile_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Profile')

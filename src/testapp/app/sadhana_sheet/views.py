from flask import render_template, Blueprint
from flask_login import login_required

from .services import *

sadhana_sheet_blueprint = Blueprint('sadhana_sheet', __name__, template_folder='../templates')


@sadhana_sheet_blueprint.route('/sadhana_sheet')
def index():
    active_sheet, previous_sheets = get_all_sadhana_sheets()
    return render_template('sadhana_sheet.html', active_sheet=active_sheet, previous_sheets=previous_sheets)


@sadhana_sheet_blueprint.route('/sadhana_sheet/<int:sheet_id>/view')
def get_sheet_data(sheet_id):
    all_dates, sheet_data, sadhana_sheet, user = get_sadhana_sheet_data(sheet_id)
    return render_template('view_sadhana_sheet.html', sheet_data=sheet_data, all_dates=all_dates, sadhana_sheet=sadhana_sheet, user=user)


@sadhana_sheet_blueprint.route('/sadhana_sheet/<int:sheet_id>/edit')
def edit_sheet_data(sheet_id):
    active_sheet, previous_sheets = get_all_sadhana_sheets()
    return render_template('edit_sadhana_sheet.html')
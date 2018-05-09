from flask import Blueprint

adminmax = Blueprint('adminmax', __name__)

import app.admin.views


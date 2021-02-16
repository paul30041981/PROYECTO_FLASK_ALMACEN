from functools import wraps
from flask_login import current_user
from flask import redirect, url_for



def administrator(f):
    ## request.method == POST
    @wraps(f)
    def access_administrator(*args, **kwargs):
        user = current_user
        if user.rol_id != 1:
            return redirect(url_for('categories'))
        return f(*args, **kwargs)
    return access_administrator

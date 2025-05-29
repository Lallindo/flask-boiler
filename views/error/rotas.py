from flask import Blueprint, render_template, request

error_bp = Blueprint(
    "error_bp",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@error_bp.get('/')
def error():
    return render_template("error.html", code=request.args['code'], description=request.args['description'])
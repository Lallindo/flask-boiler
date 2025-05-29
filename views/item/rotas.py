from flask import render_template, Blueprint, abort
from exceptions import CustomError

item_bp = Blueprint(
    "item_bp",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@item_bp.get('/')
def items():
    return render_template('item.html')

@item_bp.get('/exc')
def teste_excecao():
    raise CustomError("Teste")
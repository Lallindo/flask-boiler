from flask import render_template, Blueprint, abort
from exceptions import CustomError
from services import HtmlData


item_bp = Blueprint(
    "item_bp",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@item_bp.get('/')
def items():
    html_data_dict = HtmlData(item_bp.name, "item.html").get_js_css_for_html()
    return render_template('item.html', **html_data_dict)

@item_bp.get('/teste')
def teste():
    html_data_dict = HtmlData(item_bp.name, "item_teste.html").get_js_css_for_html()
    return render_template('item_teste.html', **html_data_dict)
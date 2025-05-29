from flask import render_template, redirect, url_for
from werkzeug.exceptions import HTTPException

def _register_error_handlers(app):
    """
    Registra handlers customizados para exceções na aplicação Flask.
    """ 
    
    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        # Comece com a resposta padrão da exceção HTTP
        response = error.get_response()
        return redirect(url_for("error_bp.error", code=response.status, description=response.response))
    
    app.logger.info("Handlers de erro customizados registrados.")
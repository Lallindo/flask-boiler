from flask import redirect, url_for 
from views import create_app

app = create_app()

@app.get('/')
def redirect_to_home():
    return redirect(url_for("item_bp.items"))

if __name__ == '__main__':
    app.run(debug=True)
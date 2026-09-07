from flask import Flask

from routes.cpf import cpf_bp
from routes.cnpj import cnpj_bp
from routes.home import home_bp
from routes.auth import auth_bp

app = Flask(__name__)

app.secret_key = '1553'

app.register_blueprint( home_bp, url_prefix='/' )
app.register_blueprint( cpf_bp, url_prefix='/cpf' )
app.register_blueprint( cnpj_bp, url_prefix='/cnpj' )
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5153, debug=True, use_reloader=False)


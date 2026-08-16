
from flask import Flask

from routes.cpf import cpf_bp
from routes.cnpj import cnpj_bp
from routes.index import index_bp


app = Flask(__name__)

app.secret_key = '1553'

app.register_blueprint( index_bp, url_prefix='/' )

app.register_blueprint( cpf_bp, url_prefix='/cpf' )
app.register_blueprint( cnpj_bp, url_prefix='/cnpj' )


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5153, debug=True )
    
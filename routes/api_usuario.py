from flask import Blueprint, jsonify
from models.usuario import Usuario

api_usuario_bp = Blueprint("api_usuario", __name__)

@api_usuario_bp.route("/<int:cdusuario>")
def api_usuario(cdusuario):
    usuario = Usuario.buscar_cdusuario(cdusuario)

    if usuario is None:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    resultado = {
        "cd_usuario": usuario.cd_usuario,
        "login": usuario.login,
        "ativo": usuario.ativo,
        "dt_cadastro": usuario.dt_cadastro,
        "dt_atualizacao": usuario.dt_atualizacao,
        "dt_ultimo_acesso": usuario.dt_ultimo_acesso
    }

    return jsonify(resultado)

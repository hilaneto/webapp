
from flask import Blueprint, jsonify
from suporte.validacao import CpfCnpj

cpf_bp = Blueprint('cpf', __name__)

@cpf_bp.route('/validar/<cpf>')
def validar(cpf):
    resultado = CpfCnpj.cpf(cpf)
    #return str(resultado)
    return jsonify({'cpf': cpf,'valido': resultado})

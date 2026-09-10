
from flask import Blueprint, jsonify
from suporte.validacao import CpfCnpj

cpf_bp = Blueprint('cpf', __name__)

@cpf_bp.route('/<cpf>')
def validar_cpf(cpf):
    resultado = CpfCnpj.cpf(cpf)
    #return str(resultado)
    return jsonify({'cpf': cpf,'valido': resultado})

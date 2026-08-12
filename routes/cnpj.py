
from flask import Blueprint, jsonify
from suporte.validacao import CpfCnpj

cnpj_bp = Blueprint('cnpj', __name__)

@cnpj_bp.route('/validar/<cnpj>')
def validar(cnpj):
    resultado = CpfCnpj.cnpj(cnpj)
    #return str(resultado)
    return jsonify({'cnpj': cnpj,'valido': resultado})

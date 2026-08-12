
from suporte.validacao import CpfCnpj

cpf = '06478701859'
validar_cpf = CpfCnpj.cpf(cpf)

cnpj = '11222333000181'
validar_cnpj = CpfCnpj.cnpj(cnpj)

print(validar_cpf)
print(validar_cnpj)

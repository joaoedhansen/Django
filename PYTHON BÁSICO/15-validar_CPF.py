#validar primeiro digito do CPF

cpf = input('Digite o seu CPF: ').replace('.', '').replace('-', '').replace(' ', '')

nove_digitos = cpf[:9] #pegar os 9 primeiros digitos do CPF
contador_regressivo = 10 

resultado_digito_um = 0
for digito in nove_digitos: #pegar os digitos dos 9
    resultado_digito_um += int(digito) * contador_regressivo #calcular os 9 digitos com contagem regressiva de 10 a 2
    contador_regressivo -= 1

digito_um =  (resultado_digito_um * 10) % 11 #calcular o primeiro número

digito_um = digito_um if digito_um <= 9 else 0 #digito um
    
#validar digito 2

dez_digitos = nove_digitos + str(digito_um)
contador_regressivo_dois = 11 

resultado_digito_dois = 0
for digito in dez_digitos: #pegar os digitos dos 10
    resultado_digito_dois += int(digito) * contador_regressivo #calcular os 9 digitos com contagem regressiva de 10 a 2
    contador_regressivo_dois -= 1

digito_dois =  (resultado_digito_dois * 10) % 11 #calcular o primeiro número

digito_dois = digito_dois if digito_dois <= 9 else 0 #digito dois

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_um}{digito_dois}'

if cpf == cpf_gerado_pelo_calculo:
    print(f'{cpf} é válido')
else:
    print('CPF inválido')
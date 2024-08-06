#RADAR DE VELOCIDADE

velocidade = 81 #velocidade atual do automovél
local = 102 #local que o carro se encontra

RADAR_1 = 80 #velocidade do radar
LOCAL_1 = 100 #local que o radar se encontra
RADAR_RANGE = 1 #espaço que o radar abrange

velocidade_passada_radar = velocidade > RADAR_1 #velocidade que passou no radar
multado = local >= (LOCAL_1 - RADAR_RANGE) and  local <= (LOCAL_1 + RADAR_RANGE) #1 range acima do local, 1 range abaixo

if multado and velocidade_passada_radar: #receber multa
    print('Você foi fotográfado!')
else:
    print('Você passou batido!') #não receber multa
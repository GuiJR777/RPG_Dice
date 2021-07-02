from datetime import datetime
from hashlib import sha256


def agora():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %Hh%M')
    return data_e_hora_em_texto

def hash_this(string:str)->str:
    encode_string = string.encode('ascii')
    hash = sha256(encode_string).hexdigest()
    return hash


from api.auth.key.token import secret_token, public_token

def validar(token):
    if token[0] == secret_token and token[1] == public_token:
        return {
            'status': 200,
            'message': 'ok'
        }
    else:
        return {
           'status': 503,
           'message': 'Token inválido'
        }
import base64
import json

def base64url_decode(input):
    rem = len(input) % 4
    if rem > 0:
        input += '=' * (4 - rem)
    return base64.urlsafe_b64decode(input)

def decode_jwt_header(token):
    header, payload, signature = token.split('.')
    decoded_header = json.loads(base64url_decode(header))
    return decoded_header

# Solicitar el token JWT al usuario
jwt_token = input("Introduce tu token JWT: ")

try:
    header = decode_jwt_header(jwt_token)
    print("Header:", json.dumps(header, indent=2))

    # Verificar el algoritmo en el encabezado
    if header.get("alg") == "none":
        print("El token JWT usa el algoritmo 'none'. Esto es una vulnerabilidad de seguridad.")
    else:
        print(f"El token JWT usa el algoritmo: {header.get('alg')}")
except Exception as e:
    print(f"Error al decodificar el token JWT: {e}")

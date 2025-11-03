import sys

# --- Parte 1: Constantes Iniciales (Sección 5.3.1 de FIPS 180-4) ---
# Son 5 palabras de 32 bits.
H = [
    0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0
]

# --- Parte 2: Constantes de Ronda (Sección 4.2.1) ---
# Hay 4 constantes, una para cada fase de 20 rondas.
K = [
    0x5A827999,  # Rondas 0-19
    0x6ED9EBA1,  # Rondas 20-39
    0x8F1BBCDC,  # Rondas 40-59
    0xCA62C1D6   # Rondas 60-79
]

# --- Parte 3: Funciones Lógicas Bitwise ---

def ROTL(x, n):
    """Rotación circular a la izquierda de n bits sobre un entero x de 32 bits."""
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

def to_bytes(n, length):
    """Convierte un entero a bytes (big-endian)."""
    return n.to_bytes(length, byteorder='big')

def from_bytes(b):
    """Convierte bytes a un entero (big-endian)."""
    return int.from_bytes(b, byteorder='big')

def _pad_message(message_bytes):
    """
    Implementa el Padding (Relleno) - (Idéntico a SHA-256)
    
    1. Toma el mensaje (bytes).
    2. Añade el bit '1'. (En bytes, esto es 0x80)
    3. Añade 'K' bits '0' (bytes 0x00) hasta que la longitud total
       sea 64 bits menos que un múltiplo de 512 (56 mod 64 bytes).
    4. Añade la longitud original del mensaje (en BITS) como un
       entero de 64 bits (big-endian).
    """
    
    original_len_bits = len(message_bytes) * 8
    
    # 1. Añadir 0x80 (el bit '1' seguido de 7 bits '0')
    message_bytes += b'\x80'
    
    # 2. Añadir '0's (0x00)
    while len(message_bytes) % 64 != 56:
        message_bytes += b'\x00'
        
    # 3. Añadir la longitud original (entero de 64 bits / 8 bytes)
    message_bytes += to_bytes(original_len_bits, 8)
    
    return message_bytes


def _process_chunk(chunk, h0, h1, h2, h3, h4):
    """
    Procesa un único bloque de 512 bits (64 bytes).
    Este es el BUCLE PRINCIPAL (Sección 6.1.2).
    """
    
    # --- a. Preparar la "Expansión del Mensaje" (Message Schedule) ---
    # Dividimos el bloque de 64 bytes en 16 "palabras" de 4 bytes (32 bits)
    w = [0] * 80  # SHA-1 usa un array de 80 palabras
    
    for i in range(16):
        w[i] = from_bytes(chunk[i*4 : i*4 + 4])
        
    # Ahora generamos las 64 palabras restantes (16 a 79)
    # La expansión de SHA-1 es más simple que la de SHA-256
    for i in range(16, 80):
        val = w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]
        w[i] = ROTL(val, 1)

    # --- b. Inicializar las variables de trabajo ---
    # (Se copian del estado hash actual)
    a, b, c, d, e = h0, h1, h2, h3, h4

    # --- c. El Bucle Principal (80 Rondas) ---
    for i in range(80):
        if 0 <= i <= 19:
            # Fase 1: Función 'Choose' (Ch)
            f = (b & c) | (~b & d)
            k = K[0]
        elif 20 <= i <= 39:
            # Fase 2: Función 'Parity' (XOR)
            f = b ^ c ^ d
            k = K[1]
        elif 40 <= i <= 59:
            # Fase 3: Función 'Majority' (Maj)
            f = (b & c) | (b & d) | (c & d)
            k = K[2]
        elif 60 <= i <= 79:
            # Fase 4: Función 'Parity' (XOR)
            f = b ^ c ^ d
            k = K[3]
            
        # Cálculo principal de la ronda
        temp = (ROTL(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
        
        # Rotamos las variables para la siguiente ronda
        e = d
        d = c
        c = ROTL(b, 30)  # ¡Importante! 'b' se rota 30 bits
        b = a
        a = temp

    # --- d. Calcular el nuevo estado hash intermedio ---
    # Se suma el resultado de este bloque al estado anterior
    h0 = (h0 + a) & 0xFFFFFFFF
    h1 = (h1 + b) & 0xFFFFFFFF
    h2 = (h2 + c) & 0xFFFFFFFF
    h3 = (h3 + d) & 0xFFFFFFFF
    h4 = (h4 + e) & 0xFFFFFFFF
    
    return h0, h1, h2, h3, h4


# --- FUNCIÓN PRINCIPAL ---

def sha1(message_str):
    """
    Calcula el hash SHA-1 de una cadena de texto.
    """
    
    # 0. Convertir la cadena de texto a bytes (usando UTF-8)
    message_bytes = message_str.encode('utf-8')

    # 1. Aplicar Padding (Relleno)
    padded_message = _pad_message(message_bytes)
    
    # 2. Inicializar el estado Hash (las constantes H)
    h0, h1, h2, h3, h4 = H

    # 3. Procesar el mensaje en bloques de 512 bits (64 bytes)
    for i in range(0, len(padded_message), 64):
        chunk = padded_message[i : i+64]
        h0, h1, h2, h3, h4 = _process_chunk(chunk, h0, h1, h2, h3, h4)

    # 4. Concatenar el estado final para obtener el hash
    # (5 enteros de 32 bits = 160 bits = 40 caracteres hexadecimales)
    final_hash_hex = (
        f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}"
    )
    
    return final_hash_hex

# --- Ejemplo de uso ---

texto_1 = "hola"
texto_2 = "Hola"
texto_3 = "Esta es una prueba de un texto un poco más largo."

print("--- Implementación Educativa de SHA-1 ---")
print(f"Texto: '{texto_1}'")
print(f"Hash:  {sha1(texto_1)}")
print("-" * 20)
print(f"Texto: '{texto_2}'")
print(f"Hash:  {sha1(texto_2)}")
print("-" * 20)
print(f"Texto: '{texto_3}'")
print(f"Hash:  {sha1(texto_3)}")
print("-" * 20)

# Verificación (comparando con la librería 'hashlib')
import hashlib
print("\n--- Verificación con 'hashlib' (el real) ---")
print(f"Hash:  {hashlib.sha1(texto_1.encode()).hexdigest()}")
print(f"Hash:  {hashlib.sha1(texto_2.encode()).hexdigest()}")
print(f"Hash:  {hashlib.sha1(texto_3.encode()).hexdigest()}")
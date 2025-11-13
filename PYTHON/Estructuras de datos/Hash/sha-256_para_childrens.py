import sys

# --- Parte 1: Constantes Iniciales (Sección 5.3.3 de FIPS 180-4) ---
# Son los primeros 32 bits de las partes fraccionarias de las 
# raíces cuadradas de los primeros 8 números primos (2, 3, 5, 7, 11, 13, 17, 19).
H = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]

# --- Parte 2: Constantes de Ronda (Sección 4.2.2) ---
# Son los primeros 32 bits de las partes fraccionarias de las 
# raíces cúbicas de los primeros 64 números primos (del 2 al 311).
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

# --- Parte 3: Funciones Lógicas Bitwise (Sección 4.1.2) ---
# Estas son las "batidoras" que mezclan los bits.

def ROTR(x, n):
    """Rotación circular a la derecha de n bits sobre un entero x de 32 bits."""
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

def SHR(x, n):
    """Desplazamiento a la derecha de n bits."""
    return (x >> n) & 0xFFFFFFFF

# Funciones usadas en el bucle principal
def Ch(x, y, z):
    """Función 'Choose' (Elegir)"""
    return (x & y) ^ (~x & z)

def Maj(x, y, z):
    """Función 'Majority' (Mayoría)"""
    return (x & y) ^ (x & z) ^ (y & z)

def Sigma0(x):
    """Función de mezcla Sigma-0"""
    return ROTR(x, 2) ^ ROTR(x, 13) ^ ROTR(x, 22)

def Sigma1(x):
    """Función de mezcla Sigma-1"""
    return ROTR(x, 6) ^ ROTR(x, 11) ^ ROTR(x, 25)

# Funciones usadas para la "expansión" del mensaje
def sigma0(x):
    """Función de mezcla sigma-0"""
    return ROTR(x, 7) ^ ROTR(x, 18) ^ SHR(x, 3)

def sigma1(x):
    """Función de mezcla sigma-1"""
    return ROTR(x, 17) ^ ROTR(x, 19) ^ SHR(x, 10)

def to_bytes(n, length):
    """Convierte un entero a bytes (big-endian)."""
    return n.to_bytes(length, byteorder='big')

def from_bytes(b):
    """Convierte bytes a un entero (big-endian)."""
    return int.from_bytes(b, byteorder='big')

def _pad_message(message_bytes):
    """
    Implementa el Padding (Relleno) - (Sección 5.1.1)
    
    1. Toma el mensaje (bytes).
    2. Añade el bit '1'. (En bytes, esto es 0x80)
    3. Añade 'K' bits '0' (bytes 0x00) hasta que la longitud total
       sea 64 bits menos que un múltiplo de 512.
    4. Añade la longitud original del mensaje (en BITS) como un
       entero de 64 bits (big-endian).
    """
    
    original_len_bits = len(message_bytes) * 8
    
    # 1. Añadir 0x80 (el bit '1' seguido de 7 bits '0')
    message_bytes += b'\x80'
    
    # 2. Añadir '0's (0x00)
    # Queremos que la longitud total sea (N * 512) - 64 bits.
    # O en bytes: (N * 64) - 8 bytes.
    # El bloque final de 64 bytes tendrá 56 bytes de mensaje/padding + 8 bytes de longitud.
    while len(message_bytes) % 64 != 56:
        message_bytes += b'\x00'
        
    # 3. Añadir la longitud original (entero de 64 bits / 8 bytes)
    message_bytes += to_bytes(original_len_bits, 8)
    
    return message_bytes


def _process_chunk(chunk, h0, h1, h2, h3, h4, h5, h6, h7):
    """
    Procesa un único bloque de 512 bits (64 bytes).
    Este es el BUCLE PRINCIPAL (Sección 6.2.2).
    """
    
    # --- a. Preparar la "Expansión del Mensaje" (Message Schedule) ---
    # Dividimos el bloque de 64 bytes en 16 "palabras" de 4 bytes (32 bits)
    w = [0] * 64
    for i in range(16):
        # Tomamos 4 bytes a la vez del bloque
        w[i] = from_bytes(chunk[i*4 : i*4 + 4])
        
    # Ahora generamos las 48 palabras restantes (16 a 63)
    for i in range(16, 64):
        s0 = sigma0(w[i-15])
        s1 = sigma1(w[i-2])
        w[i] = (w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF

    # --- b. Inicializar las variables de trabajo ---
    # (Se copian del estado hash actual)
    a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7

    # --- c. El Bucle Principal (64 Rondas) ---
    for i in range(64):
        # Aquí ocurre la "magia" de la mezcla
        T1 = (h + Sigma1(e) + Ch(e, f, g) + K[i] + w[i]) & 0xFFFFFFFF
        T2 = (Sigma0(a) + Maj(a, b, c)) & 0xFFFFFFFF
        
        # Rotamos las variables para la siguiente ronda
        h = g
        g = f
        f = e
        e = (d + T1) & 0xFFFFFFFF
        d = c
        c = b
        b = a
        a = (T1 + T2) & 0xFFFFFFFF

    # --- d. Calcular el nuevo estado hash intermedio ---
    # Se suma el resultado de este bloque al estado anterior
    h0 = (h0 + a) & 0xFFFFFFFF
    h1 = (h1 + b) & 0xFFFFFFFF
    h2 = (h2 + c) & 0xFFFFFFFF
    h3 = (h3 + d) & 0xFFFFFFFF
    h4 = (h4 + e) & 0xFFFFFFFF
    h5 = (h5 + f) & 0xFFFFFFFF
    h6 = (h6 + g) & 0xFFFFFFFF
    h7 = (h7 + h) & 0xFFFFFFFF
    
    return h0, h1, h2, h3, h4, h5, h6, h7


# --- FUNCIÓN PRINCIPAL ---

def sha256(message_str):
    """
    Calcula el hash SHA-256 de una cadena de texto.
    """
    
    # 0. Convertir la cadena de texto a bytes (usando UTF-8)
    message_bytes = message_str.encode('utf-8')

    # 1. Aplicar Padding (Relleno)
    padded_message = _pad_message(message_bytes)
    
    # 2. Inicializar el estado Hash (las constantes H)
    h0, h1, h2, h3, h4, h5, h6, h7 = H

    # 3. Procesar el mensaje en bloques de 512 bits (64 bytes)
    for i in range(0, len(padded_message), 64):
        chunk = padded_message[i : i+64]
        h0, h1, h2, h3, h4, h5, h6, h7 = _process_chunk(chunk, h0, h1, h2, h3, h4, h5, h6, h7)

    # 4. Concatenar el estado final para obtener el hash
    # Convertimos cada entero de 32 bits a 4 bytes hexadecimales
    final_hash_hex = (
        f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}"
        f"{h4:08x}{h5:08x}{h6:08x}{h7:08x}"
    )
    
    return final_hash_hex

# --- Ejemplo de uso ---

texto_1 = "hola"
texto_2 = "Hola"
texto_3 = "Esta es una prueba de un texto un poco más largo."

print("--- Implementación Educativa de SHA-256 ---")
print(f"Texto: '{texto_1}'")
print(f"Hash:  {sha256(texto_1)}")
print("-" * 20)
print(f"Texto: '{texto_2}'")
print(f"Hash:  {sha256(texto_2)}")
print("-" * 20)
print(f"Texto: '{texto_3}'")
print(f"Hash:  {sha256(texto_3)}")
print("-" * 20)

# Verificación (comparando con la librería 'hashlib')
import hashlib
print("\n--- Verificación con 'hashlib' (el real) ---")
print(f"Hash:  {hashlib.sha256(texto_1.encode()).hexdigest()}")
print(f"Hash:  {hashlib.sha256(texto_2.encode()).hexdigest()}")
print(f"Hash:  {hashlib.sha256(texto_3.encode()).hexdigest()}")
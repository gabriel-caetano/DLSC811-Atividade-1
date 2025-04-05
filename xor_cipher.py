
def xor_cipher(buffer1: bytes, buffer2: bytes) -> bytes:
    if len(buffer1) != len(buffer2):
        raise ValueError("Os buffers devem ter o mesmo tamanho")
    
    return bytes(b1 ^ b2 for b1, b2 in zip(buffer1, buffer2))

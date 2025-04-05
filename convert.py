import base64

def raw_to_base64(raw_bytes):
    return base64.b64encode(raw_bytes).decode('utf-8')

def base64_to_raw(base64_str):
    return bytearray(base64.b64decode(base64_str))

def raw_to_hex(raw_bytes):
    return ''.join(f'{byte:02x}' for byte in raw_bytes)

def hex_to_raw(hex_str):
    return bytearray.fromhex(hex_str)

def raw_to_ascii(raw_bytes):
    return raw_bytes.decode('ascii')

def ascii_to_raw(ascii_str):
    return ascii_str.encode('ascii')
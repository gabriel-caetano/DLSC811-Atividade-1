from convert import base64_to_raw, hex_to_raw, raw_to_hex, ascii_to_raw, raw_to_ascii
from xor_cipher import xor_cipher
from break_hex_cipher import break_single_char_xor

# parte 1
data_base64 = "QWNvcmRhUGVkcmluaG9RdWVob2pldGVtY2FtcGVvbmF0bw=="
raw_data = base64_to_raw(data_base64)
hex_data = raw_to_hex(raw_data)
ascii_data = raw_to_ascii(raw_data)
raw_from_ascii = ascii_to_raw(ascii_data)

print("Raw bytes  :", raw_data)
print("Base64     :", data_base64)
print("Hexadecimal:", hex_data)
print("ASCII         :", ascii_data)
print("Raw from ASCII:", raw_from_ascii)

# parte 2
plaintext_hex = "41636f72646150656472696e686f517565686f6a6574656d63616d70656f6e61746f"
key_hex = "0b021e0701003e0a0d060c0807063d1a0b0f0e060a1a020c0f0e03170403010f130e"

plaintext = hex_to_raw(plaintext_hex)
key = hex_to_raw(key_hex)

cipher_text = xor_cipher(plaintext, key)
cipher_text_hex = raw_to_hex(cipher_text)

print("Cipher text:", cipher_text_hex)

# parte 3
cipher_text_hex = "072c232c223d2c3e3e2c2328232538202e2c3f3f223d223f2c3c3824072c232c223d2c3e3e2c2328232538202b24212028232c191b1b222e283c382828233f22212c2238393f222e242a2c3f3f223d223f2c2408232c22292c2f22212c3d3f223c38283b2c242c2e222339282e283f002c243e38203d22382e2228202c243e38203e282e38212239283f2024232c002c3e38202122382e223d222928393f222e22232c283e3c3824232c19382922243e3e22272c2b2c373d2c3f3928292c3f223924232c082c3f223924232c272c2b2c373d2c3f392829283b222e281c3828392820242928242c3e392c22202229283f232c3e082220283e202225222028203c38283b243b242c232c3e2e2c3b283f232c3e"

candidates = break_single_char_xor(cipher_text_hex)

for i, (score, key, plaintext) in enumerate(candidates, 1):
    print(f"\nCANDIDATO #{i}")
    print(f"Chave (hex): {hex(key)} | caractere: {chr(key)!r} | Score: {score}")
    print("Mensagem decifrada:\n", plaintext.strip())
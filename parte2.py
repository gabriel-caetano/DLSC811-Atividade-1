
from xor_cipher import xor_cipher
from convert import (
    hex_to_raw,
    raw_to_hex
)

def parte2():
    plaintext_hex = "41636f72646150656472696e686f517565686f6a6574656d63616d70656f6e61746f"
    key_hex = "0b021e0701003e0a0d060c0807063d1a0b0f0e060a1a020c0f0e03170403010f130e"

    plaintext = hex_to_raw(plaintext_hex)
    key = hex_to_raw(key_hex)

    cipher_text = xor_cipher(plaintext, key)
    cipher_text_hex = raw_to_hex(cipher_text)

    print("Cipher text:", cipher_text_hex)

def main():
    parte2()

if __name__ == "__main__":
    main()
    
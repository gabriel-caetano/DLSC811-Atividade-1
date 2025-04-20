from break_hex_cipher import break_single_char_xor

def parte3():
    cipher_text_hex = "072c232c223d2c3e3e2c2328232538202e2c3f3f223d223f2c3c3824072c232c223d2c3e3e2c2328232538202b24212028232c191b1b222e283c382828233f22212c2238393f222e242a2c3f3f223d223f2c2408232c22292c2f22212c3d3f223c38283b2c242c2e222339282e283f002c243e38203d22382e2228202c243e38203e282e38212239283f2024232c002c3e38202122382e223d222928393f222e22232c283e3c3824232c19382922243e3e22272c2b2c373d2c3f3928292c3f223924232c082c3f223924232c272c2b2c373d2c3f392829283b222e281c3828392820242928242c3e392c22202229283f232c3e082220283e202225222028203c38283b243b242c232c3e2e2c3b283f232c3e"

    candidates = break_single_char_xor(cipher_text_hex)

    for i, (score, key, plaintext) in enumerate(candidates, 1):
        print(f"\nCANDIDATO #{i}")
        print(f"Chave (hex): {hex(key)} | caractere: {chr(key)!r} | Score: {score}")
        print("Mensagem decifrada:\n", plaintext.strip())

def main():
    parte3()

if __name__ == "__main__":
    main()
    
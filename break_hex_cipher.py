from convert import hex_to_raw, raw_to_ascii
from xor_cipher import xor_cipher


def score_text(text: str) -> float:
    common_chars = ' aaeoiosrnmdutclpvqgbfhzjxkyw' # caracteres mais frequentes em pt
    # common_chars = ' etaoinshrdlcum' # caracteres mais frequentes em en
    return sum(text.lower().count(c) for c in common_chars)

def break_single_char_xor(cipher_hex: bytes):
    candidates = []
    cipher_bytes = hex_to_raw(cipher_hex)
    for key in range(256):
        key_bytes = bytes([key]) * len(cipher_bytes)
        plaintext_bytes = xor_cipher(cipher_bytes, key_bytes)
        try:
            text = raw_to_ascii(plaintext_bytes)
            if text.isprintable():
                score = score_text(text)
                candidates.append((score, key, text))
        except Exception:
            continue

    candidates.sort(reverse=True)
    return candidates[:3]
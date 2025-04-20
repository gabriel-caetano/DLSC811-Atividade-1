from convert import (
    base64_to_raw,
    raw_to_hex,
    ascii_to_raw,
    raw_to_ascii
)

def parte1():
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

def main():
    parte1()

if __name__ == "__main__":
    main()
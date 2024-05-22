import binascii
import hmac
import hashlib

def main():
    key = b'p@ssw0rd'
    _bytes = b'foobar'##một đối tượng bytes đại diện cho một chuỗi các byte. Nó tương ứng với chuỗi "foobar" được mã hóa thành các byte với bảng mã UTF-8.

    hmac_sha256 = hmac.new(key, digestmod=hashlib.sha256)
    hmac_sha256.update(_bytes)
    digest = hmac_sha256.digest()

    print("HMAC digest as bytes:", digest)
    print("HMAC digest as hex string:", digest.hex())
    return digest.hex()

# import hashlib
# import hmac
# import hashlib
# import unidecode

# def decode_hex_to_string(hex_str):
#     key = b'p@ssw0rd'
#     hmac_sha256 = hmac.new(key, digestmod=hashlib.sha256)
#     # print(bytes.fromhex(hex_str))
#     hmac_sha256.update(bytes.fromhex(hex_str))
#     decoded_bytes = bytes.fromhex(hex_str)#hmac_sha256.digest()
#     print(decoded_bytes)
#     decoded_str = decoded_bytes.decode('iso-8859-1')
#     print(decoded_str)
#     # return decoded_str

def decode_hmac_digest(key, digest):
    hmac_sha256 = hmac.new(key, digestmod=hashlib.sha256)
    hmac_sha256.update(digest)
    decrypted_bytes = hmac_sha256.digest()
    return decrypted_bytes

if __name__ == "__main__":
    main()
    key = b'p@ssw0rd'
    digest = b'\x0f\xa5W\xa7DvD+\x07>\x1c\x0b\x830\xd3\xc6\x0b\xb5\x1285f\xe47\x97>\xd2\xfcU\x9b}\xa5'
    decrypted_bytes = decode_hmac_digest(key, digest)
    print("Decrypted bytes:", decrypted_bytes)
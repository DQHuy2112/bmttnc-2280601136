from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import os

class RSACipher:
    def __init__(self):
        self.private_key_path = "private_key.pem"
        self.public_key_path = "public_key.pem"

    def generate_keys(self):
        """Tạo cặp khóa RSA và lưu vào file."""
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        with open(self.private_key_path, "wb") as priv_file:
            priv_file.write(private_key)

        with open(self.public_key_path, "wb") as pub_file:
            pub_file.write(public_key)

    def load_keys(self):
        """Tải khóa RSA từ file."""
        if not os.path.exists(self.private_key_path) or not os.path.exists(self.public_key_path):
            raise FileNotFoundError("Khóa RSA chưa được tạo. Vui lòng gọi phương thức generate_keys trước.")

        with open(self.private_key_path, "rb") as priv_file:
            private_key = RSA.import_key(priv_file.read())

        with open(self.public_key_path, "rb") as pub_file:
            public_key = RSA.import_key(pub_file.read())

        return private_key, public_key

    def encrypt(self, message, key):
        """Mã hóa thông điệp bằng khóa RSA."""
        cipher = PKCS1_OAEP.new(key)
        encrypted_message = cipher.encrypt(message.encode("utf-8"))
        return encrypted_message

    def decrypt(self, ciphertext, key):
        """Giải mã thông điệp bằng khóa RSA."""
        cipher = PKCS1_OAEP.new(key)
        decrypted_message = cipher.decrypt(ciphertext)
        return decrypted_message.decode("utf-8")

    def sign(self, message, private_key):
        """Ký thông điệp bằng khóa riêng."""
        h = SHA256.new(message.encode("utf-8"))
        signature = pkcs1_15.new(private_key).sign(h)
        return signature

    def verify(self, signature, message, public_key):
        """Xác minh chữ ký bằng khóa công khai."""
        h = SHA256.new(message.encode("utf-8"))
        try:
            pkcs1_15.new(public_key).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False


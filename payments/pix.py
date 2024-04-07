

from uuid import uuid4

import qrcode


class Pix:
    def __init__(self):
        pass

    def create_payment(self, base_dir=""):
        bank_payment_id = str(uuid4())
        
        hash_payment = f'hash_payment_{bank_payment_id}'
        img = qrcode.make(hash_payment)
        img_path = f"qr_code_payment_{bank_payment_id}"
        img.save(f"{base_dir}static/img/{img_path}.png")

        return {"bank_payment_id": bank_payment_id, "qr_code_path": img_path}
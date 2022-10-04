import hashlib


class EncodeMD5:
    def getMD5(self, type, date, company):
        md = hashlib.md5((type + date + company).encode())
        return md.hexdigest()
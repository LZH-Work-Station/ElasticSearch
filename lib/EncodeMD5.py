import hashlib


class EncodeMD5:
    def getMD5(self, type, date, company):
        md = hashlib.md5((type + date + company).encode())
        return md.hexdigest()

    def getMD5Intraday(self, type, date, company, interval):
        md = hashlib.md5((type + date + company + interval).encode())
        return md.hexdigest()

    def getMD5Company(self, type, company):
        md = hashlib.md5((type + company).encode())
        return md.hexdigest()

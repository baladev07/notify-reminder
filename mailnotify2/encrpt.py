from cryptography.fernet import Fernet



class encrypt:
    key = Fernet.generate_key()
    fernet = Fernet(key)

    def __init__(self):
        self.secret_key = 'django-insecure-6-zrh@!jkhl$a71*^-vzdf((uuhg%h&e=q(69uss-+wiak2uu)'
        self.name = 'empty'
        self.loginName = 'empty'
        self.password = 'empty'

    def encryptLocal(self, value):
        return encrypt.fernet.encrypt(value.encode())

    def getSecretKey(self):
        return encrypt.fernet.decrypt(self.encryptLocal(self.secret_key)).decode()

    def getUserName(self):
        return encrypt.fernet.decrypt(self.encryptLocal(self.name)).decode()

    def getLoginName(self):
        return encrypt.fernet.decrypt(self.encryptLocal(self.loginName)).decode()

    def getPassword(self):
        return encrypt.fernet.decrypt(self.encryptLocal(self.password)).decode()

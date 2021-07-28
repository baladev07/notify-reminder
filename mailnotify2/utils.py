from cryptography.fernet import Fernet


class details:
    key = Fernet.generate_key()
    fernet = Fernet(key)

    def __init__(self):
        self.secret_key = 'django-insecure-6-zrh@!jkhl$a71*^-vzdf((uuhg%h&e=q(69uss-+wiak2uu)'
        self.name = 'd5gpk0qa2io2sf'
        self.loginName = 'uefjymjzuzvkbz'
        self.password = 'dcbe9d556b3ff776f7806c4e9fb76c0195c63b9b497dc4caf85cb9419db78c9e'
        self.host = 'ec2-52-202-152-4.compute-1.amazonaws.com'
        self.port = '5432'
        self.email = 'notifyreminder@gmail.com'
        self.mail_password = 'notify_07'
        self.allowed_host = ['notifyreminder.herokuapp.com', '127.0.0.1']


def getName():
    return 'd5gpk0qa2io2sf'


def getSecretKey():
    return 'django-insecure-6-zrh@!jkhl$a71*^-vzdf((uuhg%h&e=q(69uss-+wiak2uu)'


def getLoginName():
    return 'uefjymjzuzvkbz'


def getPassword():
    return 'dcbe9d556b3ff776f7806c4e9fb76c0195c63b9b497dc4caf85cb9419db78c9e'


def getHostName():
    return 'ec2-52-202-152-4.compute-1.amazonaws.com'


def getPort():
    return '5432'


def getEmail():
    return 'notifyreminder@gmail.com'


def getEmailPassword():
    return 'notify_07'


def getAllowedHosts():
    return ['notifyreminder.herokuapp.com', '127.0.0.1']
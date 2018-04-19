from random import Random # 用于生成随机码
from django.core.mail import send_mail # 发送邮件模块
from ALG_x.settings import EMAIL_FROM  # setting.py添加的的配置信息
from .models import Person


def create_str(randomlength = 16):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str

def send_email_test(email, type_post):
    if type_post == 'create_user':
        str = create_str()
        user = Person.objects.get(email = email)
        user.code = str
        user.save()

        url = 'http://localhost:8000/login_register/email_test/%s' % str

        email_title = "请激活邮箱"
        email_body = "点击下面链接以激活账户%s" % url
        print(1)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        print(2)

        if send_status:
            pass
    elif type_post == 'find_password':
        pass



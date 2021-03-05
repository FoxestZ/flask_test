import random, string


from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header

def send_email(receiver, ecode):
    sender = 'Hello<1281838272@qq.com>'
    content = f"<br/>您的验证码为：<span style='color:red;font-size:20px;'>{ecode}</span>"
    message = MIMEText(content, 'html', 'utf-8')
    message['Subject'] = Header('我的验证码', 'utf-8')
    message['From'] = sender
    message['To'] = receiver

    smtpObj = SMTP_SSL('smtp.qq.com')
    smtpObj.login(user='1281838272@qq.com', password='haudnncaxopaghbb')
    # smtpObj.login('181838272@qq.com", "vzkfeprsyhtuhdii")
    smtpObj.sendmail(sender, receiver, str(message))
    smtpObj.quit()


def gen_text():
    list = random.sample(string.ascii_letters+string.digits, 6)
    # print(''.join(list))
    return''.join(list)

code = gen_text()
print(code)
send_email('752904837@qq.com', code)
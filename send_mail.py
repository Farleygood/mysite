import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

'''
if __name__ == '__main__':
    send_mail(
        '来自www.fanleiblog.com的测试邮件',  # subject
        '欢迎访问www.fanleiblog.com,这里是....',  # content
        'xxx@sina.com',  # sender
        ['xxx@qq.com'],  # reception
    )
'''

if __name__ == '__main__':
    subject, from_email,to = '来自www.fanleiblog.com的测试邮件', 'xxx@sina.com', 'xxx@qq.com'
    text_content = '欢迎访问www.fanleiblog.com,这里是....'
    html_content = '<p>欢迎访问<a href="http://www.baidu.com" target=blank>www.fanleiblog.com</a>,这里是樊磊的blog</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attch_alternative(html_content, 'text/html')
    msg.send()
import yagmail


def mass_mailing(to, subject, contents, user=None, password=None, host=None):
    """
    发送邮件  包含群发
    :param to    list or str   str 为单发给一个人  list 为群发
    :param subject    str           邮件主题
    :param contents   list          包含 内容 html文本以及图片的其他附件
    :param user       str           发送者用户名
    :param password   str           发送者密码
    :param host       str           发送的代理服务器地址
    """
    user = user or 'yourusername'
    password = password or 'yourpassword'
    host = host or 'yourserver'
    yag = yagmail.SMTP(
        user=user, password=password, host=host)  # pip install yagmail
    yag.send(to=to, subject=subject, contents=contents)
    print(" send successed !!!")


if __name__ == "__main__":

    to = [
        '597010012@qq.com',
    ]  # 'zhuyp@wopuwulian.com',

    subject = '测试群发功能'

    # html = 'Template.html'
    # with open(html,'r') as f:
    #     l = f.readlines()
    #     l_str = ''.join(item.strip().replace("style"," style") for item in l)
    #     l_str = l_str.format("领取质保卡")
    #     print(l_str)
    # 直接读取格式化后的html文件不可以，原因不明，所以需要替换掉换行之后就好使了

    l_str = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><title>Document</title></head><body><div  style="align-items: center; margin: auto;"><div style="width: 600px;height: 578px;margin: auto;padding: 0;background: url(https://s1.ax1x.com/2020/06/15/N95RIJ.jpg);"><div style="text-align: center;padding-top: 80px;font-family: PingFang SC;color: rgba(255, 255, 255, 0.66);opacity: 1;z-index: 2;">您的预约导出</div><div style="text-align: center;padding-top: 10px;font-size: 26px;font-family: PingFang SC;color: rgba(255, 255, 255, 0.88);opacity: 1;z-index: 2;">「 {0} 」</div><img style="margin: auto;padding: 0;text-align: center;padding-top: 40px;padding-left: 250px;width: 100px;height: 100px;z-index: 2;"src="https://s1.ax1x.com/2020/06/15/N9bGMn.png"/><div style="text-align: center;padding-top: 10px;font-size: 20px;font-family: PingFang SC;color: rgba(255, 255, 255, 1);opacity: 1;z-index: 2;">已完成!</div><div style="text-align: center;padding-top: 60px;font-family: PingFang SC;line-height: 25px;color: rgba(255, 255, 255, 0.66);opacity: 1;z-index: 2;">请在「沃朴物联后台管理系统-预约导出」下载</div><div style="text-align: center;margin-top: 20px;margin-left: 100px;background-color: #18d16e;width: 400px;height: 60px;z-index: 2;"><a style="display: block;text-align: center;line-height: 60px;text-decoration: none;width: 400px;height: 60px;font-size: 26px;font-family: PingFang SC;color: rgba(255, 255, 255, 1);opacity: 1;z-index: 2;"href="https://www.baidu.com"target="_blank">点击前往下载</a></div></div><div style="width: 600px;height: 229px;margin: auto;padding: 0;background: url(https://s1.ax1x.com/2020/06/15/N9IPeS.png);background-size: 100%;"></div></div></body></html>"""
    mass_mailing(to, subject, [l_str])
    pass

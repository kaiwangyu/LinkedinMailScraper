import threading
import tkinter as tk
import csv
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from random import randrange
import re
import os
from PIL import ImageTk, Image


class App:
    def __init__(self, parent):
        #self.listbox = tk.Listbox(parent,width=50, height =5)
        #self.listbox.pack()

        self.button = tk.Button(parent, text='Start', command=self.begin, bg='brown', fg='white',width=15, height =2, font=('helvetica', 9, 'bold'))
        self.button.pack()

    def func(self):
        '''long-running work'''
        self.button.config(text='Running')
        x1 = entry1.get()
        x2 = entry2.get()
        x3 = entry3.get()
        x4 = entry4.get()
        x5 = entry5.get()
        x6 = entry6.get()
        contador = 1  # 计数循环次数
        contador_final = int(float(x3)) - 1
        circles = int(x4)
        finish = int(x5)
        s = int(x6)
        rest_time = int(s * 3600)
        if (s < 0):
            #self.listbox.insert('PLEASE ENTER A POSITIVE VALUE')
            print('PLEASE ENTER A POSITIVE VALUE')
            exit()
        else:
            pass
        print('YOU MAY HAVE', numbers - contador_final, 'PERSONS TO SCRAP')

        # 登陆领英
        options = Options()
        options.add_argument('disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_argument('headless') 无CONSOLE
        options.add_argument('’–disable-webgl')

        driver = webdriver.Chrome(os.path.abspath('chromedriver'), options=options)
        driver.get('https://www.linkedin.com/login')
        username = driver.find_element_by_id('username')
        username.send_keys(x1)
        password = driver.find_element_by_id('password')
        password.send_keys(x2)
        log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
        log_in_button.click()
        time.sleep(40)

        # file_name = r'C:\Users\air\PycharmProjects\pythonlinkedin-v2\log.csv'

        def check():
            try:
                title = driver.title
            except WebDriverException:
                file.close()
                print('PROGRAM IS STOPPED, LOG IS GENERATED ')

        with open(os.path.abspath('log.csv'), 'a', encoding='utf-8') as file:
            write = csv.writer(file, delimiter='\t', lineterminator='\n')
            for number in range(contador_final, numbers):
                Name_search = df['Full Name'][number]  # 调用数组
                num = str(contador)
                #self.listbox.insert(contador)
                print(contador)
                print(Name_search)
                Name_search_particular = df['First Name'][number]
                is_null = pd.isnull(Name_search)  # 检查姓名是否为空
                if is_null == True:
                    print('THIS USER DOES NOT EXIST')  # 如果为空开始下个循环
                    contador += 1
                    continue
                else:
                    time.sleep(randrange(8, 15))
                    check()
                    log_in_button = driver.find_element_by_id('ember21')  # mi red
                    log_in_button.click()
                    time.sleep(randrange(8, 12))
                    check()
                    """第一段 加入EXCEPTION 防止领英崩溃导致主界面无法显示,需要重新返回到主界面开始"""
                    try:
                        log_in_button = driver.find_element_by_xpath(
                            '/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div/section[1]/div/div[1]/a')  # contactos
                    except NoSuchElementException:
                        log_in_button = driver.find_element_by_xpath(
                            '/html/body/div[6]/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div/section[1]/div/div[1]/a'
                            '')  # Contactos
                    log_in_button.click()
                    time.sleep(randrange(10, 12))
                    check()
                    """第一段 加入EXCEPTION 防止领英崩溃导致主界面无法显示,需要重新返回到主界面开始"""

                    """第二段 加入EXCEPTION 防止领英崩溃导致主界面无法显示,需要重新返回到主界面开始"""
                    try:
                        log_in_button = driver.find_element_by_xpath(
                            '/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/div/section/div[1]/div[2]/div/div/input')  # input name
                    except NoSuchElementException:
                        time.sleep(10)
                        try:
                            log_in_button = driver.find_element_by_xpath(
                                '/html/body/div[6]/div[3]/div/div/div/div/div[2]/div/div/main/div/section/div[1]/div[2]/div/div/input')
                        except NoSuchElementException:
                            time.sleep(randrange(10, 12))
                            check()
                            log_in_button = driver.find_element_by_id('ember21')  # mi red
                            log_in_button.click()
                            time.sleep(randrange(10, 15))
                            check()
                            log_in_button = driver.find_element_by_xpath(
                                '/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div/section[1]/div/div[1]/a')  # Contactos
                            log_in_button.click()
                            time.sleep(randrange(10, 12))
                            check()
                            try:
                                log_in_button = driver.find_element_by_xpath(
                                    '/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/div/section/div[1]/div[2]/div/div/input')  # 找到联系人姓名INPUT
                            except NoSuchElementException:
                                time.sleep(randrange(30, 60))
                                check()
                                log_in_button = driver.find_element_by_xpath(
                                    '/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/div/section/div[1]/div[2]/div/div/input')

                    """第二段 加入EXCEPTION 防止领英崩溃导致主界面无法显示,需要重新返回到主界面开始"""

                    try:
                        log_in_button.send_keys(Name_search)  # send name
                        time.sleep(randrange(8, 9))
                        check()
                    except WebDriverException:
                        log_in_button.send_keys(Name_search_particular)
                        time.sleep(randrange(8, 9))
                        check()
                    '''联系人已注销账户或者已被拉黑'''
                    try:
                        log_in_button = driver.find_element_by_xpath(
                            '/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/div/section/ul/li/div[2]/a')  # 点击第一条
                        log_in_button.click()
                        time.sleep(randrange(6, 12))
                        check()
                    except NoSuchElementException:
                        try:
                            log_in_button = driver.find_element_by_xpath(
                                '/html/body/div[6]/div[3]/div/div/div/div/div[2]/div/div/main/div/section/ul/li/div[2]/a')
                            log_in_button.click()
                            time.sleep(randrange(6, 12))
                            check()
                        except NoSuchElementException:
                            print('THIS CONTACT DOES NOT BELONG TO YOUR CONNECTIONS')
                            log_in_button = driver.find_element_by_xpath('/html/body/div[5]/header/div/nav/ul/li[1]/a')
                            log_in_button.click()
                            check()
                            contador += 1
                            continue

                    '''第三段防网页崩溃'''
                    try:
                        local = log_in_local = driver.find_element_by_xpath(
                            '/html/body/div[5]/div[3]/div/div/div/div/div[3]/div/div/main/div/section/div[2]/div[2]/div[2]/span[1]').text
                        print(local)
                    except NoSuchElementException:
                        try:
                            local = log_in_local = driver.find_element_by_xpath(
                                '/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/section/div[2]/div[2]/div[2]/span[1]').text
                            print(local)
                        except NoSuchElementException:
                            print('THIS CONTACT DO NOT HAVE LOCAL COUNTRY INFORMATION DISPLAYED')
                            local = 'THIS CONTACT DO NOT HAVE LOCAL COUNTRY INFORMATION DISPLAYED'
                    try:
                        log_in_button = driver.find_element_by_xpath(
                            '/html/body/div[5]/div[3]/div/div/div/div/div[3]/div/div/main/div/section/div[2]/div[2]/div[2]/span[2]/a')  # 点击信息栏
                        log_in_button.click()
                        time.sleep(randrange(5, 10))
                        check()
                    except NoSuchElementException:
                        log_in_button = driver.find_element_by_xpath(
                            '/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/section/div[2]/div[2]/div[2]/span[2]/a')
                        log_in_button.click()
                        time.sleep(randrange(5, 10))
                        check()
                    '''第三段防网页崩溃'''

                    '''获取联系人邮箱'''
                    try:
                        em = driver.find_element_by_xpath(
                            '/html/body/div[3]/div/div/div[2]/section/div/div[1]/div/section[2]/div/a')
                        em = em.text
                        if (
                                re.fullmatch(regex, em)):  # 在这个路径下找到的信息不符合邮箱格式，调到另外一个路径
                            print(em)
                        else:
                            em = driver.find_element_by_xpath(
                                '/html/body/div[3]/div/div/div[2]/section/div/div[1]/div/section[3]/div/a')
                            em = em.text
                            print(em)
                    except NoSuchElementException:  # 路径没有信息提取或无法提取,换到另外三个个路径,直到找到正确邮件格式,否则提示用户没有设置邮箱可见
                        try:
                            em = driver.find_element_by_xpath(
                                '/html/body/div[3]/div/div/div[2]/section/div/div[1]/div/section[4]/div/a')
                            em = em.text
                            if (re.fullmatch(regex, em)):
                                print(em)
                            else:
                                em = driver.find_element_by_xpath(
                                    '/html/body/div[3]/div/div/div[2]/section/div/div[1]/div/section[5]/div/a')
                                em = em.text
                                print(em)

                        except NoSuchElementException:
                            try:
                                em = driver.find_element_by_xpath(
                                    '/html/body/div[3]/div/div/div[2]/section/div/div[1]/div/section[3]/div/a')
                                em = em.text
                                print(em)

                            except NoSuchElementException:
                                em = 'USER DO NOT HAVE EMA  IL DISPLAYED'
                                print(em)

                    write.writerow((str(contador), Name_search, local, em))
                    '''textList = 
                    for line in textList:
                        # write line to output file
                        file.write(line)
                        file.write("\n")
                        file.close()'''

                    log_in_button = driver.find_element_by_xpath(
                        '/html/body/div[3]/div/div/button')  # ×掉信息栏，返回到主界面，准备下一个CIRCLE
                    log_in_button.click()
                    time.sleep(randrange(5, 7))
                    try:
                        log_in_button = driver.find_element_by_xpath('/html/body/div[5]/header/div/nav/ul/li[1]/a')
                        log_in_button.click()
                        time.sleep(randrange(6, 8))
                    except NoSuchElementException:
                        log_in_button = driver.find_element_by_xpath('/html/body/div[6]/header/div/nav/ul/li[1]/a')
                        log_in_button.click()
                        time.sleep(randrange(6, 8))
                    if (contador % finish == 0):  # 爬虫休息时间，避免平台验证或封号风险
                        driver.close()
                        print('TIME TO SLEEP, SEE YOU', rest_time, 'HOUR(S) LATER')
                        time.sleep(finish)
                        driver = webdriver.Chrome('/Users/air/bin/chromedriver')
                        driver.get('https://www.linkedin.com/login')
                        username = driver.find_element_by_id('username')
                        username.send_keys(x1)
                        password = driver.find_element_by_id('password')
                        password.send_keys(x2)
                        log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
                        log_in_button.click()
                        time.sleep(randrange(30, 40))

                if ((contador % circles == 0) & (contador % finish != 0)):  # 设定循环次数后，浏览器重启，避免浏览器内存崩溃
                    driver.close()
                    time.sleep(randrange(30, 40))
                    driver = webdriver.Chrome('/Users/air/bin/chromedriver')
                    driver.get('https://www.linkedin.com/login')
                    username = driver.find_element_by_id('username')
                    username.send_keys(x1)
                    password = driver.find_element_by_id('password')
                    password.send_keys(x2)
                    log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
                    log_in_button.click()
                    time.sleep(randrange(30, 40))
                else:
                    contador += 1
                    continue
                contador += 1

        self.button.config(text='Done')
        self.button.config(state=tk.NORMAL)

    def begin(self):
        '''start a thread and connect it to func'''
        self.button.config(state=tk.DISABLED)
        threading.Thread(target=self.func, daemon=True).start()

if __name__ == '__main__':
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # 邮箱检查正式表达式
    filename = "Connections.csv"
    col_list = ['First Name', 'Last Name']
    df = pd.read_csv(filename, usecols=col_list, encoding='utf-8')
    index = df.index
    numbers = len(index)
    df["Full Name"] = df["First Name"] + ' ' + df["Last Name"]  # 全名拼接



    root = tk.Tk()


    canvas1 = tk.Canvas(root, width=700, height=720, relief='raised')
    canvas1.pack()
    image = Image.open("perlove.png")
    resize_image = image.resize((100, 80))
    img = ImageTk.PhotoImage(resize_image)
    panel = tk.Label(root, image=img)
    canvas1.create_window(500, 180, window=panel)

    label1 = tk.Label(root, text='Linkedin Contacts Email Scraper')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(350, 25, window=label1)
    label1 = tk.Label(root, text='Linkedin Contacts Email Scraper')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(350, 25, window=label1)

    label7 = tk.Label(root,
                      text='PLEASE KEEP THE BROWSER WINDOW ALWAYS ON TOP AND PLEASE SHUT DOWN YOUR VPN 请尽量不要最小化浏览器请关闭VPN',
                      fg='red')
    label7.config(font=('helvetica', 8))
    canvas1.create_window(350, 75, window=label7)

    label2 = tk.Label(root, text='ENTER YOUR LINKEDIN ACCOUNT 输入您的领英账号')
    label2.config(font=('helvetica', 10))
    canvas1.create_window(200, 100, window=label2)

    entry1 = tk.Entry(root)
    entry1.insert(-1, '@gmail.com')
    canvas1.create_window(200, 140, window=entry1)

    label3 = tk.Label(root, text='ENTER YOUR PASSWORD 输入您的领英密码')
    label3.config(font=('helvetica', 10))
    canvas1.create_window(200, 200, window=label3)

    entry2 = tk.Entry(root, show="*")
    entry2.insert(-1, '***')
    canvas1.create_window(200, 240, window=entry2)

    label4 = tk.Label(root, text='WHICH NUMBER OF CONNECTION LIST WOULD YOU LIKE TO START 输入索引起始位置')
    label4.config(font=('helvetica', 10))
    canvas1.create_window(280, 300, window=label4)

    entry3 = tk.Entry(root)
    entry3.insert(-1, '1')
    canvas1.create_window(200, 340, window=entry3)

    label5 = tk.Label(root, text='ENTER CIRCLES TO RESTART YOUR BROWSER 设置循环次数重启浏览器 默认每60次重启')

    label5.config(font=('helvetica', 10))
    canvas1.create_window(280, 400, window=label5)

    entry4 = tk.Entry(root)
    entry4.insert(-1, '60')
    canvas1.create_window(200, 440, window=entry4)

    label6 = tk.Label(root, text='ENTER CIRCLES PAUSE THE TASKS 设置循环次数暂停爬虫 默认200次')
    label6.config(font=('helvetica', 10))
    canvas1.create_window(280, 500, window=label6)

    entry5 = tk.Entry(root)
    entry5.insert(-1, '200')
    canvas1.create_window(200, 540, window=entry5)

    label7 = tk.Label(root, text='STANDBY TIME 爬虫暂停休息时间默认2小时 避免平台验证或封号')
    label6.config(font=('helvetica', 10))
    canvas1.create_window(280, 600, window=label7)

    entry6 = tk.Entry(root)
    entry6.insert(-1, '2')
    canvas1.create_window(200, 640, window=entry6)

    app = App(root)
    root.mainloop()
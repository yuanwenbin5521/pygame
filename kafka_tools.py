# coding=UTF-8
import Tkinter as tk
from kafka import KafkaProducer
from tkMessageBox import *
window=tk.Tk()
window.title('Kafka Tools')
window.geometry('300x100')





servicesStr=tk.StringVar()
services = tk.Entry(window,show=None,textvariable=servicesStr)

topicStr=tk.StringVar()
topic = tk.Entry(window,show=None,textvariable=topicStr)

msgStr=tk.StringVar()
msg = tk.Entry(window,show=None,textvariable=msgStr)

services.pack()
topic.pack()
msg.pack()
def send_msg():

    try:
        producer = KafkaProducer(bootstrap_servers=servicesStr.get())
        producer.send(topicStr.get(), msgStr.get())
    except Exception  as e:
        showerror("发送失败！",e.message)
    else:
        showinfo("发送成功！","kafka消息发送成功！")

b = tk.Button(window,
    text='send message',
    width=15, height=2,
    command=send_msg)
b.pack()
window.mainloop()
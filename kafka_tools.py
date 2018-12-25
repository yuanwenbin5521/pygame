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


{"BizConv":"Following","BusinessCode":3001,"CheckStatus":"内部复核通过","CounterpartyID":"收益凭证","DaycountConv":"1","DivAdjust":1,"Edge":"JSON:[\"\"]","EventID":"1545717616191_testxj002","EventType":135001,"ExpiryDate":"2018/12/25 00:00:00","FixingRecord":0,"MakerID":"cubetest31","MarginNet":0,"MsgType":"240300","OverrideObsDate":"JSON:[\"2018/12/25\"]","PerformanceType":"Single","Position":10.00000000,"ProductType":119006,"QuantoFlag":"Vanilla","ReportingNotional":0E-8,"SalesID":"JSON:[\"\"]","SeqNo":1545717616191,"SettleCcy":"CNY","SettlementDate":"2018/12/25 00:00:00","SettlementType":"Cash","Strategy":"2323","StrikeDate":"2018/12/25 00:00:00","SubBook":"12341","TemplateType":"Autocall","TradeCcy":"CNY","TradeDate":"2018/12/25 00:00:00","TradeID":"testxj002","TradePrice":0E-8,"TradeType":"BC","Underlying":[{"ExchangeCode":"SH","InitialFixing":2.0000000000000000,"OverrideFixing":3.00000000,"Underlying":"600000.SH","UnderlyingCcy":"CNY","Weight":1.00000000}],"optionpremiumvalid":0}

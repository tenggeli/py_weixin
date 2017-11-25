# -*- coding: utf-8 -*-
# filename: receive.py
import xml.etree.ElementTree as ET

import logging
logging.basicConfig(filename='/mnt/log/nginx/python.log',level=logging.DEBUG)
logging.info('this is receive.py')

def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    msg_type = xmlData.find('MsgType').text
    if msg_type == 'text':
        return TextMsg(xmlData)
    elif msg_type == 'image':
        print "xxxx"
        return ImageMsg(xmlData)

class Msg(object):
    def __init__(self, xmlData):
        print "Msg"
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text
        self.Content = xmlData.find('Content').text
        #self.MediaId = xmlData.find('MediaId').text

class TextMsg(Msg):
    def __init__(self, xmlData):
        print "text"
        Msg.__init__(self, xmlData)
        self.Content = xmlData.find('Content').text.encode("utf-8")

class ImageMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        print "ImageMsg"
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text
        print "cccccc"
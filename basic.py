# -*- coding: utf-8 -*-
#  filename: basic.py
import urllib
import time
import json
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
import MySQLdb

engine = create_engine("mysql+mysqldb://root:root@127.0.0.1:3306/test", max_overflow=5)

class Basic:
    def __real_get_access_token(self):
        appId = "wxd4a571adfc4d2c79"
        appSecret = "a1238284510d1e8c2183f998343d42c3"

        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (appId, appSecret))
        urlResp = urllib.urlopen(postUrl)
        urlResp = json.loads(urlResp.read())
        self.__accessToken = urlResp['access_token']
        self.__leftTime = urlResp['expires_in']

        '''
            1。去数据库查询是否有toke 
                    存在 判断失效时间
                        未失效 使用
                        失效 重新获取，更新toke
                    不存在 获取toke 写入并记录 失效时间
        '''
    def __init__(self):
        self.__accessToken = ''
        self.__leftTime = 0
    def get_access_token(self):



        if self.__leftTime < 10:
            self.__real_get_access_token()
            return self.__accessToken
    def run(self):
        while(True):
            if self.__leftTime > 10:
                time.sleep(2)
                self.__leftTime -= 2
            else:
                self.__real_get_access_token()

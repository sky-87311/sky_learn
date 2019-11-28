# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 21:09
# @Author  : 边笑天
# @File    : test_01.py
# @Software: PyCharm

import unittest
import requests
import json
from requests.packages import urllib3

urllib3.disable_warnings() #关闭警告信息

def login(user="taojiaming",psw="123456"):
    login_url = "https://gateway.bdxetyy.com/bdxdoctor-authentication/admin/login"
    login_header = {
    "Host":"gateway.bdxetyy.com",
    "Connection":"keep-alive",
    "Content-Length":"45",
    "Accept":"application/json, text/plain, */*",
    "Origin":"https://his.bdxetyy.com",
    "Authorization":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1Y2U3ZjA4NC05NzNjLTRjNzgtOWY4My0wYmQ2OGY4NTU4MTQiLCJpYXQiOjE1NzQyMjU3MzcsImlzcyI6InRhb2ppYW1pbmciLCJzdWIiOiJ0YW9qaWFtaW5nIiwiZXhwIjo0NzI5ODk5MzM3fQ.RZIDae1M98_WNQWOszWz5IsTqxzDMWJHW-aMIshFmZY",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "Sec-Fetch-Mode":"cors",
    "Content-Type":"application/json;charset=UTF-8",
    "Sec-Fetch-Site":"same-site",
    "Referer":"https://his.bdxetyy.com/",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    }
    login_body = {"username":"%s"%user,"password":"%s"%psw}
    login_result = requests.post(url=login_url,headers=login_header,json=login_body,verify=False)
    #print(login_result.json())
    #print(login_result.json()["datas"]["token"])
    login_token = (login_result.json()["datas"]["token"])
    return login_token
#print(login())
token=login()

class Select(unittest.TestCase):
    """北斗星登陆查询测试集合"""
    @classmethod
    def setUpClass(cls):
        login()

    def tearDown(self):
        print('已退出')

    def test_seekperson_select(self):
        """查询就诊人"""
        select_url = "https://gateway.bdxetyy.com/bdxdoctor-admin/seekMedicalPerson"
        select_header ={
            "pageNum": "1",
            "Sec-Fetch-Mode": "cors",
            "pageSize": "10",
            "Origin": "https://his.bdxetyy.com",
            "Authorization": "%s"%token,
            "orderBy": "s.create_date desc",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Sec-Fetch-Site": "same-site",
            "Referer": "https://his.bdxetyy.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Token": "%s"%token
        }
        select_body = {"staffCardType":""}
        select_result = requests.post(url=select_url,headers=select_header,json=select_body,verify=False)
        pagesize = select_result.json()["pageSize"]
        total = select_result.json()["total"]
        self.assertEqual(pagesize, 10)

if __name__ == '__main__':
    unittest.main()

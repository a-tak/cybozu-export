#!/usr/bin/python3
# coding: utf-8

#http://qiita.com/beatinaniwa/items/72b777e23ef2390e13f8
import lxml.html
import requests
import configparser
import sys
import codecs
import pprint

args = sys.argv

#target_url = 'http://news.tv-asahi.co.jp/news_politics/articles/000041338.html'
#target_html = requests.get(target_url).text

#shift-jisに変換処理を追加要
f = open(args[1],"r", encoding="shift_jis")
target_html = f.read()
f.close()

root = lxml.html.fromstring(target_html)
#text_content()メソッドはそのタグ以下にあるすべてのテキストを取得する
value = root.cssselect("body")[0].text_content()
#value = root.cssselect("table.calendar > tbody > tr:nth-child(2) > td:nth-child(3)")[0].text_content()
#value = root.cssselect("body > table.calendar > tbody > tr:nth-child(2) > td:nth-child(3)")[0].text_content()
pprint.pprint(value)


#!/usr/bin/python3
# coding: utf-8

#http://qiita.com/beatinaniwa/items/72b777e23ef2390e13f8
import lxml.html
import requests

target_url = 'http://news.tv-asahi.co.jp/news_politics/articles/000041338.html'
target_html = requests.get(target_url).text
root = lxml.html.fromstring(target_html)
#text_content()メソッドはそのタグ以下にあるすべてのテキストを取得する
root.cssselect('#news_body > p').text_content()


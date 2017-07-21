#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' a test module '

__author__ = '朱超'

' url handlers '
from coreweb import get,post

@get('/blog')
def get_blog():
    return 'Hello,Blog'




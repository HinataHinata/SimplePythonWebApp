#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' a test module '

__author__ = '朱超'

import orm
from models import User,Blog,Comment
import pymysql
import asyncio

loop = asyncio.get_event_loop()
async def test():
    await orm.create_pool(user='www-data',password='www-data',db='simple')
    u = User(name='KeWei',email='test005@example.com',passwd='1234567890',image='about:blank')
    # await  u.save()
    user = await User.find('1') # 这个地方开始忘记了加上'' 导致一个转换double的错误。
    print(user.name,user.email,user.create_at,user.id)
    result = await User.findNumber('count(distinct name)')
    print(result)
#
# for x in test():
#     pass
loop.run_until_complete(test())



# example to connect to sql
# import asyncio
# import aiomysql
#
#
# async def test_example(loop):
#     conn = await aiomysql.connect(host='127.0.0.1', port=3306,
#                                   user='root', password='', db='mysql',
#                                   loop=loop)
#
#     async with conn.cursor() as cur:
#         await cur.execute("SELECT Host,User FROM user")
#         print(cur.description)
#         r = await cur.fetchall()
#         print(r)
#     conn.close()
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test_example(loop))




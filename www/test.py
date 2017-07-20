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
    u = User(name='Test',email='test004@example.com',passwd='1234567890',image='about:blank')
    await u.save()
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




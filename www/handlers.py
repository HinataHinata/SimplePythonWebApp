#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' a test module '

__author__ = '朱超'

' url handlers '
import re,time,json,logging,hashlib,base64,asyncio
from coreweb import get,post
from models import User,Comment,Blog,next_id


@get('/')
async def index(request):
    summary = '李白（701年－762年），字太白，号青莲居士，中国唐朝诗人，自言祖籍陇西成纪（今甘肃省天水市秦安县），先世西凉武昭王李嵩之后，与李唐皇室同宗，得罪播西域。幼时内迁，寄籍剑南道绵州（今四川省江油昌隆县）。另郭沫若考证李白出生于吉尔吉斯碎叶河上的碎叶城，属唐安西都护府（今楚河州托克马克市）[1]。有“诗仙”、“诗侠”、“酒仙”、“谪仙人”等称呼，活跃于盛唐[2]，为杰出的浪漫主义诗人。与杜甫合称“李杜”[3]。被贺知章惊呼为“天上谪仙”。'
    blogs= [
        Blog(id = '1',name='TestBlog',summary= summary,create_at = time.time()-120),
        Blog(id='2', name='SomethingNew', summary=summary, create_at=time.time() - 3600),
        Blog(id = '3',name='Learn Swift',summary= summary,create_at = time.time()-7200),
    ]
    return {
        '__template__':'blogs.html',
        'blogs':blogs
    }

@get('/blog')
def get_blog():
    return 'Hello,Blog'




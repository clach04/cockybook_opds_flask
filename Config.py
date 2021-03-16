# coding: UTF-8

import os


__author__ = 'lei'


# #############################
#root for opds server website
#SITE_URL = "http://10.10.113.237:5000"
SITE_URL = "http://opds.cockybook.com"
SITE_URL = None
SITE_URL = 'http://localhost:5000/'
SITE_URL = SITE_URL or os.environ.get('SITE_URL')
SITE_TITLE = "Opds CockyBook"
SITE_EMAIL = "yinlei212@gmail.com"
SITE_BOOK_LIST = SITE_URL + "/list"

#download URL is SITE_BOOK_DONWLOAD/$path/$filename.$postfix
SITE_BOOK_DONWLOAD = 'http://7sbqcs.com1.z0.glb.clouddn.com'
SITE_BOOK_DONWLOAD = SITE_URL + "download/"

#for local filesyste
base = "C:\\code\\py\\cockybook\\epubs"

# Used In opdscore.py
filesyste_type='LocalFileSystem'
#filesyste_type = 'QiniuFileSystem'
#filesyste_type = 'LocalMetadataFileSystem'

description=u"""
     OPDS 标准核心功能是支持 EPUB 标准和基于 Atom XML 的目录格式.
可以使用阅读器进行在线书库添加，比如FBReader、静读天下（Moon+ Reader）、Aldiko、Stanza等等.
添加地址为:   http://opds.cockybook.com
"""
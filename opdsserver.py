# coding: UTF-8

from xml.dom.minidom import Document
from flask import Flask, send_file, make_response, g
import Const
from opdscore import FeedDoc, Link, OpdsProtocol, Entry

import Config

import utils

import logging

__author__ = 'lei'

app = Flask(__name__)

@app.route("/static/<path:stcpath>")
def css(stcpath):
    return app.send_static_file(stcpath)

@app.route("/")
def root():
    d=Document()
    print('clach04_debug d %r' % d)
    print('clach04_debug type(d) %r' % type(d))
    f = FeedDoc(d)
    entry = Entry()
    entry.id = Config.SITE_BOOK_LIST
    print('clach04_debug Config.SITE_URL %r' % Config.SITE_URL)
    entry.content = "all Books List By Type"
    entry.title = "Book List"

    entry.updated = utils.getNow()
    # TODO add Another Links
    entry.links = [Link(entry.id, Const.book_link_rel_subsection, "Book List", Const.book_type_entry_catalog)]
    f.createEntry(entry)
    resp = make_response(f.toString())
    resp.headers['Content-Type'] = 'application/xml; profile=opds-catalog; kind=navigation'
    print('clach04_debug %r' % 'about to return /')

    return resp

@app.route('/list/')
@app.route('/list/<path:path>/')
def listbooks(path="/"):
    feed = FeedDoc(Document(), path)

    # TODO add *** to feed.toString()
    l = getOpdsProtocol().listBooks(path)

    for entry in l:
        feed.createEntry(entry)

    resp = make_response(feed.toString())
    resp.headers['Content-Type'] = 'text/xml; profile=opds-catalog; kind=navigation'
    print('clach04_debug %r' % 'about to return /ist*')
    return resp

@app.route('/download/<path:path>')
def download(path):
    """
    download book
    """
    print('clach04_debug download path %r' % path)
    filePath = getOpdsProtocol().dowloadBook(path)
    return send_file(filePath)

@app.route('/show/<path:path>')
def showhtml(path):
    return "show file:" + path


def getOpdsProtocol():
    return OpdsProtocol()


if __name__ == "__main__":
    #Config.SITE_URL = 'http://localhost:5000/'

    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                )
    app.debug = True
    app.run(host='0.0.0.0')


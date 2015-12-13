#! /usr/bin/env python
# -*- coding: utf-8 -*-

def application(environ, start_response):
    start_response('200 OK', [('Content_Type', 'text/html')])
    return [b'<h1>Hello, py web!</h1>']
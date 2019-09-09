#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'Web APP server,listen in host:9000.Created on 2019-09-09'
__author__:"HuangTao"

import logging;logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time

from aiohttp import web

#url='/' request
def index(request):
	return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

#main loop
@asyncio.coroutine
def init(loop):
	app=web.Application(loop=loop)
	app.router.add_route('GET','/',index)	#add new router for response
	srv=yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return srv

if __name__=='__main__':
	loop=asyncio.get_event_loop()
	loop.run_until_complete(init(loop))
	loop.run_forever()
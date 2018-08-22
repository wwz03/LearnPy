#application_hello.py
def  application(environ, start_response):
	start_response('200 ok', [('context-type','text/html')])
	body='<h1>hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web 二傻子')
	#body='<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')]

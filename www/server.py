#server.py
from wsgiref.simple_server 	import make_server
from application_hello		import application

httpd = make_server('', 7000, application)
print('server http on port 7000...')
httpd.serve_forever()

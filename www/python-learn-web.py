#python-learn-web
#后台把HTML语言传递到前台，前台解析，形成看到的网页。后台到前台的传输使用的就是http协议
#HTTP请求：步骤1：输入网址，发送请求，包括get，post。get的话，只发送一个head，post有body。一个HTTP请求只申请一个。申请-响应模式

#HTTP格式：
GET：

GET /path http/1.1
haad1：value1



HTTP
HTML
CSS
JavaScript:JavaScript是为了让HTML具有交互性而作为脚本语言添加的，JavaScript既可以内嵌到HTML中，也可以从外部链接到HTML中。如果我们希望当用户点击标题时把标题变成红色，就必须通过JavaScript来实现


当我们用Python或者其他语言开发Web应用时，我们就是要在服务器端动态创建出HTML，这样，浏览器就会向不同的用户显示出不同的Web页面。

示例：
<html>
	<head>
		<title>web学习</title>
		<style>
		h1{
			color: #333333;
			font-size: 48px;
			text-shadow: 3px 3px 3px #666666;
		}		
		</style>
		<script>
			function change(){
				document.getElementsByTagName('h1')[0].style.color = '#ff0000';
			}
		</script>
	</head>
	<body>
		<h1 onclick="change()"> Hello, World!</h1>
	</body>
</html>


了解了HTTP协议和HTML文档，我们其实就明白了一个Web应用的本质就是：
1.浏览器发送一个HTTP请求；
2.服务器收到请求，生成一个HTML文档；
3.服务器把HTML文档作为HTTP响应的Body发送给浏览器；
4.浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

静态服务器：提前准备好html文件，等待用户请求时，直接返回html文件，进行解析显示

动态html生成：使用python，根据用户请求，服务器端 动态生成html文件。应用端忽略http请求和tcp请求。而是用统一的借口：WSGI（WEB SERVER GATEWAY INTERFACE）
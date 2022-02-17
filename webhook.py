from dhooks import Webhook

hook = Webhook("URL вебхука")

while True:
	say = input('Что ввести: ')
	hook.send(say)

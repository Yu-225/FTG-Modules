from .. import loader, utils
from telethon.errors import MessageEmptyError

def register(cb):
	cb(ReverseMod())

class ReverseMod(loader.Module):
	"""Реверс"""
	strings = {'name': 'Reverse'}
	async def reverse(self, arg):
		self.arglist = list(arg)
		self.newlist = []
		self.result = ''

		for char in arglist:
			if char=='q':
				newlist.append('й')
			if char=='w':
				newlist.append('ц')
			if char=='e':
				newlist.append('у')
			if char=='r':
				newlist.append('к')
			if char=='t':
				newlist.append('е')
			if char=='y':
				newlist.append('н')
			if char=='u':
				newlist.append('г')
			if char=='i':
				newlist.append('ш')
			if char=='o':
				newlist.append('щ')
			if char=='p':
				newlist.append('з')
			if char=='[':
				newlist.append('х')
			if char==']':
				newlist.append('ї')
			if char=='a':
				newlist.append('ф')
			if char=='s':
				newlist.append('і')
			if char=='d':
				newlist.append('в')
			if char=='f':
				newlist.append('а')
			if char=='g':
				newlist.append('п')
			if char=='h':
				newlist.append('р')
			if char=='j':
				newlist.append('о')
			if char=='k':
				newlist.append('л')
			if char=='l':
				newlist.append('д')
			if char==';':
				newlist.append('ж')
			if char=='\'':
				newlist.append('є')
			if char=='z':
				newlist.append('я')
			if char=='x':
				newlist.append('ч')
			if char=='c':
				newlist.append('с')
			if char=='v':
				newlist.append('м')
			if char=='b':
				newlist.append('и')
			if char=='n':
				newlist.append('т')
			if char=='m':
				newlist.append('ь')
			if char==',':
				newlist.append('б')
			if char=='.':
				newlist.append('ю')
			if char=='/':
				newlist.append('.')
			if char==' ':
				newlist.append(' ')
		result = result.join(newlist)
		return result

	async def revcmd(self, message):
		""".rev <текст або реплай>"""
		try:
			arg = utils.get_args_raw(message)
			reply = await message.get_reply_message()
			if not arg and not reply:
				return await message.edit("Тут нема тексту.")
			if reply:
				return await message.edit(str(reverse(reply)))
			if arg:
				return await message.edit(str(reverse(arg)))
		except MessageEmptyError:
			return await message.edit("Це не текст.")
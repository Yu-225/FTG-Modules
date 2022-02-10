from .. import loader, utils
from time import sleep



class TimerMod(loader.Module):
    """Timer""" 
    strings = {'name': 'Timer'} 
    
    async def timercmd(self, message):
        """Timer sec"""
        time = utils.get_args_raw(message)
        await message.edit(time + ' sec')
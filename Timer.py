from .. import loader, utils
from time import sleep



class TimerMod(loader.Module):
    """Timer""" 
    strings = {'name': 'Timer'} 
    
    async def timercmd(self, event):
        """Timer sec"""
        time = utils.get_args_raw(event)
        
        try: int(time)
        except: await event.edit('Error: Invalid You і твоя команда')

        for i in range(time):
            await event.edit(time + ' sec')
            sleep(1)
            time-=1
        await event.edit('ypa )')
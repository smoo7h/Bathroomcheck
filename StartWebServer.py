import web
import time
import RPi.GPIO as IO

MENS_IO = 2
WOMENS_IO = 3

IO.setmode(IO.BCM)
IO.setup(MENS_IO, IO.IN, pull_up_down=IO.PUD_UP)
IO.setup(WOMENS_IO, IO.IN, pull_up_down=IO.PUD_UP)

urls = (
        '/door1', 'Door1',
        '/door2', 'Door2',
        '/washroom', 'WashRoom',
        '/serverroom', 'ServerRoom'
        )

app = web.application(urls, globals())

web.config.debug = True

class WashRoom:
    def __init__(self):
        self.render = web.template.render('templates/')

    def GET(self, name=None):
        return self.render.index(time.ctime(), time.ctime())

    def POST(self, name):
        return "post"



class Door1:
    def GET(self):
        #get gpio status here
        status = IO.input(MENS_IO)
        
        if status:
            return '{"Status":"True"}'
        else:
            return '{"Status":"False"}'

class Door2:
    def GET(self):
        #get gpio status here
        status = IO.input(WOMENS_IO)
        
        if status:
            return '{"Status":"True"}'
        else:
            return '{"Status":"False"}'


class ServerRoom:
    def __init__(self):
        self.render = web.template.render('templates/')
    
    def GET(self, name=None):
        return self.render.ServerRoom(time.ctime())
    
    def POST(self, name):
        return "post"



if __name__=='__main__':app.run()


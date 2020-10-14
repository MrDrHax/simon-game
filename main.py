import pyglet, guillermo, math, danny
from time import sleep
from pyglet import shapes

# colors in RGB
colors = {
    'red' : (255,0,0),
    'green': (0,255,0),
    'blue' : (0,0,255),
    'yellow' : (255,255,0),
    'dark red' : (100,0,0),
    'dark green': (0,100,0),
    'dark blue' : (0,0,100),
    'dark yellow' : (100,100,0)
}

#                            /$$ /$$          
#                           | $$|__/          
#   /$$$$$$  /$$   /$$  /$$$$$$$ /$$  /$$$$$$ 
#  |____  $$| $$  | $$ /$$__  $$| $$ /$$__  $$
#   /$$$$$$$| $$  | $$| $$  | $$| $$| $$  \ $$
#  /$$__  $$| $$  | $$| $$  | $$| $$| $$  | $$
# |  $$$$$$$|  $$$$$$/|  $$$$$$$| $$|  $$$$$$/
#  \_______/ \______/  \_______/|__/ \______/ 

pyglet.options['search_local_libs'] = True
pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')

audio1 = pyglet.media.load('audio/audio1.wav', streaming = False)
audio2 = pyglet.media.load('audio/audio2.wav', streaming = False)
audio3 = pyglet.media.load('audio/audio3.wav', streaming = False)
audio4 = pyglet.media.load('audio/audio4.wav', streaming = False)

window = pyglet.window.Window(800, 800, resizable=False, vsync=True)

mainDrawBatch = pyglet.graphics.Batch()
initialDrawBatch = pyglet.graphics.Batch()
    

#        /$$ /$$ /$$                              
#       | $$|__/| $$                              
#   /$$$$$$$ /$$| $$$$$$$  /$$   /$$ /$$  /$$$$$$ 
#  /$$__  $$| $$| $$__  $$| $$  | $$|__/ /$$__  $$
# | $$  | $$| $$| $$  \ $$| $$  | $$ /$$| $$  \ $$
# | $$  | $$| $$| $$  | $$| $$  | $$| $$| $$  | $$
# |  $$$$$$$| $$| $$$$$$$/|  $$$$$$/| $$|  $$$$$$/
#  \_______/|__/|_______/  \______/ | $$ \______/ 
#                              /$$  | $$          
#                             |  $$$$$$/          
#                              \______/           

def hacerArco(xSource,ySource,col,startAngle,endAngle,radious,lines = 50, widthOfLine = 100, batchProcces = mainDrawBatch):
    '''
    Mathematically makes an arch with specified amount of lines.
    Ark is defined as 3 point arch.
    Adds the lines to specified batch to make sure it works properly
    
    takes in:
    xSource (float) gives the theoretical center of the 3 point arch in X
    ySource (float) gives the theoretical center of the 3 point arch in Y

    col (tuple) color defined in RGB as int

    startAngle (float) the angle in degrees to start drawing from
    endAngle (float) the target angle in degrees to draw to
    radious (float) the distance from the throretical center to where the line will be drawn (in pixels)

    lines (int) amount of lines the arch wil have in total, default 50
    widthOfLine (int) the width in pixels that the line will be drawn as, default 100 

    batchProccces (pyglet batchDraw) the batch to where the lines will be added to
    '''
    linesPos = []
    angle = (endAngle - startAngle) / lines

    for lineNumber in range(lines + 1):
        x = math.cos((angle * lineNumber + startAngle) * math.pi / 180) * radious + xSource
        y = math.sin((angle * lineNumber + startAngle) * math.pi / 180) * radious + ySource
        linesPos.append((x,y))

    toReturn = []
    for i in range(lines):
        toReturn.append(shapes.Line(linesPos[i][0], linesPos[i][1], linesPos[i + 1][0], linesPos[i + 1][1], width=widthOfLine, color=col, batch=batchProcces))
    
    return toReturn

# makes lines and appends the circle parts to their respective patches

# batch creation
redDrawBatch = pyglet.graphics.Batch()
greenDrawBatch = pyglet.graphics.Batch()
blueDrawBatch = pyglet.graphics.Batch()
yellowDrawBatch = pyglet.graphics.Batch()

# line creation by colour
simonRedActive = hacerArco(window.width//2,window.height//2,colors['red'],0,90,300, batchProcces=redDrawBatch)
simonRedUnactive = hacerArco(window.width//2,window.height//2,colors['dark red'],0,90,300, batchProcces=mainDrawBatch)

simonGreenActive = hacerArco(window.width//2,window.height//2,colors['green'],90,180,300, batchProcces=greenDrawBatch)
simonGreenUnactive = hacerArco(window.width//2,window.height//2,colors['dark green'],90,180,300, batchProcces=mainDrawBatch)

simonBlueActive = hacerArco(window.width//2,window.height//2,colors['blue'],180,270,300, batchProcces=blueDrawBatch)
simonBlueUnactive = hacerArco(window.width//2,window.height//2,colors['dark blue'],180,270,300, batchProcces=mainDrawBatch)

simonYellowActive = hacerArco(window.width//2,window.height//2,colors['yellow'],270,360,300, batchProcces=yellowDrawBatch)
simonYellowUnactive = hacerArco(window.width//2,window.height//2,colors['dark yellow'],270,360,300, batchProcces=mainDrawBatch)



#   /$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$ 
#  /$$_____/ /$$_____/ /$$__  $$ /$$__  $$ /$$__  $$
# |  $$$$$$ | $$      | $$  \ $$| $$  \__/| $$$$$$$$
#  \____  $$| $$      | $$  | $$| $$      | $$_____/
#  /$$$$$$$/|  $$$$$$$|  $$$$$$/| $$      |  $$$$$$$
# |_______/  \_______/ \______/ |__/       \_______/

scoreLabel = pyglet.text.Label('score',
                          font_name='Times New Roman',
                          font_size=40,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center', batch=mainDrawBatch)

score = 0
current = 0

#              /$$                 /$$              
#             | $$                | $$              
#   /$$$$$$$ /$$$$$$    /$$$$$$  /$$$$$$    /$$$$$$ 
#  /$$_____/|_  $$_/   |____  $$|_  $$_/   /$$__  $$
# |  $$$$$$   | $$      /$$$$$$$  | $$    | $$$$$$$$
#  \____  $$  | $$ /$$ /$$__  $$  | $$ /$$| $$_____/
#  /$$$$$$$/  |  $$$$/|  $$$$$$$  |  $$$$/|  $$$$$$$
# |_______/    \___/   \_______/   \___/   \_______/

def makeRed(activo = True, doStuff = True):
    '''
    plays audio corresponding to color, and queues the line to be drawn or not

    activo (bool) makes colour active or not
    '''
    global toDraw, audio1
    if activo:
        toDraw[0] = True
        try:
            audio1.play()
        except:
            print('no se puede poner audio')
    else:
        toDraw[0] = False

def makeGreen(activo = True, doStuff = True):
    '''
    plays audio corresponding to color, and queues the line to be drawn or not

    activo (bool) makes colour active or not
    '''
    global toDraw, audio2
    if activo:
        toDraw[1] = True
        try:
            audio2.play()
        except:
            print('no se puede poner audio')
    else:
        toDraw[1] = False

def makeBlue(activo = True, doStuff = True):
    '''
    plays audio corresponding to color, and queues the line to be drawn or not

    activo (bool) makes colour active or not
    '''
    global toDraw, audio3
    if activo:
        toDraw[2] = True
        try:
            audio3.play()
        except:
            print('no se puede poner audio')
    else:
        toDraw[2] = False

def makeYellow(activo = True, doStuff = True):
    '''
    plays audio corresponding to color, and queues the line to be drawn or not

    activo (bool) makes colour active or not
    '''
    global toDraw, audio4
    if activo:
        toDraw[3] = True
        try:
            audio4.play()
        except:
            print('no se puede poner audio')
    else:
        toDraw[3] = False

def makeColor(dm, activo = True, col = 1):
    '''
    plays audio corresponding to color, and queues the line to be drawn or not

    activo (bool) makes colour active or not
    col (int) converts int type to color type, to play corresponding audio
    '''
    global toDraw, audio1,audio2,audio3,audio4
    audios = [audio1,audio2,audio3,audio4]

    if activo:
        toDraw[col] = True
        try:
            audios[col].play()
        except:
            print('no se puede poner audio')
    else:
        toDraw[col] = False

toDraw = [False, False, False, False]

#                                            /$$             
#                                           | $$             
#   /$$$$$$  /$$    /$$ /$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$$
#  /$$__  $$|  $$  /$$//$$__  $$| $$__  $$|_  $$_/  /$$_____/
# | $$$$$$$$ \  $$/$$/| $$$$$$$$| $$  \ $$  | $$   |  $$$$$$ 
# | $$_____/  \  $$$/ | $$_____/| $$  | $$  | $$ /$$\____  $$
# |  $$$$$$$   \  $/  |  $$$$$$$| $$  | $$  |  $$$$//$$$$$$$/
#  \_______/    \_/    \_______/|__/  |__/   \___/ |_______/ 


@window.event
def on_draw():
    '''
    the main pyglet draw function
    '''
    window.clear()
    mainDrawBatch.draw()
    if toDraw[0]:
        redDrawBatch.draw()
    if toDraw[1]:
        greenDrawBatch.draw()
    if toDraw[2]:
        blueDrawBatch.draw()
    if toDraw[3]:
        yellowDrawBatch.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    '''
    mouse event handler
    '''
    global activeControlls, score, current, gameNotes

    if activeControlls:
        toSend = 0
        if x > window.get_size()[0] / 2 and y > window.get_size()[1] / 2:
            makeRed()
            toSend = 0
        elif x < window.get_size()[0] / 2 and y > window.get_size()[1] / 2:
            makeGreen()
            toSend = 1
        elif x < window.get_size()[0] / 2 and y < window.get_size()[1] / 2:
            makeBlue()
            toSend = 2
        else:
            makeYellow()
            toSend = 3

        getError = danny.regresar_valor(toSend, gameNotes, current)
        done = danny.estop(current, gameNotes)

        current += 1

        if done:
            timing = math.e ** (score * -0.1)
            scheduleGameSteps(timing, 0.1, 0.3)
            current = 0

        if getError:
            guillermo.reset_GameOrder()
            score = -1
            current = 0
            scheduleGameSteps(0.2, 0.1, 1)
    
@window.event
def on_mouse_release(x, y, button, modifiers):
    '''
    mouse event handler
    '''
    global toDraw,activeControlls

    toDraw[2] = False
    toDraw[1] = False
    toDraw[3] = False
    toDraw[0] = False

def startDraw(dm):
    '''
    create the initial draw to make everything look pretty
    '''
    initialDrawBatch.draw()

def gameLoop(dm):
    '''
    main game loop
    this loop is independant to pyglet loops, but gets called by it
    '''
    global score, scoreLabel
    
    scoreLabel.text = str(score)

def activateControlls(dm):
    '''
    make inputs active
    '''
    global activeControlls
    activeControlls = True
    pyglet.clock.schedule_interval(gameLoop, 1/120.0)

def deactivateControlls():
    '''
    deactivate all inputs
    '''
    global activeControlls
    activeControlls = False
    pyglet.clock.unschedule(gameLoop)

def scheduleGameSteps(timePerBlink, rest, endTimeDelay):
    '''
    deactivate controlls, and make the next sequence, at the end, reactivate controlls
    '''
    global score, gameNotes
    
    score += 1
    sleep(0.5)
    deactivateControlls()
    
    gameNotes = guillermo.Return_GameOrder(score)
    
    for i in range(len(gameNotes)):
        time = (timePerBlink + rest) * i
        pyglet.clock.schedule_once(makeColor, time , col = gameNotes[i])
        pyglet.clock.schedule_once(makeColor, time + timePerBlink, activo = False , col = gameNotes[i])
    
    pyglet.clock.schedule_once(activateControlls, len(gameNotes) * (timePerBlink + rest) + endTimeDelay)
    

gameNotes = [0,1,2,3,3,2,1,0]

activeControlls =  False
pyglet.clock.schedule_interval(gameLoop, 1/120.0)
scheduleGameSteps(0.2, 0.1, 1)

pyglet.app.run()
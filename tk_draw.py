# module to draw things with tkinter

from tkinter import *
import consts as Consts

DEBUG = False


def getInstance():
    ''' Returns a Tkinter instance for future Tkinter calls '''
    return Tk()


def clickHandler(event, gols):
    if DEBUG:
        print('click at x : (%d), y : (%d)' % (event.x, event.y))
    scaledPoint = scaleGraphicToBoard((event.x, event.y))
    if DEBUG:
        print('stupid scale, x : (%d), y : (%d)' % (scaledPoint[0],
                                                    scaledPoint[1]))
    """
    gols.setFrame(scaledPoint[0], scaledPoint[1])
    """


def keyboardHandler(event):
    if DEBUG:
        print('keystroke pressed : ', repr(event.char))


def updateHandler(instance, window, ids, gols):
    if DEBUG:
        print('update')
    gols.update()
    drawField(window, ids, gols)
    attachUpdater(instance, window, ids, gols)


def getWindow(instance, gols):
    ''' Returns a canvas object to draw on '''
    canvas = Canvas(instance, width=Consts.TK_WIDTH, height=Consts.TK_HEIGHT)
    canvas.bind('<Key>', keyboardHandler)
    canvas.bind('<ButtonPress-1>',
                lambda event, localGols=gols: clickHandler(event, localGols))
    canvas.pack()
    return canvas


def attachUpdater(instance, window, ids, gols):
    instance.after(Consts.TK_UPDATE_TIMER, updateHandler,
                   instance, window, ids, gols)


def attachMainloop(instance):
    ''' Calls Tkinter mainloop() function '''
    instance.mainloop()


def scaleBoardToGraphic(point):
    if len(point) == 2:
        for i in range(2):
            if not isinstance(point[i], int):
                raise Exception('bad point format')
        return ((point[0] * Consts.TK_WIDTH) / Consts.BOA_WIDTH,
                (point[1] * Consts.TK_HEIGHT) / Consts.BOA_HEIGHT)


def scaleGraphicToBoard(point):
    if len(point) == 2:
        for i in range(2):
            if (not isinstance(point[i], int)
                    and not isinstance(point[i], float)):
                raise Exception('bad point format')
        return (int((point[0] / Consts.TK_WIDTH) * Consts.BOA_WIDTH),
                int((point[1] / Consts.TK_HEIGHT) * Consts.BOA_HEIGHT))


def drawRect(window, x, y):
    sPoint = scaleBoardToGraphic((x, y))
    ePoint = scaleBoardToGraphic((x + 1, y + 1))
    if DEBUG:
        print('RECTANGLE:: start point : {}, end point : {}'.format(sPoint,
                                                                    ePoint))
    window.create_rectangle(sPoint[0],
                            sPoint[1],
                            ePoint[0],
                            ePoint[1],
                            outline=Consts.TK_COLOR_GREEN,
                            fill=Consts.TK_CELL_COLOR,
                            width=2)


def drawField(window, ids, gols):
    '''
    Update the field in the canvas on the window
    There is dead cells (white) and alive cells (black)
    '''

    # Reset background
    window.itemconfig(ids[0], fill=Consts.TK_BG_COLOR)

    # Update all cells
    for y in range(gols.field.height):
        for x in range(gols.field.width):
            frame = gols.field.getFrame(x, y)
            if frame in Consts.BOA_VALID_REPR:
                frameId = ids[1][(y * gols.field.width) + x]
                if frame == Consts.BOA_ALIVE_REPR:
                    window.itemconfig(frameId, outline=Consts.TK_COLOR_GREEN, fill=Consts.TK_CELL_COLOR, width=2)
                else:
                    window.itemconfig(frameId, outline=Consts.TK_BG_COLOR, fill=Consts.TK_BG_COLOR, width=0)

    # Update generation count on window
    window.itemconfig(ids[2], text=str(gols.generation), font=('Helvetica', '20'))

    return

def initWindow(window, gols):
    '''
    Draws the field in the canvas on the window
    There is dead cells (white) and alive cells (black)
    Init function returns all object ids needed for further graphic modifications
    '''

    backgroundId = window.create_rectangle(0, 0,
                                           Consts.TK_WIDTH, Consts.TK_HEIGHT,
                                           fill=Consts.TK_BG_COLOR)

    cellsIds = []

    for y in range(gols.field.height):
        for x in range(gols.field.width):
            frame = gols.field.getFrame(x, y)
            if frame in Consts.BOA_VALID_REPR:
                sPoint = scaleBoardToGraphic((x, y))
                ePoint = scaleBoardToGraphic((x + 1, y + 1))
                cellsIds.append(window.create_rectangle(sPoint[0],
                                                        sPoint[1],
                                                        ePoint[0],
                                                        ePoint[1],
                                                        outline=Consts.TK_COLOR_BLUE,
                                                        fill=Consts.TK_CELL_COLOR,
                                                        width=1))

    textId = window.create_text(10, 10, anchor="nw", fill="white")
    window.itemconfig(textId, text=str(gols.generation), font=('Helvetica', '20'))

    return (backgroundId, cellsIds, textId)

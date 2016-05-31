#!/usr/bin/python

## consts placeholder

''' main consts '''

USAGE   = "USAGE:\t./gol [filename]"

''' board consts '''

BOA_HEIGHT          = 75
BOA_WIDTH           = 75
BOA_FIELD_TYPECODE  = 'B'
BOA_DEAD_REPR       = 0
BOA_ALIVE_REPR      = 1
BOA_VALID_REPR      = [BOA_DEAD_REPR,
                       BOA_ALIVE_REPR]
BOA_MAX_GENERATION  = 300

''' random '''

DISTRIBUTION        = 0.5

''' tkinter consts '''

TK_WIDTH            = 700
TK_HEIGHT           = 700
TK_COLOR_WHITE      = '#ffffff'
TK_COLOR_BLACK      = '#000000'
TK_COLOR_RED        = '#ff0000'
TK_COLOR_GREEN      = '#00ff00'
TK_COLOR_BLUE       = '#0000ff'
TK_BG_COLOR         = TK_COLOR_BLACK
TK_CELL_COLOR       = TK_COLOR_BLACK
TK_UPDATE_TIMER     = 100

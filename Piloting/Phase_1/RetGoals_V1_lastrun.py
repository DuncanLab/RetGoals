#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Wed Feb 19 09:13:22 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'RetGoals_V1'  # from the Builder filename that created this script
expInfo = {
    'participant': '000',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expName, expInfo['participant'], expInfo['session'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Piloting/RetGoals_V1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "EAStimLoader" ---
# Run 'Begin Experiment' code from EALoaderCode
ea_stim = []
ea_stim_corr_keys = []
ea_stim_magnitude = []
ea_stim_spec = []
ea_stim_big = []

# --- Initialize components for Routine "EncStimLoader" ---
# Run 'Begin Experiment' code from EAStimLoaderCode
enc_stim = []
enc_stim_corr_keys = []
enc_stim_spec = []

# --- Initialize components for Routine "IAStimLoader" ---
# Run 'Begin Experiment' code from IAStimLoaderCode
ia_stim = []
ia_stim_corr_keys = []
ia_stim_spec = []
ia_stim_magnitude = []
ia_stim_hasneg = []

# --- Initialize components for Routine "RetStimLoader" ---
# Run 'Begin Experiment' code from RetStimLoaderCode
ret_stim = []
ret_enc_stimname = []
ret_stim_corr_keys = []
ret_stim_spec = []

# --- Initialize components for Routine "StimShuffle" ---
# Run 'Begin Experiment' code from ShuffleCode
ea_stim_counter = 0
enc_stim_counter = 0
ia_stim_counter = 0
ret_stim_counter = 0
shuffled_order = list(range(300))
ret_shuf_prac = []
ret_shuf1 = []
ret_shuf2 = []
ret_shuf3 = []
ret_shuf4 = []
ret_shuf5 = []
ret_shuf6 = []
ret_shuf7 = []
ret_shuf8 = []
ret_shuf9 = []
ret_shuf10 = []

# --- Initialize components for Routine "WelcomeScreen" ---
welcomeText = visual.TextStim(win=win, name='welcomeText',
    text='Welcome, and thank you for agreeing to participate in our study! \n\nDuring this study, you will complete a series of tasks. There will be 4 tasks per block, and a total of 10 blocks. 5 of the blocks will be roughly 12 minutes each, and 5 of the blocks will be roughly 3 minutes each. Between each block, you will have a 30 second break. Halfway through the experiment, you will have a self-paced break, up to three minutes. If at any point you need to stop the experiment, please wait until the end of the current task, then ask the experimenter for assistance. \n\nPress the spacebar to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcomeKey = keyboard.Keyboard()

# --- Initialize components for Routine "WelcomeScreen2" ---
welcomeText2 = visual.TextStim(win=win, name='welcomeText2',
    text='You will first go through a set of practice trials to get the hang of each task. Before we begin, place the fingers of your dominant hand over the “1”, “2”, “3”, and “4” keys on the keyboard. Press any of the four keys to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcomeKey2 = keyboard.Keyboard()

# --- Initialize components for Routine "EAPracticeInstructions" ---
EAPracticeText1 = visual.TextStim(win=win, name='EAPracticeText1',
    text='Size Judgment Task',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
EAPracticeText2 = visual.TextStim(win=win, name='EAPracticeText2',
    text='For this task, you will see a set of shapes on screen. Some of the shapes will be large, and some of the shapes will be small. At the top of the screen, you will see an equation that reads “big _ small”. You will be prompted to fill in the symbol that makes the equation correct. \n\nEach of the symbols on the bottom of the screen corresponds to the four keys: ? is 1, > is 2, = is 3, and < is 4. If there are more big shapes than small shapes, the correct answer is > (press button “2”). If there are fewer big shapes than small shapes, the correct answer is < (press button “4”). If they are equal, the correct answer is = (press button “3”). If you cannot tell or are not confident, feel free to answer with ? (press button “1”). \n\nPress space to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
EAPracticeRespText = visual.TextStim(win=win, name='EAPracticeRespText',
    text='?     >      =      <\n1     2      3      4',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
EAPracticeKey = keyboard.Keyboard()

# --- Initialize components for Routine "EAPracticeInstructions2" ---
EAPractice2Text = visual.TextStim(win=win, name='EAPractice2Text',
    text='You will now practice the task without a time constraint. The shapes will appear on screen for 1.5 seconds, after which you will be able to make a response. Press 1 to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
EAPractice2Key = keyboard.Keyboard()

# --- Initialize components for Routine "EAPractice1" ---
# Run 'Begin Experiment' code from EAPractice1Code
EA_image_fp = ''
EAPractice1_Feedback = ''
EAPractice1_corrkey = ''
EAPractice1Text1 = visual.TextStim(win=win, name='EAPractice1Text1',
    text='',
    font='Open Sans',
    pos=(0, 0.4), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
EAPractice1Text2 = visual.TextStim(win=win, name='EAPractice1Text2',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
EAPractice1Stim = visual.ImageStim(
    win=win,
    name='EAPractice1Stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
EAPractice1Resp = keyboard.Keyboard()

# --- Initialize components for Routine "EAPostPractice1" ---
EAPostPractice1Text = visual.TextStim(win=win, name='EAPostPractice1Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
EAPostPractice1Resp = keyboard.Keyboard()

# --- Initialize components for Routine "ISI" ---
FixCross = visual.TextStim(win=win, name='FixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "EATrial" ---
# Run 'Begin Experiment' code from EATrialCode
EA_Feedback = ''
EA_corrkey = ''
EATrialText1 = visual.TextStim(win=win, name='EATrialText1',
    text='',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
EATrialText2 = visual.TextStim(win=win, name='EATrialText2',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
EATrialStim = visual.ImageStim(
    win=win,
    name='EATrialStim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
EATrialResp = keyboard.Keyboard()

# --- Initialize components for Routine "EAPracticeEnd" ---
EAPracticeEndText = visual.TextStim(win=win, name='EAPracticeEndText',
    text="Well Done! We'll now move on to the next set of task instructions and practice. Press 1 to continue.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
EAPracticeEndKey = keyboard.Keyboard()

# --- Initialize components for Routine "IAPracticeInstructions" ---
IAPracticeInstructions1Text1 = visual.TextStim(win=win, name='IAPracticeInstructions1Text1',
    text='Arithmetic Task',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
IAPracticeInstructions1Text2 = visual.TextStim(win=win, name='IAPracticeInstructions1Text2',
    text='For this task, you will see a set of math problems on screen, one on the left and one on the right. The blank space in the middle is the symbol that makes the equation correct. You will be prompted to fill in the symbol that makes the equation correct. \n\nEach of the symbols on the bottom of the screen corresponds to the four keys: ? is 1, > is 2, = is 3, and < is 4. If the answer to the equation on the left is greater than the answer to the equation on the right, the correct answer is > (press button “2”). If the answer to the equation on the left is less than the answer to the equation on the right, the correct answer is < (press button “4”). If they are equal, the correct answer is = (press button “3”). If you cannot tell or are not confident, feel free to answer with ? (press button “1”). \n\nPress space to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
IAPracticeInstructions1RespText = visual.TextStim(win=win, name='IAPracticeInstructions1RespText',
    text='?     >      =      <\n1     2      3      4',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
IAPracticeInstructions1Resp = keyboard.Keyboard()

# --- Initialize components for Routine "IAPracticeInstructions2" ---
IAPracticeInstructions2Text = visual.TextStim(win=win, name='IAPracticeInstructions2Text',
    text='You will now practice the task without a time constraint. The problems will appear on screen for 1.5 seconds, after which you will be able to make a response. Press 1 to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
IAPracticeInstructions2Resp = keyboard.Keyboard()

# --- Initialize components for Routine "IAPractice1" ---
# Run 'Begin Experiment' code from IAPractice1Code
IA_image_fp = ''
IAPractice1_Feedback = ''
IAPractice1_corrkey = ''
IAPractice1Text1 = visual.TextStim(win=win, name='IAPractice1Text1',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
IAPractice1Stim = visual.ImageStim(
    win=win,
    name='IAPractice1Stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.9, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
IAPractice1Resp = keyboard.Keyboard()

# --- Initialize components for Routine "IAPostPractice1" ---
IAPractice1Feedback = visual.TextStim(win=win, name='IAPractice1Feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
IAPostPractice1Resp = keyboard.Keyboard()

# --- Initialize components for Routine "ISI" ---
FixCross = visual.TextStim(win=win, name='FixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "IATrial" ---
# Run 'Begin Experiment' code from IATrialCode
IA_corrkey = ''
IATrialRespText = visual.TextStim(win=win, name='IATrialRespText',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
IATrialStim = visual.ImageStim(
    win=win,
    name='IATrialStim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.9, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
IATrialResp = keyboard.Keyboard()

# --- Initialize components for Routine "IAPracticeEnd" ---
IAPracticeEndText = visual.TextStim(win=win, name='IAPracticeEndText',
    text="Well Done! We'll now move on to the next set of task instructions and practice. Press 1 to continue.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
IAPracticeEndResp = keyboard.Keyboard()

# --- Initialize components for Routine "EncPracticeInstructions" ---
EncPracticeInstructionsText1 = visual.TextStim(win=win, name='EncPracticeInstructionsText1',
    text='Comparison & Learning Task',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
EncPracticeInstructionsText2 = visual.TextStim(win=win, name='EncPracticeInstructionsText2',
    text='For this task, you will see two pictures on screen. The pictures on the left will randomly repeat throughout the experiment, but the pictures on the right will always be new. \n\nYour job is to study the two images. You will be asked to remember which images were shown together in a subsequent task. \n\nTo help you remember, you will also make a judgment about the size of the objects in relation to one another. This will help you form an association between the objects. \n\nPlease make the judgment based off of the size of the image on screen, not the size of these objects in the real world. If the image on the left is larger than the image on the right, the correct answer is > (press button “2”). If the image on the left is smaller than the image on the right, the correct answer is < (press button “4”). If they are equal, the correct answer is = (press button “3”). If you cannot tell or are not confident, feel free to answer with ? (press button “1”). \n\nRemember, your memory for these items will be tested later, so be sure to pay attention! \n\nPress space to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
EncPracticeInstructionsRespText = visual.TextStim(win=win, name='EncPracticeInstructionsRespText',
    text='?     >      =      <\n1     2      3      4',
    font='Open Sans',
    pos=(0,-0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
EncPracticeInstructionsResp = keyboard.Keyboard()

# --- Initialize components for Routine "EncPracticeInstructions2" ---
EncPracticeInstructions2Text = visual.TextStim(win=win, name='EncPracticeInstructions2Text',
    text='You will now practice the task without a time constraint. The images will appear on screen for 1.5 seconds, after which you will be able to make a response. Press 1 to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
EncPracticeInstructions2Resp = keyboard.Keyboard()

# --- Initialize components for Routine "EncPractice1" ---
# Run 'Begin Experiment' code from EncPractice1Code
Enc_image_fp = ''
EncPractice1_Feedback = ''
EncPractice1_corrkey = ''
EncPractice1Resp = keyboard.Keyboard()
EncPractice1Stim = visual.ImageStim(
    win=win,
    name='EncPractice1Stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.0, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
EncPractice1RespText = visual.TextStim(win=win, name='EncPractice1RespText',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "EncPostPractice1" ---
EncPractice1Feedback = visual.TextStim(win=win, name='EncPractice1Feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
EncPractice1FeedbackResp = keyboard.Keyboard()

# --- Initialize components for Routine "ISI" ---
FixCross = visual.TextStim(win=win, name='FixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "EncTrial" ---
# Run 'Begin Experiment' code from EncTrialCode
Enc_corrkey = ''
EncImage = visual.ImageStim(
    win=win,
    name='EncImage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.0, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
EncTrialRespText = visual.TextStim(win=win, name='EncTrialRespText',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
EncTrialResp = keyboard.Keyboard()

# --- Initialize components for Routine "EncPracticeEnd" ---
EncPracticeEndText = visual.TextStim(win=win, name='EncPracticeEndText',
    text="Well Done! We'll now move on to the next set of task instructions and practice. Press 1 to continue.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
EncPracticeEndResp = keyboard.Keyboard()

# --- Initialize components for Routine "RetPracticeInstructions" ---
RetPracticeInstructionsText1 = visual.TextStim(win=win, name='RetPracticeInstructionsText1',
    text='Memory Task',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
RetPracticeInstructionsText2 = visual.TextStim(win=win, name='RetPracticeInstructionsText2',
    text='For this task, your memory for the images shown during the learning task will be tested. You will see one image on screen, and you will be asked which of the images at the bottom of the screen was previously shown with it.\n\nIf you think the image was shown with the berries,  press button “2”. If you think the image was shown with the truck,  press button “3”. If you think the image was shown with the house,  press button “4”. If you cannot tell or are not confident, feel free to answer with ? (press button “1”).\n\nPress space to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
RetPracticeInstructionsResp = keyboard.Keyboard()
RetPracticeInstructions1Berry = visual.ImageStim(
    win=win,
    name='RetPracticeInstructions1Berry', 
    image='/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Repeating_Ret_Stim/fruit.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, -0.35), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
RetPracticeInstructions1Question = visual.TextStim(win=win, name='RetPracticeInstructions1Question',
    text='?',
    font='Open Sans',
    pos=(-0.375, -0.35), height=0.065, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
RetPracticeInstructions1Truck = visual.ImageStim(
    win=win,
    name='RetPracticeInstructions1Truck', 
    image='/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Repeating_Ret_Stim/vehicle.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.125, -0.35), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
RetPracticeInstructions1House = visual.ImageStim(
    win=win,
    name='RetPracticeInstructions1House', 
    image='/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Repeating_Ret_Stim/building.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.375, -0.35), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
RetPracticeInstructionsNumGuide1 = visual.TextStim(win=win, name='RetPracticeInstructionsNumGuide1',
    text='1',
    font='Open Sans',
    pos=(-0.375, -0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
RetPracticeInstructionsNumGuide2 = visual.TextStim(win=win, name='RetPracticeInstructionsNumGuide2',
    text='2',
    font='Open Sans',
    pos=(-0.125, -0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
RetPracticeInstructionsNumGuide3 = visual.TextStim(win=win, name='RetPracticeInstructionsNumGuide3',
    text='3',
    font='Open Sans',
    pos=(0.125, -0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
RetPracticeInstructionsNumGuide4 = visual.TextStim(win=win, name='RetPracticeInstructionsNumGuide4',
    text='4',
    font='Open Sans',
    pos=(0.375, -0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "RetPracticeInstructions2" ---
RetPracticeInstructions2Text = visual.TextStim(win=win, name='RetPracticeInstructions2Text',
    text='You will now practice the task without a time constraint. An image will appear on screen for 1.5 seconds, after which you will be able to make a response. Press 1 to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
RetPracticeInstructions2Resp = keyboard.Keyboard()

# --- Initialize components for Routine "RetPractice1" ---
# Run 'Begin Experiment' code from RetPractice1Code
Ret_image_fp = ''
RetPractice1_Feedback = ''
RetPractice1_corrkey = ''
RetPractice1Stim = visual.ImageStim(
    win=win,
    name='RetPractice1Stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
RetPractice1Resp = keyboard.Keyboard()
RetPractice1Berry = visual.ImageStim(
    win=win,
    name='RetPractice1Berry', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, -0.35), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
RetPractice1Question = visual.TextStim(win=win, name='RetPractice1Question',
    text='',
    font='Open Sans',
    pos=(-0.375, -0.35), height=0.065, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
RetPractice1Truck = visual.ImageStim(
    win=win,
    name='RetPractice1Truck', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, -0.35), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
RetPractice1House = visual.ImageStim(
    win=win,
    name='RetPractice1House', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, -0.35), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "RetPostPractice1" ---
RetPostPractice1Text = visual.TextStim(win=win, name='RetPostPractice1Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
RetPostPractice1Resp = keyboard.Keyboard()

# --- Initialize components for Routine "ISI" ---
FixCross = visual.TextStim(win=win, name='FixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "RetTrial" ---
# Run 'Begin Experiment' code from RetTrialCode
Ret_corrkey = ''
RetTrialStim = visual.ImageStim(
    win=win,
    name='RetTrialStim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
RetTrialResp = keyboard.Keyboard()
RetTrialQuestion = visual.TextStim(win=win, name='RetTrialQuestion',
    text='',
    font='Open Sans',
    pos=(-0.375, -0.35), height=0.065, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
RetTrialBerry = visual.ImageStim(
    win=win,
    name='RetTrialBerry', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, -0.35), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
RetTrialTruck = visual.ImageStim(
    win=win,
    name='RetTrialTruck', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, -0.35), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
RetTrialHouse = visual.ImageStim(
    win=win,
    name='RetTrialHouse', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, -0.35), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "RetPracticeEnd" ---
RetPracticeEndText = visual.TextStim(win=win, name='RetPracticeEndText',
    text="Well Done! \n\nYou're now ready to begin the study. If you have any questions, please ask the experimenter now. Please make sure that your cell phone is turned off and put away. If you need to use the washroom, please do so now. \n\nPress 1 to begin the study.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
RetPracticeEndResp = keyboard.Keyboard()

# --- Initialize components for Routine "EATaskInstructions" ---
# Run 'Begin Experiment' code from Block1Counter
block_counter = 0
EATaskInstructionsText1 = visual.TextStim(win=win, name='EATaskInstructionsText1',
    text='Size Judgment Task',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
EATaskInstructionsText2 = visual.TextStim(win=win, name='EATaskInstructionsText2',
    text='For this task, you will see a set of shapes on screen. Some of the shapes will be large, and some of the shapes will be small. At the top of the screen, you will see an equation that reads “big _ small”. You will be prompted to fill in the symbol that makes the equation correct (>, =, <). \n\nRemember, you have a limited time to make your response. Please try to make a response on each trial. If you are unsure of the answer, feel free to respond with ? (press button 1).\n\nThe task will begin shortly.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "ISI" ---
FixCross = visual.TextStim(win=win, name='FixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "EATrial" ---
# Run 'Begin Experiment' code from EATrialCode
EA_Feedback = ''
EA_corrkey = ''
EATrialText1 = visual.TextStim(win=win, name='EATrialText1',
    text='',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
EATrialText2 = visual.TextStim(win=win, name='EATrialText2',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
EATrialStim = visual.ImageStim(
    win=win,
    name='EATrialStim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
EATrialResp = keyboard.Keyboard()

# --- Initialize components for Routine "EncTaskInstructions" ---
EncTaskInstructionsText1 = visual.TextStim(win=win, name='EncTaskInstructionsText1',
    text='',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
EncTaskInstructionsText2 = visual.TextStim(win=win, name='EncTaskInstructionsText2',
    text='For this task, you will see two pictures on screen. Your job is to study the two images. You will be asked to remember which images were shown together in a subsequent task. \n\nTo help you remember, you will also make a judgment about the size of the objects in relation to one another (>, =, <). Please make the judgment based off of the size of the image on screen, not the size of these objects in the real world. If you cannot tell or are not confident, feel free to answer with ? (press button “1”). \n\nRemember, your memory for these items will be tested later, so be sure to pay attention! \n\nThe task will begin shortly.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ISI" ---
FixCross = visual.TextStim(win=win, name='FixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "EncTrial" ---
# Run 'Begin Experiment' code from EncTrialCode
Enc_corrkey = ''
EncImage = visual.ImageStim(
    win=win,
    name='EncImage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.0, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
EncTrialRespText = visual.TextStim(win=win, name='EncTrialRespText',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
EncTrialResp = keyboard.Keyboard()

# --- Initialize components for Routine "IATaskInstructions" ---
IATaskInstructionsText1 = visual.TextStim(win=win, name='IATaskInstructionsText1',
    text='Arithmetic Task',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
IATaskInstructionsText2 = visual.TextStim(win=win, name='IATaskInstructionsText2',
    text='For this task, you will see a set of math problems on screen, one on the left and one on the right. The blank space in the middle is the symbol that makes the equation correct. You will be prompted to fill in the symbol that makes the equation correct (>, =, <). Please try to make a response on every trial. If you cannot tell or are not confident, feel free to answer with ? (press button “1”). \n\nThe task will begin shortly.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ISI" ---
FixCross = visual.TextStim(win=win, name='FixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "IATrial" ---
# Run 'Begin Experiment' code from IATrialCode
IA_corrkey = ''
IATrialRespText = visual.TextStim(win=win, name='IATrialRespText',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
IATrialStim = visual.ImageStim(
    win=win,
    name='IATrialStim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.9, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
IATrialResp = keyboard.Keyboard()

# --- Initialize components for Routine "RetTaskInstructions" ---
RetTaskInstructionsText1 = visual.TextStim(win=win, name='RetTaskInstructionsText1',
    text='Memory Task',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
RetTaskInstructionsText2 = visual.TextStim(win=win, name='RetTaskInstructionsText2',
    text='For this task, your memory for the images shown during the learning task will be tested. You will see one image on screen, and you will be asked which of the images at the bottom of the screen was previously shown with it (berries, truck, house). Please try to make a response on every trial. If you cannot tell or are not confident, feel free to answer with ? (press button “1”).\n\nThe task will begin shortly.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ISI" ---
FixCross = visual.TextStim(win=win, name='FixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "RetTrial" ---
# Run 'Begin Experiment' code from RetTrialCode
Ret_corrkey = ''
RetTrialStim = visual.ImageStim(
    win=win,
    name='RetTrialStim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
RetTrialResp = keyboard.Keyboard()
RetTrialQuestion = visual.TextStim(win=win, name='RetTrialQuestion',
    text='',
    font='Open Sans',
    pos=(-0.375, -0.35), height=0.065, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
RetTrialBerry = visual.ImageStim(
    win=win,
    name='RetTrialBerry', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, -0.35), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
RetTrialTruck = visual.ImageStim(
    win=win,
    name='RetTrialTruck', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, -0.35), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
RetTrialHouse = visual.ImageStim(
    win=win,
    name='RetTrialHouse', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, -0.35), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "Block1End" ---
# Run 'Begin Experiment' code from Block1EndCode
block1endtext = ''
Block1EndText = visual.TextStim(win=win, name='Block1EndText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Block2Break" ---
Block2BreakText = visual.TextStim(win=win, name='Block2BreakText',
    text='You have finished the first set of blocks! You will now have a self-paced break before the start of the next block, up to three minutes long. Please refrain from using technology during the break. The second set of blocks will take approximately 15 minutes to complete.\n\nPress 1 when you are ready to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Block2BreakKey = keyboard.Keyboard()

# --- Initialize components for Routine "EATaskInstructions" ---
# Run 'Begin Experiment' code from Block1Counter
block_counter = 0
EATaskInstructionsText1 = visual.TextStim(win=win, name='EATaskInstructionsText1',
    text='Size Judgment Task',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
EATaskInstructionsText2 = visual.TextStim(win=win, name='EATaskInstructionsText2',
    text='For this task, you will see a set of shapes on screen. Some of the shapes will be large, and some of the shapes will be small. At the top of the screen, you will see an equation that reads “big _ small”. You will be prompted to fill in the symbol that makes the equation correct (>, =, <). \n\nRemember, you have a limited time to make your response. Please try to make a response on each trial. If you are unsure of the answer, feel free to respond with ? (press button 1).\n\nThe task will begin shortly.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "ISI" ---
FixCross = visual.TextStim(win=win, name='FixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "EATrial" ---
# Run 'Begin Experiment' code from EATrialCode
EA_Feedback = ''
EA_corrkey = ''
EATrialText1 = visual.TextStim(win=win, name='EATrialText1',
    text='',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
EATrialText2 = visual.TextStim(win=win, name='EATrialText2',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
EATrialStim = visual.ImageStim(
    win=win,
    name='EATrialStim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
EATrialResp = keyboard.Keyboard()

# --- Initialize components for Routine "EncTaskInstructions" ---
EncTaskInstructionsText1 = visual.TextStim(win=win, name='EncTaskInstructionsText1',
    text='',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
EncTaskInstructionsText2 = visual.TextStim(win=win, name='EncTaskInstructionsText2',
    text='For this task, you will see two pictures on screen. Your job is to study the two images. You will be asked to remember which images were shown together in a subsequent task. \n\nTo help you remember, you will also make a judgment about the size of the objects in relation to one another (>, =, <). Please make the judgment based off of the size of the image on screen, not the size of these objects in the real world. If you cannot tell or are not confident, feel free to answer with ? (press button “1”). \n\nRemember, your memory for these items will be tested later, so be sure to pay attention! \n\nThe task will begin shortly.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ISI" ---
FixCross = visual.TextStim(win=win, name='FixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "EncTrial" ---
# Run 'Begin Experiment' code from EncTrialCode
Enc_corrkey = ''
EncImage = visual.ImageStim(
    win=win,
    name='EncImage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.0, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
EncTrialRespText = visual.TextStim(win=win, name='EncTrialRespText',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
EncTrialResp = keyboard.Keyboard()

# --- Initialize components for Routine "IATaskInstructions" ---
IATaskInstructionsText1 = visual.TextStim(win=win, name='IATaskInstructionsText1',
    text='Arithmetic Task',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
IATaskInstructionsText2 = visual.TextStim(win=win, name='IATaskInstructionsText2',
    text='For this task, you will see a set of math problems on screen, one on the left and one on the right. The blank space in the middle is the symbol that makes the equation correct. You will be prompted to fill in the symbol that makes the equation correct (>, =, <). Please try to make a response on every trial. If you cannot tell or are not confident, feel free to answer with ? (press button “1”). \n\nThe task will begin shortly.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ISI" ---
FixCross = visual.TextStim(win=win, name='FixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "IATrial" ---
# Run 'Begin Experiment' code from IATrialCode
IA_corrkey = ''
IATrialRespText = visual.TextStim(win=win, name='IATrialRespText',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
IATrialStim = visual.ImageStim(
    win=win,
    name='IATrialStim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.9, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
IATrialResp = keyboard.Keyboard()

# --- Initialize components for Routine "RetTaskInstructions" ---
RetTaskInstructionsText1 = visual.TextStim(win=win, name='RetTaskInstructionsText1',
    text='Memory Task',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
RetTaskInstructionsText2 = visual.TextStim(win=win, name='RetTaskInstructionsText2',
    text='For this task, your memory for the images shown during the learning task will be tested. You will see one image on screen, and you will be asked which of the images at the bottom of the screen was previously shown with it (berries, truck, house). Please try to make a response on every trial. If you cannot tell or are not confident, feel free to answer with ? (press button “1”).\n\nThe task will begin shortly.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ISI" ---
FixCross = visual.TextStim(win=win, name='FixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "RetTrial" ---
# Run 'Begin Experiment' code from RetTrialCode
Ret_corrkey = ''
RetTrialStim = visual.ImageStim(
    win=win,
    name='RetTrialStim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
RetTrialResp = keyboard.Keyboard()
RetTrialQuestion = visual.TextStim(win=win, name='RetTrialQuestion',
    text='',
    font='Open Sans',
    pos=(-0.375, -0.35), height=0.065, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
RetTrialBerry = visual.ImageStim(
    win=win,
    name='RetTrialBerry', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, -0.35), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
RetTrialTruck = visual.ImageStim(
    win=win,
    name='RetTrialTruck', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, -0.35), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
RetTrialHouse = visual.ImageStim(
    win=win,
    name='RetTrialHouse', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, -0.35), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "Block2End" ---
# Run 'Begin Experiment' code from Block2EndCode
block2endtext = ''
Block2EndText = visual.TextStim(win=win, name='Block2EndText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
EALoadLoop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/ExAttn_sheet.xlsx'),
    seed=None, name='EALoadLoop')
thisExp.addLoop(EALoadLoop)  # add the loop to the experiment
thisEALoadLoop = EALoadLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEALoadLoop.rgb)
if thisEALoadLoop != None:
    for paramName in thisEALoadLoop:
        exec('{} = thisEALoadLoop[paramName]'.format(paramName))

for thisEALoadLoop in EALoadLoop:
    currentLoop = EALoadLoop
    # abbreviate parameter names if possible (e.g. rgb = thisEALoadLoop.rgb)
    if thisEALoadLoop != None:
        for paramName in thisEALoadLoop:
            exec('{} = thisEALoadLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "EAStimLoader" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from EALoaderCode
    ea_stim.append(stim_name)
    ea_stim_corr_keys.append(corr_key)
    ea_stim_magnitude.append(magnitude)
    ea_stim_spec.append(stim_spec)
    ea_stim_big.append(num_big)
    # keep track of which components have finished
    EAStimLoaderComponents = []
    for thisComponent in EAStimLoaderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EAStimLoader" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EAStimLoaderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EAStimLoader" ---
    for thisComponent in EAStimLoaderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "EAStimLoader" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'EALoadLoop'


# set up handler to look after randomisation of conditions etc
EncLoadLoop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Enc_sheet.xlsx'),
    seed=None, name='EncLoadLoop')
thisExp.addLoop(EncLoadLoop)  # add the loop to the experiment
thisEncLoadLoop = EncLoadLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEncLoadLoop.rgb)
if thisEncLoadLoop != None:
    for paramName in thisEncLoadLoop:
        exec('{} = thisEncLoadLoop[paramName]'.format(paramName))

for thisEncLoadLoop in EncLoadLoop:
    currentLoop = EncLoadLoop
    # abbreviate parameter names if possible (e.g. rgb = thisEncLoadLoop.rgb)
    if thisEncLoadLoop != None:
        for paramName in thisEncLoadLoop:
            exec('{} = thisEncLoadLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "EncStimLoader" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from EAStimLoaderCode
    enc_stim.append(stim_name)
    enc_stim_corr_keys.append(corr_key)
    enc_stim_spec.append(stim_spec)
    # keep track of which components have finished
    EncStimLoaderComponents = []
    for thisComponent in EncStimLoaderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EncStimLoader" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EncStimLoaderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EncStimLoader" ---
    for thisComponent in EncStimLoaderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "EncStimLoader" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'EncLoadLoop'


# set up handler to look after randomisation of conditions etc
IALoadLoop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Int_sheet.xlsx'),
    seed=None, name='IALoadLoop')
thisExp.addLoop(IALoadLoop)  # add the loop to the experiment
thisIALoadLoop = IALoadLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIALoadLoop.rgb)
if thisIALoadLoop != None:
    for paramName in thisIALoadLoop:
        exec('{} = thisIALoadLoop[paramName]'.format(paramName))

for thisIALoadLoop in IALoadLoop:
    currentLoop = IALoadLoop
    # abbreviate parameter names if possible (e.g. rgb = thisIALoadLoop.rgb)
    if thisIALoadLoop != None:
        for paramName in thisIALoadLoop:
            exec('{} = thisIALoadLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "IAStimLoader" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from IAStimLoaderCode
    ia_stim.append(stim_name)
    ia_stim_corr_keys.append(corr_key)
    ia_stim_spec.append(stim_spec)
    ia_stim_magnitude.append(magnitude)
    ia_stim_hasneg.append(has_neg_ans)
    # keep track of which components have finished
    IAStimLoaderComponents = []
    for thisComponent in IAStimLoaderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "IAStimLoader" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IAStimLoaderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "IAStimLoader" ---
    for thisComponent in IAStimLoaderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "IAStimLoader" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'IALoadLoop'


# set up handler to look after randomisation of conditions etc
RetLoadLoop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Ret_sheet.xlsx'),
    seed=None, name='RetLoadLoop')
thisExp.addLoop(RetLoadLoop)  # add the loop to the experiment
thisRetLoadLoop = RetLoadLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRetLoadLoop.rgb)
if thisRetLoadLoop != None:
    for paramName in thisRetLoadLoop:
        exec('{} = thisRetLoadLoop[paramName]'.format(paramName))

for thisRetLoadLoop in RetLoadLoop:
    currentLoop = RetLoadLoop
    # abbreviate parameter names if possible (e.g. rgb = thisRetLoadLoop.rgb)
    if thisRetLoadLoop != None:
        for paramName in thisRetLoadLoop:
            exec('{} = thisRetLoadLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "RetStimLoader" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from RetStimLoaderCode
    ret_stim.append(stim_name)
    ret_enc_stimname.append(enc_stimname)
    ret_stim_corr_keys.append(corr_key)
    ret_stim_spec.append(stim_spec)
    # keep track of which components have finished
    RetStimLoaderComponents = []
    for thisComponent in RetStimLoaderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "RetStimLoader" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RetStimLoaderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RetStimLoader" ---
    for thisComponent in RetStimLoaderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "RetStimLoader" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'RetLoadLoop'


# --- Prepare to start Routine "StimShuffle" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from ShuffleCode
shuffle(shuffled_order)
ret_shuf_prac = shuffled_order[0:5]
shuffle(ret_shuf_prac)
ret_shuf1 = shuffled_order[5:45]
shuffle(ret_shuf1)
ret_shuf2 = shuffled_order[45:85]
shuffle(ret_shuf2)
ret_shuf3 = shuffled_order[85:125]
shuffle(ret_shuf3)
ret_shuf4 = shuffled_order[125:165]
shuffle(ret_shuf4)
ret_shuf5 = shuffled_order[165:205]
shuffle(ret_shuf5)
ret_shuf6 = shuffled_order[205:215]
shuffle(ret_shuf6)
ret_shuf7 = shuffled_order[215:225]
shuffle(ret_shuf7)
ret_shuf8 = shuffled_order[225:235]
shuffle(ret_shuf8)
ret_shuf9 = shuffled_order[235:245]
shuffle(ret_shuf9)
ret_shuf10 = shuffled_order[245:255]
shuffle(ret_shuf10)
ret_shuffled_order = ret_shuf_prac + ret_shuf1 + ret_shuf2 + ret_shuf3 + ret_shuf4 + ret_shuf5 + ret_shuf6 + ret_shuf7 + ret_shuf8 + ret_shuf9 + ret_shuf10
# keep track of which components have finished
StimShuffleComponents = []
for thisComponent in StimShuffleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "StimShuffle" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StimShuffleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "StimShuffle" ---
for thisComponent in StimShuffleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "StimShuffle" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "WelcomeScreen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
welcomeKey.keys = []
welcomeKey.rt = []
_welcomeKey_allKeys = []
# keep track of which components have finished
WelcomeScreenComponents = [welcomeText, welcomeKey]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "WelcomeScreen" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeText* updates
    if welcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeText.frameNStart = frameN  # exact frame index
        welcomeText.tStart = t  # local t and not account for scr refresh
        welcomeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcomeText.started')
        welcomeText.setAutoDraw(True)
    
    # *welcomeKey* updates
    waitOnFlip = False
    if welcomeKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeKey.frameNStart = frameN  # exact frame index
        welcomeKey.tStart = t  # local t and not account for scr refresh
        welcomeKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeKey, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcomeKey.started')
        welcomeKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcomeKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcomeKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcomeKey.status == STARTED and not waitOnFlip:
        theseKeys = welcomeKey.getKeys(keyList=['space'], waitRelease=False)
        _welcomeKey_allKeys.extend(theseKeys)
        if len(_welcomeKey_allKeys):
            welcomeKey.keys = _welcomeKey_allKeys[-1].name  # just the last key pressed
            welcomeKey.rt = _welcomeKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "WelcomeScreen" ---
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if welcomeKey.keys in ['', [], None]:  # No response was made
    welcomeKey.keys = None
thisExp.addData('welcomeKey.keys',welcomeKey.keys)
if welcomeKey.keys != None:  # we had a response
    thisExp.addData('welcomeKey.rt', welcomeKey.rt)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "WelcomeScreen2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
welcomeKey2.keys = []
welcomeKey2.rt = []
_welcomeKey2_allKeys = []
# keep track of which components have finished
WelcomeScreen2Components = [welcomeText2, welcomeKey2]
for thisComponent in WelcomeScreen2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "WelcomeScreen2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeText2* updates
    if welcomeText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeText2.frameNStart = frameN  # exact frame index
        welcomeText2.tStart = t  # local t and not account for scr refresh
        welcomeText2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeText2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcomeText2.started')
        welcomeText2.setAutoDraw(True)
    
    # *welcomeKey2* updates
    waitOnFlip = False
    if welcomeKey2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeKey2.frameNStart = frameN  # exact frame index
        welcomeKey2.tStart = t  # local t and not account for scr refresh
        welcomeKey2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeKey2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcomeKey2.started')
        welcomeKey2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcomeKey2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcomeKey2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcomeKey2.status == STARTED and not waitOnFlip:
        theseKeys = welcomeKey2.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
        _welcomeKey2_allKeys.extend(theseKeys)
        if len(_welcomeKey2_allKeys):
            welcomeKey2.keys = _welcomeKey2_allKeys[-1].name  # just the last key pressed
            welcomeKey2.rt = _welcomeKey2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreen2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "WelcomeScreen2" ---
for thisComponent in WelcomeScreen2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if welcomeKey2.keys in ['', [], None]:  # No response was made
    welcomeKey2.keys = None
thisExp.addData('welcomeKey2.keys',welcomeKey2.keys)
if welcomeKey2.keys != None:  # we had a response
    thisExp.addData('welcomeKey2.rt', welcomeKey2.rt)
thisExp.nextEntry()
# the Routine "WelcomeScreen2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EAPracticeInstructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
EAPracticeKey.keys = []
EAPracticeKey.rt = []
_EAPracticeKey_allKeys = []
# keep track of which components have finished
EAPracticeInstructionsComponents = [EAPracticeText1, EAPracticeText2, EAPracticeRespText, EAPracticeKey]
for thisComponent in EAPracticeInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EAPracticeInstructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EAPracticeText1* updates
    if EAPracticeText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EAPracticeText1.frameNStart = frameN  # exact frame index
        EAPracticeText1.tStart = t  # local t and not account for scr refresh
        EAPracticeText1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EAPracticeText1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EAPracticeText1.started')
        EAPracticeText1.setAutoDraw(True)
    
    # *EAPracticeText2* updates
    if EAPracticeText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EAPracticeText2.frameNStart = frameN  # exact frame index
        EAPracticeText2.tStart = t  # local t and not account for scr refresh
        EAPracticeText2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EAPracticeText2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EAPracticeText2.started')
        EAPracticeText2.setAutoDraw(True)
    
    # *EAPracticeRespText* updates
    if EAPracticeRespText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EAPracticeRespText.frameNStart = frameN  # exact frame index
        EAPracticeRespText.tStart = t  # local t and not account for scr refresh
        EAPracticeRespText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EAPracticeRespText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EAPracticeRespText.started')
        EAPracticeRespText.setAutoDraw(True)
    
    # *EAPracticeKey* updates
    waitOnFlip = False
    if EAPracticeKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EAPracticeKey.frameNStart = frameN  # exact frame index
        EAPracticeKey.tStart = t  # local t and not account for scr refresh
        EAPracticeKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EAPracticeKey, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EAPracticeKey.started')
        EAPracticeKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EAPracticeKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EAPracticeKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EAPracticeKey.status == STARTED and not waitOnFlip:
        theseKeys = EAPracticeKey.getKeys(keyList=['space'], waitRelease=False)
        _EAPracticeKey_allKeys.extend(theseKeys)
        if len(_EAPracticeKey_allKeys):
            EAPracticeKey.keys = _EAPracticeKey_allKeys[-1].name  # just the last key pressed
            EAPracticeKey.rt = _EAPracticeKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EAPracticeInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EAPracticeInstructions" ---
for thisComponent in EAPracticeInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if EAPracticeKey.keys in ['', [], None]:  # No response was made
    EAPracticeKey.keys = None
thisExp.addData('EAPracticeKey.keys',EAPracticeKey.keys)
if EAPracticeKey.keys != None:  # we had a response
    thisExp.addData('EAPracticeKey.rt', EAPracticeKey.rt)
thisExp.nextEntry()
# the Routine "EAPracticeInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EAPracticeInstructions2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
EAPractice2Key.keys = []
EAPractice2Key.rt = []
_EAPractice2Key_allKeys = []
# keep track of which components have finished
EAPracticeInstructions2Components = [EAPractice2Text, EAPractice2Key]
for thisComponent in EAPracticeInstructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EAPracticeInstructions2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EAPractice2Text* updates
    if EAPractice2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EAPractice2Text.frameNStart = frameN  # exact frame index
        EAPractice2Text.tStart = t  # local t and not account for scr refresh
        EAPractice2Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EAPractice2Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EAPractice2Text.started')
        EAPractice2Text.setAutoDraw(True)
    
    # *EAPractice2Key* updates
    waitOnFlip = False
    if EAPractice2Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EAPractice2Key.frameNStart = frameN  # exact frame index
        EAPractice2Key.tStart = t  # local t and not account for scr refresh
        EAPractice2Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EAPractice2Key, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EAPractice2Key.started')
        EAPractice2Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EAPractice2Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EAPractice2Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EAPractice2Key.status == STARTED and not waitOnFlip:
        theseKeys = EAPractice2Key.getKeys(keyList=['1'], waitRelease=False)
        _EAPractice2Key_allKeys.extend(theseKeys)
        if len(_EAPractice2Key_allKeys):
            EAPractice2Key.keys = _EAPractice2Key_allKeys[-1].name  # just the last key pressed
            EAPractice2Key.rt = _EAPractice2Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EAPracticeInstructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EAPracticeInstructions2" ---
for thisComponent in EAPracticeInstructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if EAPractice2Key.keys in ['', [], None]:  # No response was made
    EAPractice2Key.keys = None
thisExp.addData('EAPractice2Key.keys',EAPractice2Key.keys)
if EAPractice2Key.keys != None:  # we had a response
    thisExp.addData('EAPractice2Key.rt', EAPractice2Key.rt)
thisExp.nextEntry()
# the Routine "EAPracticeInstructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EAPractice1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from EAPractice1Code
EA_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/ExAttn_stim/'
EA_image_fp = os.path.join(EA_image_fp, ea_stim[shuffled_order[ea_stim_counter]])
EAPractice1_corrkey = str(ea_stim_corr_keys[shuffled_order[ea_stim_counter]])
thisExp.addData('corr_key', EAPractice1_corrkey)
thisExp.addData('stim_name', ea_stim[shuffled_order[ea_stim_counter]])
thisExp.addData('magnitude', ea_stim_magnitude[shuffled_order[ea_stim_counter]])
thisExp.addData('stim_spec', ea_stim_spec[shuffled_order[ea_stim_counter]])
thisExp.addData('num_big', ea_stim_big[shuffled_order[ea_stim_counter]])
ea_stim_counter += 1
EAPractice1Text1.setText('big _ small')
EAPractice1Text2.setText('?     >     =     <')
EAPractice1Stim.setImage(EA_image_fp)
EAPractice1Resp.keys = []
EAPractice1Resp.rt = []
_EAPractice1Resp_allKeys = []
# keep track of which components have finished
EAPractice1Components = [EAPractice1Text1, EAPractice1Text2, EAPractice1Stim, EAPractice1Resp]
for thisComponent in EAPractice1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EAPractice1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EAPractice1Text1* updates
    if EAPractice1Text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EAPractice1Text1.frameNStart = frameN  # exact frame index
        EAPractice1Text1.tStart = t  # local t and not account for scr refresh
        EAPractice1Text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EAPractice1Text1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EAPractice1Text1.started')
        EAPractice1Text1.setAutoDraw(True)
    
    # *EAPractice1Text2* updates
    if EAPractice1Text2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
        # keep track of start time/frame for later
        EAPractice1Text2.frameNStart = frameN  # exact frame index
        EAPractice1Text2.tStart = t  # local t and not account for scr refresh
        EAPractice1Text2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EAPractice1Text2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EAPractice1Text2.started')
        EAPractice1Text2.setAutoDraw(True)
    
    # *EAPractice1Stim* updates
    if EAPractice1Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EAPractice1Stim.frameNStart = frameN  # exact frame index
        EAPractice1Stim.tStart = t  # local t and not account for scr refresh
        EAPractice1Stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EAPractice1Stim, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EAPractice1Stim.started')
        EAPractice1Stim.setAutoDraw(True)
    
    # *EAPractice1Resp* updates
    waitOnFlip = False
    if EAPractice1Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EAPractice1Resp.frameNStart = frameN  # exact frame index
        EAPractice1Resp.tStart = t  # local t and not account for scr refresh
        EAPractice1Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EAPractice1Resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EAPractice1Resp.started')
        EAPractice1Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EAPractice1Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EAPractice1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EAPractice1Resp.status == STARTED and not waitOnFlip:
        theseKeys = EAPractice1Resp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
        _EAPractice1Resp_allKeys.extend(theseKeys)
        if len(_EAPractice1Resp_allKeys):
            EAPractice1Resp.keys = _EAPractice1Resp_allKeys[-1].name  # just the last key pressed
            EAPractice1Resp.rt = _EAPractice1Resp_allKeys[-1].rt
            # was this correct?
            if (EAPractice1Resp.keys == str(EAPractice1_corrkey)) or (EAPractice1Resp.keys == EAPractice1_corrkey):
                EAPractice1Resp.corr = 1
            else:
                EAPractice1Resp.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EAPractice1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EAPractice1" ---
for thisComponent in EAPractice1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from EAPractice1Code
if EAPractice1Resp.keys == EAPractice1_corrkey:
    EAPractice1_Feedback = 'Well done!\n\nWe will now practice with a time constraint. The shapes will again appear on screen for 1.5 seconds, after which you will be able to make a response. You have a limited time to make a response, so be sure to be quick! Each trial will be separated by a blank screen with a cross at the center.\n\nPress 1 to begin.'
else:
    EAPractice1_Feedback = 'Not quite, but you will have more practice now!\n\nThe next practice trials will have a time constraint. The shapes will again appear on screen for 1.5 seconds, after which you will be able to make a response. You have a limited time to make a response, so be sure to be quick! Each trial will be separated by a blank screen with a cross at the center.\n\nPress 1 to begin.'
# check responses
if EAPractice1Resp.keys in ['', [], None]:  # No response was made
    EAPractice1Resp.keys = None
    # was no response the correct answer?!
    if str(EAPractice1_corrkey).lower() == 'none':
       EAPractice1Resp.corr = 1;  # correct non-response
    else:
       EAPractice1Resp.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('EAPractice1Resp.keys',EAPractice1Resp.keys)
thisExp.addData('EAPractice1Resp.corr', EAPractice1Resp.corr)
if EAPractice1Resp.keys != None:  # we had a response
    thisExp.addData('EAPractice1Resp.rt', EAPractice1Resp.rt)
thisExp.nextEntry()
# the Routine "EAPractice1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EAPostPractice1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
EAPostPractice1Text.setText(EAPractice1_Feedback)
EAPostPractice1Resp.keys = []
EAPostPractice1Resp.rt = []
_EAPostPractice1Resp_allKeys = []
# keep track of which components have finished
EAPostPractice1Components = [EAPostPractice1Text, EAPostPractice1Resp]
for thisComponent in EAPostPractice1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EAPostPractice1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EAPostPractice1Text* updates
    if EAPostPractice1Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EAPostPractice1Text.frameNStart = frameN  # exact frame index
        EAPostPractice1Text.tStart = t  # local t and not account for scr refresh
        EAPostPractice1Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EAPostPractice1Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EAPostPractice1Text.started')
        EAPostPractice1Text.setAutoDraw(True)
    
    # *EAPostPractice1Resp* updates
    waitOnFlip = False
    if EAPostPractice1Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EAPostPractice1Resp.frameNStart = frameN  # exact frame index
        EAPostPractice1Resp.tStart = t  # local t and not account for scr refresh
        EAPostPractice1Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EAPostPractice1Resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EAPostPractice1Resp.started')
        EAPostPractice1Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EAPostPractice1Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EAPostPractice1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EAPostPractice1Resp.status == STARTED and not waitOnFlip:
        theseKeys = EAPostPractice1Resp.getKeys(keyList=['1'], waitRelease=False)
        _EAPostPractice1Resp_allKeys.extend(theseKeys)
        if len(_EAPostPractice1Resp_allKeys):
            EAPostPractice1Resp.keys = _EAPostPractice1Resp_allKeys[-1].name  # just the last key pressed
            EAPostPractice1Resp.rt = _EAPostPractice1Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EAPostPractice1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EAPostPractice1" ---
for thisComponent in EAPostPractice1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if EAPostPractice1Resp.keys in ['', [], None]:  # No response was made
    EAPostPractice1Resp.keys = None
thisExp.addData('EAPostPractice1Resp.keys',EAPostPractice1Resp.keys)
if EAPostPractice1Resp.keys != None:  # we had a response
    thisExp.addData('EAPostPractice1Resp.rt', EAPostPractice1Resp.rt)
thisExp.nextEntry()
# the Routine "EAPostPractice1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
EAPractice2Trials = data.TrialHandler(nReps=4.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='EAPractice2Trials')
thisExp.addLoop(EAPractice2Trials)  # add the loop to the experiment
thisEAPractice2Trial = EAPractice2Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEAPractice2Trial.rgb)
if thisEAPractice2Trial != None:
    for paramName in thisEAPractice2Trial:
        exec('{} = thisEAPractice2Trial[paramName]'.format(paramName))

for thisEAPractice2Trial in EAPractice2Trials:
    currentLoop = EAPractice2Trials
    # abbreviate parameter names if possible (e.g. rgb = thisEAPractice2Trial.rgb)
    if thisEAPractice2Trial != None:
        for paramName in thisEAPractice2Trial:
            exec('{} = thisEAPractice2Trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ISI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [FixCross]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixCross* updates
        if FixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixCross.frameNStart = frameN  # exact frame index
            FixCross.tStart = t  # local t and not account for scr refresh
            FixCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixCross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FixCross.started')
            FixCross.setAutoDraw(True)
        if FixCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixCross.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                FixCross.tStop = t  # not accounting for scr refresh
                FixCross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FixCross.stopped')
                FixCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI" ---
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "EATrial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from EATrialCode
    EA_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/ExAttn_stim/'
    EA_image_fp = os.path.join(EA_image_fp, ea_stim[shuffled_order[ea_stim_counter]])
    EA_corrkey = str(ea_stim_corr_keys[shuffled_order[ea_stim_counter]])
    thisExp.addData('corr_key', EA_corrkey)
    thisExp.addData('stim_name', ea_stim[shuffled_order[ea_stim_counter]])
    thisExp.addData('magnitude', ea_stim_magnitude[shuffled_order[ea_stim_counter]])
    thisExp.addData('stim_spec', ea_stim_spec[shuffled_order[ea_stim_counter]])
    thisExp.addData('num_big', ea_stim_big[shuffled_order[ea_stim_counter]])
    ea_stim_counter += 1
    EATrialText1.setText('big _ small')
    EATrialText2.setText('?     >     =     <')
    EATrialStim.setImage(EA_image_fp)
    EATrialResp.keys = []
    EATrialResp.rt = []
    _EATrialResp_allKeys = []
    # keep track of which components have finished
    EATrialComponents = [EATrialText1, EATrialText2, EATrialStim, EATrialResp]
    for thisComponent in EATrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EATrial" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *EATrialText1* updates
        if EATrialText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EATrialText1.frameNStart = frameN  # exact frame index
            EATrialText1.tStart = t  # local t and not account for scr refresh
            EATrialText1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EATrialText1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EATrialText1.started')
            EATrialText1.setAutoDraw(True)
        if EATrialText1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EATrialText1.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                EATrialText1.tStop = t  # not accounting for scr refresh
                EATrialText1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATrialText1.stopped')
                EATrialText1.setAutoDraw(False)
        
        # *EATrialText2* updates
        if EATrialText2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            EATrialText2.frameNStart = frameN  # exact frame index
            EATrialText2.tStart = t  # local t and not account for scr refresh
            EATrialText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EATrialText2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EATrialText2.started')
            EATrialText2.setAutoDraw(True)
        if EATrialText2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EATrialText2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                EATrialText2.tStop = t  # not accounting for scr refresh
                EATrialText2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATrialText2.stopped')
                EATrialText2.setAutoDraw(False)
        
        # *EATrialStim* updates
        if EATrialStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EATrialStim.frameNStart = frameN  # exact frame index
            EATrialStim.tStart = t  # local t and not account for scr refresh
            EATrialStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EATrialStim, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EATrialStim.started')
            EATrialStim.setAutoDraw(True)
        if EATrialStim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EATrialStim.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                EATrialStim.tStop = t  # not accounting for scr refresh
                EATrialStim.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATrialStim.stopped')
                EATrialStim.setAutoDraw(False)
        
        # *EATrialResp* updates
        waitOnFlip = False
        if EATrialResp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            EATrialResp.frameNStart = frameN  # exact frame index
            EATrialResp.tStart = t  # local t and not account for scr refresh
            EATrialResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EATrialResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EATrialResp.started')
            EATrialResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(EATrialResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(EATrialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if EATrialResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EATrialResp.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                EATrialResp.tStop = t  # not accounting for scr refresh
                EATrialResp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATrialResp.stopped')
                EATrialResp.status = FINISHED
        if EATrialResp.status == STARTED and not waitOnFlip:
            theseKeys = EATrialResp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
            _EATrialResp_allKeys.extend(theseKeys)
            if len(_EATrialResp_allKeys):
                EATrialResp.keys = _EATrialResp_allKeys[-1].name  # just the last key pressed
                EATrialResp.rt = _EATrialResp_allKeys[-1].rt
                # was this correct?
                if (EATrialResp.keys == str(EA_corrkey)) or (EATrialResp.keys == EA_corrkey):
                    EATrialResp.corr = 1
                else:
                    EATrialResp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EATrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EATrial" ---
    for thisComponent in EATrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if EATrialResp.keys in ['', [], None]:  # No response was made
        EATrialResp.keys = None
        # was no response the correct answer?!
        if str(EA_corrkey).lower() == 'none':
           EATrialResp.corr = 1;  # correct non-response
        else:
           EATrialResp.corr = 0;  # failed to respond (incorrectly)
    # store data for EAPractice2Trials (TrialHandler)
    EAPractice2Trials.addData('EATrialResp.keys',EATrialResp.keys)
    EAPractice2Trials.addData('EATrialResp.corr', EATrialResp.corr)
    if EATrialResp.keys != None:  # we had a response
        EAPractice2Trials.addData('EATrialResp.rt', EATrialResp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'EAPractice2Trials'


# --- Prepare to start Routine "EAPracticeEnd" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
EAPracticeEndKey.keys = []
EAPracticeEndKey.rt = []
_EAPracticeEndKey_allKeys = []
# keep track of which components have finished
EAPracticeEndComponents = [EAPracticeEndText, EAPracticeEndKey]
for thisComponent in EAPracticeEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EAPracticeEnd" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EAPracticeEndText* updates
    if EAPracticeEndText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EAPracticeEndText.frameNStart = frameN  # exact frame index
        EAPracticeEndText.tStart = t  # local t and not account for scr refresh
        EAPracticeEndText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EAPracticeEndText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EAPracticeEndText.started')
        EAPracticeEndText.setAutoDraw(True)
    
    # *EAPracticeEndKey* updates
    waitOnFlip = False
    if EAPracticeEndKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EAPracticeEndKey.frameNStart = frameN  # exact frame index
        EAPracticeEndKey.tStart = t  # local t and not account for scr refresh
        EAPracticeEndKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EAPracticeEndKey, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EAPracticeEndKey.started')
        EAPracticeEndKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EAPracticeEndKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EAPracticeEndKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EAPracticeEndKey.status == STARTED and not waitOnFlip:
        theseKeys = EAPracticeEndKey.getKeys(keyList=['1'], waitRelease=False)
        _EAPracticeEndKey_allKeys.extend(theseKeys)
        if len(_EAPracticeEndKey_allKeys):
            EAPracticeEndKey.keys = _EAPracticeEndKey_allKeys[-1].name  # just the last key pressed
            EAPracticeEndKey.rt = _EAPracticeEndKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EAPracticeEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EAPracticeEnd" ---
for thisComponent in EAPracticeEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if EAPracticeEndKey.keys in ['', [], None]:  # No response was made
    EAPracticeEndKey.keys = None
thisExp.addData('EAPracticeEndKey.keys',EAPracticeEndKey.keys)
if EAPracticeEndKey.keys != None:  # we had a response
    thisExp.addData('EAPracticeEndKey.rt', EAPracticeEndKey.rt)
thisExp.nextEntry()
# the Routine "EAPracticeEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "IAPracticeInstructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
IAPracticeInstructions1Resp.keys = []
IAPracticeInstructions1Resp.rt = []
_IAPracticeInstructions1Resp_allKeys = []
# keep track of which components have finished
IAPracticeInstructionsComponents = [IAPracticeInstructions1Text1, IAPracticeInstructions1Text2, IAPracticeInstructions1RespText, IAPracticeInstructions1Resp]
for thisComponent in IAPracticeInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "IAPracticeInstructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IAPracticeInstructions1Text1* updates
    if IAPracticeInstructions1Text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IAPracticeInstructions1Text1.frameNStart = frameN  # exact frame index
        IAPracticeInstructions1Text1.tStart = t  # local t and not account for scr refresh
        IAPracticeInstructions1Text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IAPracticeInstructions1Text1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IAPracticeInstructions1Text1.started')
        IAPracticeInstructions1Text1.setAutoDraw(True)
    
    # *IAPracticeInstructions1Text2* updates
    if IAPracticeInstructions1Text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IAPracticeInstructions1Text2.frameNStart = frameN  # exact frame index
        IAPracticeInstructions1Text2.tStart = t  # local t and not account for scr refresh
        IAPracticeInstructions1Text2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IAPracticeInstructions1Text2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IAPracticeInstructions1Text2.started')
        IAPracticeInstructions1Text2.setAutoDraw(True)
    
    # *IAPracticeInstructions1RespText* updates
    if IAPracticeInstructions1RespText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IAPracticeInstructions1RespText.frameNStart = frameN  # exact frame index
        IAPracticeInstructions1RespText.tStart = t  # local t and not account for scr refresh
        IAPracticeInstructions1RespText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IAPracticeInstructions1RespText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IAPracticeInstructions1RespText.started')
        IAPracticeInstructions1RespText.setAutoDraw(True)
    
    # *IAPracticeInstructions1Resp* updates
    waitOnFlip = False
    if IAPracticeInstructions1Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IAPracticeInstructions1Resp.frameNStart = frameN  # exact frame index
        IAPracticeInstructions1Resp.tStart = t  # local t and not account for scr refresh
        IAPracticeInstructions1Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IAPracticeInstructions1Resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IAPracticeInstructions1Resp.started')
        IAPracticeInstructions1Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(IAPracticeInstructions1Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(IAPracticeInstructions1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if IAPracticeInstructions1Resp.status == STARTED and not waitOnFlip:
        theseKeys = IAPracticeInstructions1Resp.getKeys(keyList=['space'], waitRelease=False)
        _IAPracticeInstructions1Resp_allKeys.extend(theseKeys)
        if len(_IAPracticeInstructions1Resp_allKeys):
            IAPracticeInstructions1Resp.keys = _IAPracticeInstructions1Resp_allKeys[-1].name  # just the last key pressed
            IAPracticeInstructions1Resp.rt = _IAPracticeInstructions1Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IAPracticeInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "IAPracticeInstructions" ---
for thisComponent in IAPracticeInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if IAPracticeInstructions1Resp.keys in ['', [], None]:  # No response was made
    IAPracticeInstructions1Resp.keys = None
thisExp.addData('IAPracticeInstructions1Resp.keys',IAPracticeInstructions1Resp.keys)
if IAPracticeInstructions1Resp.keys != None:  # we had a response
    thisExp.addData('IAPracticeInstructions1Resp.rt', IAPracticeInstructions1Resp.rt)
thisExp.nextEntry()
# the Routine "IAPracticeInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "IAPracticeInstructions2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
IAPracticeInstructions2Resp.keys = []
IAPracticeInstructions2Resp.rt = []
_IAPracticeInstructions2Resp_allKeys = []
# keep track of which components have finished
IAPracticeInstructions2Components = [IAPracticeInstructions2Text, IAPracticeInstructions2Resp]
for thisComponent in IAPracticeInstructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "IAPracticeInstructions2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IAPracticeInstructions2Text* updates
    if IAPracticeInstructions2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IAPracticeInstructions2Text.frameNStart = frameN  # exact frame index
        IAPracticeInstructions2Text.tStart = t  # local t and not account for scr refresh
        IAPracticeInstructions2Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IAPracticeInstructions2Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IAPracticeInstructions2Text.started')
        IAPracticeInstructions2Text.setAutoDraw(True)
    
    # *IAPracticeInstructions2Resp* updates
    waitOnFlip = False
    if IAPracticeInstructions2Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IAPracticeInstructions2Resp.frameNStart = frameN  # exact frame index
        IAPracticeInstructions2Resp.tStart = t  # local t and not account for scr refresh
        IAPracticeInstructions2Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IAPracticeInstructions2Resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IAPracticeInstructions2Resp.started')
        IAPracticeInstructions2Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(IAPracticeInstructions2Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(IAPracticeInstructions2Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if IAPracticeInstructions2Resp.status == STARTED and not waitOnFlip:
        theseKeys = IAPracticeInstructions2Resp.getKeys(keyList=['1'], waitRelease=False)
        _IAPracticeInstructions2Resp_allKeys.extend(theseKeys)
        if len(_IAPracticeInstructions2Resp_allKeys):
            IAPracticeInstructions2Resp.keys = _IAPracticeInstructions2Resp_allKeys[-1].name  # just the last key pressed
            IAPracticeInstructions2Resp.rt = _IAPracticeInstructions2Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IAPracticeInstructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "IAPracticeInstructions2" ---
for thisComponent in IAPracticeInstructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if IAPracticeInstructions2Resp.keys in ['', [], None]:  # No response was made
    IAPracticeInstructions2Resp.keys = None
thisExp.addData('IAPracticeInstructions2Resp.keys',IAPracticeInstructions2Resp.keys)
if IAPracticeInstructions2Resp.keys != None:  # we had a response
    thisExp.addData('IAPracticeInstructions2Resp.rt', IAPracticeInstructions2Resp.rt)
thisExp.nextEntry()
# the Routine "IAPracticeInstructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "IAPractice1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from IAPractice1Code
IA_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/IntAttn_stim/'
IA_image_fp = os.path.join(IA_image_fp, ia_stim[shuffled_order[ia_stim_counter]])
IAPractice1_corrkey = str(ia_stim_corr_keys[shuffled_order[ia_stim_counter]])
thisExp.addData('corr_key', IAPractice1_corrkey)
thisExp.addData('stim_name', ia_stim[shuffled_order[ia_stim_counter]])
thisExp.addData('magnitude', ia_stim_magnitude[shuffled_order[ia_stim_counter]])
thisExp.addData('stim_spec', ia_stim_spec[shuffled_order[ia_stim_counter]])
thisExp.addData('has_neg', ia_stim_hasneg[shuffled_order[ia_stim_counter]])
ia_stim_counter += 1
IAPractice1Text1.setText('?     >     =     <')
IAPractice1Stim.setImage(IA_image_fp)
IAPractice1Resp.keys = []
IAPractice1Resp.rt = []
_IAPractice1Resp_allKeys = []
# keep track of which components have finished
IAPractice1Components = [IAPractice1Text1, IAPractice1Stim, IAPractice1Resp]
for thisComponent in IAPractice1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "IAPractice1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IAPractice1Text1* updates
    if IAPractice1Text1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
        # keep track of start time/frame for later
        IAPractice1Text1.frameNStart = frameN  # exact frame index
        IAPractice1Text1.tStart = t  # local t and not account for scr refresh
        IAPractice1Text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IAPractice1Text1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IAPractice1Text1.started')
        IAPractice1Text1.setAutoDraw(True)
    
    # *IAPractice1Stim* updates
    if IAPractice1Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IAPractice1Stim.frameNStart = frameN  # exact frame index
        IAPractice1Stim.tStart = t  # local t and not account for scr refresh
        IAPractice1Stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IAPractice1Stim, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IAPractice1Stim.started')
        IAPractice1Stim.setAutoDraw(True)
    
    # *IAPractice1Resp* updates
    waitOnFlip = False
    if IAPractice1Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IAPractice1Resp.frameNStart = frameN  # exact frame index
        IAPractice1Resp.tStart = t  # local t and not account for scr refresh
        IAPractice1Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IAPractice1Resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IAPractice1Resp.started')
        IAPractice1Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(IAPractice1Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(IAPractice1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if IAPractice1Resp.status == STARTED and not waitOnFlip:
        theseKeys = IAPractice1Resp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
        _IAPractice1Resp_allKeys.extend(theseKeys)
        if len(_IAPractice1Resp_allKeys):
            IAPractice1Resp.keys = _IAPractice1Resp_allKeys[-1].name  # just the last key pressed
            IAPractice1Resp.rt = _IAPractice1Resp_allKeys[-1].rt
            # was this correct?
            if (IAPractice1Resp.keys == str(IAPractice1_corrkey)) or (IAPractice1Resp.keys == IAPractice1_corrkey):
                IAPractice1Resp.corr = 1
            else:
                IAPractice1Resp.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IAPractice1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "IAPractice1" ---
for thisComponent in IAPractice1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from IAPractice1Code
if IAPractice1Resp.keys == IAPractice1_corrkey:
    IAPractice1_Feedback = 'Well done!\n\nWe will now practice with a time constraint. The equations will again appear on screen for 1.5 seconds, after which you will be able to make a response. You have a limited time to make a response, so be sure to be quick! Each trial will be separated by a blank screen with a cross at the center.\n\nPress 1 to begin.'
else:
    EAPractice1_Feedback = 'Not quite, but you will have more practice now!\n\nThe next practice trials will have a time constraint. The equations will again appear on screen for 1.5 seconds, after which you will be able to make a response. You have a limited time to make a response, so be sure to be quick! Each trial will be separated by a blank screen with a cross at the center.\n\nPress 1 to begin.'
# check responses
if IAPractice1Resp.keys in ['', [], None]:  # No response was made
    IAPractice1Resp.keys = None
    # was no response the correct answer?!
    if str(IAPractice1_corrkey).lower() == 'none':
       IAPractice1Resp.corr = 1;  # correct non-response
    else:
       IAPractice1Resp.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('IAPractice1Resp.keys',IAPractice1Resp.keys)
thisExp.addData('IAPractice1Resp.corr', IAPractice1Resp.corr)
if IAPractice1Resp.keys != None:  # we had a response
    thisExp.addData('IAPractice1Resp.rt', IAPractice1Resp.rt)
thisExp.nextEntry()
# the Routine "IAPractice1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "IAPostPractice1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
IAPractice1Feedback.setText(IAPractice1_Feedback)
IAPostPractice1Resp.keys = []
IAPostPractice1Resp.rt = []
_IAPostPractice1Resp_allKeys = []
# keep track of which components have finished
IAPostPractice1Components = [IAPractice1Feedback, IAPostPractice1Resp]
for thisComponent in IAPostPractice1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "IAPostPractice1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IAPractice1Feedback* updates
    if IAPractice1Feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IAPractice1Feedback.frameNStart = frameN  # exact frame index
        IAPractice1Feedback.tStart = t  # local t and not account for scr refresh
        IAPractice1Feedback.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IAPractice1Feedback, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IAPractice1Feedback.started')
        IAPractice1Feedback.setAutoDraw(True)
    
    # *IAPostPractice1Resp* updates
    waitOnFlip = False
    if IAPostPractice1Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IAPostPractice1Resp.frameNStart = frameN  # exact frame index
        IAPostPractice1Resp.tStart = t  # local t and not account for scr refresh
        IAPostPractice1Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IAPostPractice1Resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IAPostPractice1Resp.started')
        IAPostPractice1Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(IAPostPractice1Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(IAPostPractice1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if IAPostPractice1Resp.status == STARTED and not waitOnFlip:
        theseKeys = IAPostPractice1Resp.getKeys(keyList=['1'], waitRelease=False)
        _IAPostPractice1Resp_allKeys.extend(theseKeys)
        if len(_IAPostPractice1Resp_allKeys):
            IAPostPractice1Resp.keys = _IAPostPractice1Resp_allKeys[-1].name  # just the last key pressed
            IAPostPractice1Resp.rt = _IAPostPractice1Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IAPostPractice1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "IAPostPractice1" ---
for thisComponent in IAPostPractice1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if IAPostPractice1Resp.keys in ['', [], None]:  # No response was made
    IAPostPractice1Resp.keys = None
thisExp.addData('IAPostPractice1Resp.keys',IAPostPractice1Resp.keys)
if IAPostPractice1Resp.keys != None:  # we had a response
    thisExp.addData('IAPostPractice1Resp.rt', IAPostPractice1Resp.rt)
thisExp.nextEntry()
# the Routine "IAPostPractice1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
IAPractice2Trials = data.TrialHandler(nReps=4.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='IAPractice2Trials')
thisExp.addLoop(IAPractice2Trials)  # add the loop to the experiment
thisIAPractice2Trial = IAPractice2Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIAPractice2Trial.rgb)
if thisIAPractice2Trial != None:
    for paramName in thisIAPractice2Trial:
        exec('{} = thisIAPractice2Trial[paramName]'.format(paramName))

for thisIAPractice2Trial in IAPractice2Trials:
    currentLoop = IAPractice2Trials
    # abbreviate parameter names if possible (e.g. rgb = thisIAPractice2Trial.rgb)
    if thisIAPractice2Trial != None:
        for paramName in thisIAPractice2Trial:
            exec('{} = thisIAPractice2Trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ISI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [FixCross]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixCross* updates
        if FixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixCross.frameNStart = frameN  # exact frame index
            FixCross.tStart = t  # local t and not account for scr refresh
            FixCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixCross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FixCross.started')
            FixCross.setAutoDraw(True)
        if FixCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixCross.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                FixCross.tStop = t  # not accounting for scr refresh
                FixCross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FixCross.stopped')
                FixCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI" ---
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "IATrial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from IATrialCode
    IA_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/IntAttn_stim/'
    IA_image_fp = os.path.join(IA_image_fp, ia_stim[shuffled_order[ia_stim_counter]])
    IA_corrkey = str(ia_stim_corr_keys[shuffled_order[ia_stim_counter]])
    thisExp.addData('corr_key', IA_corrkey)
    thisExp.addData('stim_name', ia_stim[shuffled_order[ia_stim_counter]])
    thisExp.addData('magnitude', ia_stim_magnitude[shuffled_order[ia_stim_counter]])
    thisExp.addData('stim_spec', ia_stim_spec[shuffled_order[ia_stim_counter]])
    thisExp.addData('has_neg', ia_stim_hasneg[shuffled_order[ia_stim_counter]])
    ia_stim_counter += 1
    IATrialRespText.setText('?     >     =     <')
    IATrialStim.setImage(IA_image_fp)
    IATrialResp.keys = []
    IATrialResp.rt = []
    _IATrialResp_allKeys = []
    # keep track of which components have finished
    IATrialComponents = [IATrialRespText, IATrialStim, IATrialResp]
    for thisComponent in IATrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "IATrial" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IATrialRespText* updates
        if IATrialRespText.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            IATrialRespText.frameNStart = frameN  # exact frame index
            IATrialRespText.tStart = t  # local t and not account for scr refresh
            IATrialRespText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IATrialRespText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IATrialRespText.started')
            IATrialRespText.setAutoDraw(True)
        if IATrialRespText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > IATrialRespText.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                IATrialRespText.tStop = t  # not accounting for scr refresh
                IATrialRespText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IATrialRespText.stopped')
                IATrialRespText.setAutoDraw(False)
        
        # *IATrialStim* updates
        if IATrialStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IATrialStim.frameNStart = frameN  # exact frame index
            IATrialStim.tStart = t  # local t and not account for scr refresh
            IATrialStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IATrialStim, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IATrialStim.started')
            IATrialStim.setAutoDraw(True)
        if IATrialStim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > IATrialStim.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                IATrialStim.tStop = t  # not accounting for scr refresh
                IATrialStim.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IATrialStim.stopped')
                IATrialStim.setAutoDraw(False)
        
        # *IATrialResp* updates
        waitOnFlip = False
        if IATrialResp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            IATrialResp.frameNStart = frameN  # exact frame index
            IATrialResp.tStart = t  # local t and not account for scr refresh
            IATrialResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IATrialResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IATrialResp.started')
            IATrialResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(IATrialResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(IATrialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if IATrialResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > IATrialResp.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                IATrialResp.tStop = t  # not accounting for scr refresh
                IATrialResp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IATrialResp.stopped')
                IATrialResp.status = FINISHED
        if IATrialResp.status == STARTED and not waitOnFlip:
            theseKeys = IATrialResp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
            _IATrialResp_allKeys.extend(theseKeys)
            if len(_IATrialResp_allKeys):
                IATrialResp.keys = _IATrialResp_allKeys[-1].name  # just the last key pressed
                IATrialResp.rt = _IATrialResp_allKeys[-1].rt
                # was this correct?
                if (IATrialResp.keys == str(IA_corrkey)) or (IATrialResp.keys == IA_corrkey):
                    IATrialResp.corr = 1
                else:
                    IATrialResp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IATrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "IATrial" ---
    for thisComponent in IATrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if IATrialResp.keys in ['', [], None]:  # No response was made
        IATrialResp.keys = None
        # was no response the correct answer?!
        if str(IA_corrkey).lower() == 'none':
           IATrialResp.corr = 1;  # correct non-response
        else:
           IATrialResp.corr = 0;  # failed to respond (incorrectly)
    # store data for IAPractice2Trials (TrialHandler)
    IAPractice2Trials.addData('IATrialResp.keys',IATrialResp.keys)
    IAPractice2Trials.addData('IATrialResp.corr', IATrialResp.corr)
    if IATrialResp.keys != None:  # we had a response
        IAPractice2Trials.addData('IATrialResp.rt', IATrialResp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'IAPractice2Trials'


# --- Prepare to start Routine "IAPracticeEnd" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
IAPracticeEndResp.keys = []
IAPracticeEndResp.rt = []
_IAPracticeEndResp_allKeys = []
# keep track of which components have finished
IAPracticeEndComponents = [IAPracticeEndText, IAPracticeEndResp]
for thisComponent in IAPracticeEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "IAPracticeEnd" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IAPracticeEndText* updates
    if IAPracticeEndText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IAPracticeEndText.frameNStart = frameN  # exact frame index
        IAPracticeEndText.tStart = t  # local t and not account for scr refresh
        IAPracticeEndText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IAPracticeEndText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IAPracticeEndText.started')
        IAPracticeEndText.setAutoDraw(True)
    
    # *IAPracticeEndResp* updates
    waitOnFlip = False
    if IAPracticeEndResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IAPracticeEndResp.frameNStart = frameN  # exact frame index
        IAPracticeEndResp.tStart = t  # local t and not account for scr refresh
        IAPracticeEndResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IAPracticeEndResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IAPracticeEndResp.started')
        IAPracticeEndResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(IAPracticeEndResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(IAPracticeEndResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if IAPracticeEndResp.status == STARTED and not waitOnFlip:
        theseKeys = IAPracticeEndResp.getKeys(keyList=['1'], waitRelease=False)
        _IAPracticeEndResp_allKeys.extend(theseKeys)
        if len(_IAPracticeEndResp_allKeys):
            IAPracticeEndResp.keys = _IAPracticeEndResp_allKeys[-1].name  # just the last key pressed
            IAPracticeEndResp.rt = _IAPracticeEndResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IAPracticeEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "IAPracticeEnd" ---
for thisComponent in IAPracticeEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if IAPracticeEndResp.keys in ['', [], None]:  # No response was made
    IAPracticeEndResp.keys = None
thisExp.addData('IAPracticeEndResp.keys',IAPracticeEndResp.keys)
if IAPracticeEndResp.keys != None:  # we had a response
    thisExp.addData('IAPracticeEndResp.rt', IAPracticeEndResp.rt)
thisExp.nextEntry()
# the Routine "IAPracticeEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EncPracticeInstructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
EncPracticeInstructionsResp.keys = []
EncPracticeInstructionsResp.rt = []
_EncPracticeInstructionsResp_allKeys = []
# keep track of which components have finished
EncPracticeInstructionsComponents = [EncPracticeInstructionsText1, EncPracticeInstructionsText2, EncPracticeInstructionsRespText, EncPracticeInstructionsResp]
for thisComponent in EncPracticeInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EncPracticeInstructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EncPracticeInstructionsText1* updates
    if EncPracticeInstructionsText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EncPracticeInstructionsText1.frameNStart = frameN  # exact frame index
        EncPracticeInstructionsText1.tStart = t  # local t and not account for scr refresh
        EncPracticeInstructionsText1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EncPracticeInstructionsText1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EncPracticeInstructionsText1.started')
        EncPracticeInstructionsText1.setAutoDraw(True)
    
    # *EncPracticeInstructionsText2* updates
    if EncPracticeInstructionsText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EncPracticeInstructionsText2.frameNStart = frameN  # exact frame index
        EncPracticeInstructionsText2.tStart = t  # local t and not account for scr refresh
        EncPracticeInstructionsText2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EncPracticeInstructionsText2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EncPracticeInstructionsText2.started')
        EncPracticeInstructionsText2.setAutoDraw(True)
    
    # *EncPracticeInstructionsRespText* updates
    if EncPracticeInstructionsRespText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EncPracticeInstructionsRespText.frameNStart = frameN  # exact frame index
        EncPracticeInstructionsRespText.tStart = t  # local t and not account for scr refresh
        EncPracticeInstructionsRespText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EncPracticeInstructionsRespText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EncPracticeInstructionsRespText.started')
        EncPracticeInstructionsRespText.setAutoDraw(True)
    
    # *EncPracticeInstructionsResp* updates
    waitOnFlip = False
    if EncPracticeInstructionsResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EncPracticeInstructionsResp.frameNStart = frameN  # exact frame index
        EncPracticeInstructionsResp.tStart = t  # local t and not account for scr refresh
        EncPracticeInstructionsResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EncPracticeInstructionsResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EncPracticeInstructionsResp.started')
        EncPracticeInstructionsResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EncPracticeInstructionsResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EncPracticeInstructionsResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EncPracticeInstructionsResp.status == STARTED and not waitOnFlip:
        theseKeys = EncPracticeInstructionsResp.getKeys(keyList=['space'], waitRelease=False)
        _EncPracticeInstructionsResp_allKeys.extend(theseKeys)
        if len(_EncPracticeInstructionsResp_allKeys):
            EncPracticeInstructionsResp.keys = _EncPracticeInstructionsResp_allKeys[-1].name  # just the last key pressed
            EncPracticeInstructionsResp.rt = _EncPracticeInstructionsResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EncPracticeInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EncPracticeInstructions" ---
for thisComponent in EncPracticeInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if EncPracticeInstructionsResp.keys in ['', [], None]:  # No response was made
    EncPracticeInstructionsResp.keys = None
thisExp.addData('EncPracticeInstructionsResp.keys',EncPracticeInstructionsResp.keys)
if EncPracticeInstructionsResp.keys != None:  # we had a response
    thisExp.addData('EncPracticeInstructionsResp.rt', EncPracticeInstructionsResp.rt)
thisExp.nextEntry()
# the Routine "EncPracticeInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EncPracticeInstructions2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
EncPracticeInstructions2Resp.keys = []
EncPracticeInstructions2Resp.rt = []
_EncPracticeInstructions2Resp_allKeys = []
# keep track of which components have finished
EncPracticeInstructions2Components = [EncPracticeInstructions2Text, EncPracticeInstructions2Resp]
for thisComponent in EncPracticeInstructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EncPracticeInstructions2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EncPracticeInstructions2Text* updates
    if EncPracticeInstructions2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EncPracticeInstructions2Text.frameNStart = frameN  # exact frame index
        EncPracticeInstructions2Text.tStart = t  # local t and not account for scr refresh
        EncPracticeInstructions2Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EncPracticeInstructions2Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EncPracticeInstructions2Text.started')
        EncPracticeInstructions2Text.setAutoDraw(True)
    
    # *EncPracticeInstructions2Resp* updates
    waitOnFlip = False
    if EncPracticeInstructions2Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EncPracticeInstructions2Resp.frameNStart = frameN  # exact frame index
        EncPracticeInstructions2Resp.tStart = t  # local t and not account for scr refresh
        EncPracticeInstructions2Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EncPracticeInstructions2Resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EncPracticeInstructions2Resp.started')
        EncPracticeInstructions2Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EncPracticeInstructions2Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EncPracticeInstructions2Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EncPracticeInstructions2Resp.status == STARTED and not waitOnFlip:
        theseKeys = EncPracticeInstructions2Resp.getKeys(keyList=['1'], waitRelease=False)
        _EncPracticeInstructions2Resp_allKeys.extend(theseKeys)
        if len(_EncPracticeInstructions2Resp_allKeys):
            EncPracticeInstructions2Resp.keys = _EncPracticeInstructions2Resp_allKeys[-1].name  # just the last key pressed
            EncPracticeInstructions2Resp.rt = _EncPracticeInstructions2Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EncPracticeInstructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EncPracticeInstructions2" ---
for thisComponent in EncPracticeInstructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if EncPracticeInstructions2Resp.keys in ['', [], None]:  # No response was made
    EncPracticeInstructions2Resp.keys = None
thisExp.addData('EncPracticeInstructions2Resp.keys',EncPracticeInstructions2Resp.keys)
if EncPracticeInstructions2Resp.keys != None:  # we had a response
    thisExp.addData('EncPracticeInstructions2Resp.rt', EncPracticeInstructions2Resp.rt)
thisExp.nextEntry()
# the Routine "EncPracticeInstructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EncPractice1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from EncPractice1Code
Enc_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Enc_stim/'
Enc_image_fp = os.path.join(Enc_image_fp, enc_stim[shuffled_order[enc_stim_counter]])
EncPractice1_corrkey = str(enc_stim_corr_keys[shuffled_order[enc_stim_counter]])
thisExp.addData('corr_key', EncPractice1_corrkey)
thisExp.addData('stim_name', enc_stim[shuffled_order[enc_stim_counter]])
thisExp.addData('stim_spec', enc_stim_spec[shuffled_order[enc_stim_counter]])
enc_stim_counter += 1
EncPractice1Resp.keys = []
EncPractice1Resp.rt = []
_EncPractice1Resp_allKeys = []
EncPractice1Stim.setImage(Enc_image_fp)
EncPractice1RespText.setText('?     >     =     <')
# keep track of which components have finished
EncPractice1Components = [EncPractice1Resp, EncPractice1Stim, EncPractice1RespText]
for thisComponent in EncPractice1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EncPractice1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EncPractice1Resp* updates
    waitOnFlip = False
    if EncPractice1Resp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
        # keep track of start time/frame for later
        EncPractice1Resp.frameNStart = frameN  # exact frame index
        EncPractice1Resp.tStart = t  # local t and not account for scr refresh
        EncPractice1Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EncPractice1Resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EncPractice1Resp.started')
        EncPractice1Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EncPractice1Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EncPractice1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EncPractice1Resp.status == STARTED and not waitOnFlip:
        theseKeys = EncPractice1Resp.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
        _EncPractice1Resp_allKeys.extend(theseKeys)
        if len(_EncPractice1Resp_allKeys):
            EncPractice1Resp.keys = _EncPractice1Resp_allKeys[-1].name  # just the last key pressed
            EncPractice1Resp.rt = _EncPractice1Resp_allKeys[-1].rt
            # was this correct?
            if (EncPractice1Resp.keys == str(EncPractice1_corrkey)) or (EncPractice1Resp.keys == EncPractice1_corrkey):
                EncPractice1Resp.corr = 1
            else:
                EncPractice1Resp.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # *EncPractice1Stim* updates
    if EncPractice1Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EncPractice1Stim.frameNStart = frameN  # exact frame index
        EncPractice1Stim.tStart = t  # local t and not account for scr refresh
        EncPractice1Stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EncPractice1Stim, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EncPractice1Stim.started')
        EncPractice1Stim.setAutoDraw(True)
    
    # *EncPractice1RespText* updates
    if EncPractice1RespText.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
        # keep track of start time/frame for later
        EncPractice1RespText.frameNStart = frameN  # exact frame index
        EncPractice1RespText.tStart = t  # local t and not account for scr refresh
        EncPractice1RespText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EncPractice1RespText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EncPractice1RespText.started')
        EncPractice1RespText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EncPractice1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EncPractice1" ---
for thisComponent in EncPractice1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from EncPractice1Code
if EncPractice1Resp.keys == EncPractice1_corrkey:
    EncPractice1_Feedback = 'Well done!\n\nWe will now practice with a time constraint. The images will again appear on screen for 1.5 seconds, after which you will be able to make a response. You have a limited time to make a response, so be sure to be quick! Unlike the other tasks, there will be a short delay between when you make a button press and when the trial ends. Please try to only press one key during the response time. Remember, make your judgment based on the size of the items on the screen, not the size of the items in the real world. Each trial will be separated by a blank screen with a cross at the center.\n\nPress 1 to begin.'
else:
    EncPractice1_Feedback = 'Not quite, but you will have more practice now!\n\nThe next practice trials will have a time constraint. The equations will again appear on screen for 1.5 seconds, after which you will be able to make a response. You have a limited time to make a response, so be sure to be quick! Unlike the other tasks, there will be a short delay between when you make a button press and when the trial ends. Please try to only press one key during the response time. Remember, make your judgment based on the size of the items on the screen, not the size of the items in the real world. Each trial will be separated by a blank screen with a cross at the center.\n\nPress 1 to begin.'
# check responses
if EncPractice1Resp.keys in ['', [], None]:  # No response was made
    EncPractice1Resp.keys = None
    # was no response the correct answer?!
    if str(EncPractice1_corrkey).lower() == 'none':
       EncPractice1Resp.corr = 1;  # correct non-response
    else:
       EncPractice1Resp.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('EncPractice1Resp.keys',EncPractice1Resp.keys)
thisExp.addData('EncPractice1Resp.corr', EncPractice1Resp.corr)
if EncPractice1Resp.keys != None:  # we had a response
    thisExp.addData('EncPractice1Resp.rt', EncPractice1Resp.rt)
thisExp.nextEntry()
# the Routine "EncPractice1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EncPostPractice1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
EncPractice1Feedback.setText(EncPractice1_Feedback)
EncPractice1FeedbackResp.keys = []
EncPractice1FeedbackResp.rt = []
_EncPractice1FeedbackResp_allKeys = []
# keep track of which components have finished
EncPostPractice1Components = [EncPractice1Feedback, EncPractice1FeedbackResp]
for thisComponent in EncPostPractice1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EncPostPractice1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EncPractice1Feedback* updates
    if EncPractice1Feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EncPractice1Feedback.frameNStart = frameN  # exact frame index
        EncPractice1Feedback.tStart = t  # local t and not account for scr refresh
        EncPractice1Feedback.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EncPractice1Feedback, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EncPractice1Feedback.started')
        EncPractice1Feedback.setAutoDraw(True)
    
    # *EncPractice1FeedbackResp* updates
    waitOnFlip = False
    if EncPractice1FeedbackResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EncPractice1FeedbackResp.frameNStart = frameN  # exact frame index
        EncPractice1FeedbackResp.tStart = t  # local t and not account for scr refresh
        EncPractice1FeedbackResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EncPractice1FeedbackResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EncPractice1FeedbackResp.started')
        EncPractice1FeedbackResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EncPractice1FeedbackResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EncPractice1FeedbackResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EncPractice1FeedbackResp.status == STARTED and not waitOnFlip:
        theseKeys = EncPractice1FeedbackResp.getKeys(keyList=['1'], waitRelease=False)
        _EncPractice1FeedbackResp_allKeys.extend(theseKeys)
        if len(_EncPractice1FeedbackResp_allKeys):
            EncPractice1FeedbackResp.keys = _EncPractice1FeedbackResp_allKeys[-1].name  # just the last key pressed
            EncPractice1FeedbackResp.rt = _EncPractice1FeedbackResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EncPostPractice1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EncPostPractice1" ---
for thisComponent in EncPostPractice1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if EncPractice1FeedbackResp.keys in ['', [], None]:  # No response was made
    EncPractice1FeedbackResp.keys = None
thisExp.addData('EncPractice1FeedbackResp.keys',EncPractice1FeedbackResp.keys)
if EncPractice1FeedbackResp.keys != None:  # we had a response
    thisExp.addData('EncPractice1FeedbackResp.rt', EncPractice1FeedbackResp.rt)
thisExp.nextEntry()
# the Routine "EncPostPractice1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
EncPractice2Trials = data.TrialHandler(nReps=4.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='EncPractice2Trials')
thisExp.addLoop(EncPractice2Trials)  # add the loop to the experiment
thisEncPractice2Trial = EncPractice2Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEncPractice2Trial.rgb)
if thisEncPractice2Trial != None:
    for paramName in thisEncPractice2Trial:
        exec('{} = thisEncPractice2Trial[paramName]'.format(paramName))

for thisEncPractice2Trial in EncPractice2Trials:
    currentLoop = EncPractice2Trials
    # abbreviate parameter names if possible (e.g. rgb = thisEncPractice2Trial.rgb)
    if thisEncPractice2Trial != None:
        for paramName in thisEncPractice2Trial:
            exec('{} = thisEncPractice2Trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ISI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [FixCross]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixCross* updates
        if FixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixCross.frameNStart = frameN  # exact frame index
            FixCross.tStart = t  # local t and not account for scr refresh
            FixCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixCross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FixCross.started')
            FixCross.setAutoDraw(True)
        if FixCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixCross.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                FixCross.tStop = t  # not accounting for scr refresh
                FixCross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FixCross.stopped')
                FixCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI" ---
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "EncTrial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from EncTrialCode
    Enc_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Enc_stim/'
    Enc_image_fp = os.path.join(Enc_image_fp, enc_stim[shuffled_order[enc_stim_counter]])
    Enc_corrkey = str(enc_stim_corr_keys[shuffled_order[enc_stim_counter]])
    thisExp.addData('corr_key', Enc_corrkey)
    thisExp.addData('stim_name', enc_stim[shuffled_order[enc_stim_counter]])
    thisExp.addData('stim_spec', enc_stim_spec[shuffled_order[enc_stim_counter]])
    enc_stim_counter += 1
    EncImage.setImage(Enc_image_fp)
    EncTrialRespText.setText('?     >     =     <')
    EncTrialResp.keys = []
    EncTrialResp.rt = []
    _EncTrialResp_allKeys = []
    # keep track of which components have finished
    EncTrialComponents = [EncImage, EncTrialRespText, EncTrialResp]
    for thisComponent in EncTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EncTrial" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *EncImage* updates
        if EncImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EncImage.frameNStart = frameN  # exact frame index
            EncImage.tStart = t  # local t and not account for scr refresh
            EncImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EncImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EncImage.started')
            EncImage.setAutoDraw(True)
        if EncImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EncImage.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                EncImage.tStop = t  # not accounting for scr refresh
                EncImage.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EncImage.stopped')
                EncImage.setAutoDraw(False)
        
        # *EncTrialRespText* updates
        if EncTrialRespText.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            EncTrialRespText.frameNStart = frameN  # exact frame index
            EncTrialRespText.tStart = t  # local t and not account for scr refresh
            EncTrialRespText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EncTrialRespText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EncTrialRespText.started')
            EncTrialRespText.setAutoDraw(True)
        if EncTrialRespText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EncTrialRespText.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                EncTrialRespText.tStop = t  # not accounting for scr refresh
                EncTrialRespText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EncTrialRespText.stopped')
                EncTrialRespText.setAutoDraw(False)
        
        # *EncTrialResp* updates
        waitOnFlip = False
        if EncTrialResp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            EncTrialResp.frameNStart = frameN  # exact frame index
            EncTrialResp.tStart = t  # local t and not account for scr refresh
            EncTrialResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EncTrialResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EncTrialResp.started')
            EncTrialResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(EncTrialResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(EncTrialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if EncTrialResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EncTrialResp.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                EncTrialResp.tStop = t  # not accounting for scr refresh
                EncTrialResp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EncTrialResp.stopped')
                EncTrialResp.status = FINISHED
        if EncTrialResp.status == STARTED and not waitOnFlip:
            theseKeys = EncTrialResp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
            _EncTrialResp_allKeys.extend(theseKeys)
            if len(_EncTrialResp_allKeys):
                EncTrialResp.keys = _EncTrialResp_allKeys[-1].name  # just the last key pressed
                EncTrialResp.rt = _EncTrialResp_allKeys[-1].rt
                # was this correct?
                if (EncTrialResp.keys == str(Enc_corrkey)) or (EncTrialResp.keys == Enc_corrkey):
                    EncTrialResp.corr = 1
                else:
                    EncTrialResp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EncTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EncTrial" ---
    for thisComponent in EncTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if EncTrialResp.keys in ['', [], None]:  # No response was made
        EncTrialResp.keys = None
        # was no response the correct answer?!
        if str(Enc_corrkey).lower() == 'none':
           EncTrialResp.corr = 1;  # correct non-response
        else:
           EncTrialResp.corr = 0;  # failed to respond (incorrectly)
    # store data for EncPractice2Trials (TrialHandler)
    EncPractice2Trials.addData('EncTrialResp.keys',EncTrialResp.keys)
    EncPractice2Trials.addData('EncTrialResp.corr', EncTrialResp.corr)
    if EncTrialResp.keys != None:  # we had a response
        EncPractice2Trials.addData('EncTrialResp.rt', EncTrialResp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'EncPractice2Trials'


# --- Prepare to start Routine "EncPracticeEnd" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
EncPracticeEndResp.keys = []
EncPracticeEndResp.rt = []
_EncPracticeEndResp_allKeys = []
# keep track of which components have finished
EncPracticeEndComponents = [EncPracticeEndText, EncPracticeEndResp]
for thisComponent in EncPracticeEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EncPracticeEnd" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EncPracticeEndText* updates
    if EncPracticeEndText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EncPracticeEndText.frameNStart = frameN  # exact frame index
        EncPracticeEndText.tStart = t  # local t and not account for scr refresh
        EncPracticeEndText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EncPracticeEndText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EncPracticeEndText.started')
        EncPracticeEndText.setAutoDraw(True)
    
    # *EncPracticeEndResp* updates
    waitOnFlip = False
    if EncPracticeEndResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EncPracticeEndResp.frameNStart = frameN  # exact frame index
        EncPracticeEndResp.tStart = t  # local t and not account for scr refresh
        EncPracticeEndResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EncPracticeEndResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EncPracticeEndResp.started')
        EncPracticeEndResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EncPracticeEndResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EncPracticeEndResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EncPracticeEndResp.status == STARTED and not waitOnFlip:
        theseKeys = EncPracticeEndResp.getKeys(keyList=['1'], waitRelease=False)
        _EncPracticeEndResp_allKeys.extend(theseKeys)
        if len(_EncPracticeEndResp_allKeys):
            EncPracticeEndResp.keys = _EncPracticeEndResp_allKeys[-1].name  # just the last key pressed
            EncPracticeEndResp.rt = _EncPracticeEndResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EncPracticeEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EncPracticeEnd" ---
for thisComponent in EncPracticeEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if EncPracticeEndResp.keys in ['', [], None]:  # No response was made
    EncPracticeEndResp.keys = None
thisExp.addData('EncPracticeEndResp.keys',EncPracticeEndResp.keys)
if EncPracticeEndResp.keys != None:  # we had a response
    thisExp.addData('EncPracticeEndResp.rt', EncPracticeEndResp.rt)
thisExp.nextEntry()
# the Routine "EncPracticeEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "RetPracticeInstructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
RetPracticeInstructionsResp.keys = []
RetPracticeInstructionsResp.rt = []
_RetPracticeInstructionsResp_allKeys = []
# keep track of which components have finished
RetPracticeInstructionsComponents = [RetPracticeInstructionsText1, RetPracticeInstructionsText2, RetPracticeInstructionsResp, RetPracticeInstructions1Berry, RetPracticeInstructions1Question, RetPracticeInstructions1Truck, RetPracticeInstructions1House, RetPracticeInstructionsNumGuide1, RetPracticeInstructionsNumGuide2, RetPracticeInstructionsNumGuide3, RetPracticeInstructionsNumGuide4]
for thisComponent in RetPracticeInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "RetPracticeInstructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *RetPracticeInstructionsText1* updates
    if RetPracticeInstructionsText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPracticeInstructionsText1.frameNStart = frameN  # exact frame index
        RetPracticeInstructionsText1.tStart = t  # local t and not account for scr refresh
        RetPracticeInstructionsText1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPracticeInstructionsText1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPracticeInstructionsText1.started')
        RetPracticeInstructionsText1.setAutoDraw(True)
    
    # *RetPracticeInstructionsText2* updates
    if RetPracticeInstructionsText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPracticeInstructionsText2.frameNStart = frameN  # exact frame index
        RetPracticeInstructionsText2.tStart = t  # local t and not account for scr refresh
        RetPracticeInstructionsText2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPracticeInstructionsText2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPracticeInstructionsText2.started')
        RetPracticeInstructionsText2.setAutoDraw(True)
    
    # *RetPracticeInstructionsResp* updates
    waitOnFlip = False
    if RetPracticeInstructionsResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPracticeInstructionsResp.frameNStart = frameN  # exact frame index
        RetPracticeInstructionsResp.tStart = t  # local t and not account for scr refresh
        RetPracticeInstructionsResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPracticeInstructionsResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPracticeInstructionsResp.started')
        RetPracticeInstructionsResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(RetPracticeInstructionsResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(RetPracticeInstructionsResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if RetPracticeInstructionsResp.status == STARTED and not waitOnFlip:
        theseKeys = RetPracticeInstructionsResp.getKeys(keyList=['space'], waitRelease=False)
        _RetPracticeInstructionsResp_allKeys.extend(theseKeys)
        if len(_RetPracticeInstructionsResp_allKeys):
            RetPracticeInstructionsResp.keys = _RetPracticeInstructionsResp_allKeys[-1].name  # just the last key pressed
            RetPracticeInstructionsResp.rt = _RetPracticeInstructionsResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *RetPracticeInstructions1Berry* updates
    if RetPracticeInstructions1Berry.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPracticeInstructions1Berry.frameNStart = frameN  # exact frame index
        RetPracticeInstructions1Berry.tStart = t  # local t and not account for scr refresh
        RetPracticeInstructions1Berry.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPracticeInstructions1Berry, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPracticeInstructions1Berry.started')
        RetPracticeInstructions1Berry.setAutoDraw(True)
    
    # *RetPracticeInstructions1Question* updates
    if RetPracticeInstructions1Question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPracticeInstructions1Question.frameNStart = frameN  # exact frame index
        RetPracticeInstructions1Question.tStart = t  # local t and not account for scr refresh
        RetPracticeInstructions1Question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPracticeInstructions1Question, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPracticeInstructions1Question.started')
        RetPracticeInstructions1Question.setAutoDraw(True)
    
    # *RetPracticeInstructions1Truck* updates
    if RetPracticeInstructions1Truck.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPracticeInstructions1Truck.frameNStart = frameN  # exact frame index
        RetPracticeInstructions1Truck.tStart = t  # local t and not account for scr refresh
        RetPracticeInstructions1Truck.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPracticeInstructions1Truck, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPracticeInstructions1Truck.started')
        RetPracticeInstructions1Truck.setAutoDraw(True)
    
    # *RetPracticeInstructions1House* updates
    if RetPracticeInstructions1House.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPracticeInstructions1House.frameNStart = frameN  # exact frame index
        RetPracticeInstructions1House.tStart = t  # local t and not account for scr refresh
        RetPracticeInstructions1House.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPracticeInstructions1House, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPracticeInstructions1House.started')
        RetPracticeInstructions1House.setAutoDraw(True)
    
    # *RetPracticeInstructionsNumGuide1* updates
    if RetPracticeInstructionsNumGuide1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPracticeInstructionsNumGuide1.frameNStart = frameN  # exact frame index
        RetPracticeInstructionsNumGuide1.tStart = t  # local t and not account for scr refresh
        RetPracticeInstructionsNumGuide1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPracticeInstructionsNumGuide1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPracticeInstructionsNumGuide1.started')
        RetPracticeInstructionsNumGuide1.setAutoDraw(True)
    
    # *RetPracticeInstructionsNumGuide2* updates
    if RetPracticeInstructionsNumGuide2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPracticeInstructionsNumGuide2.frameNStart = frameN  # exact frame index
        RetPracticeInstructionsNumGuide2.tStart = t  # local t and not account for scr refresh
        RetPracticeInstructionsNumGuide2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPracticeInstructionsNumGuide2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPracticeInstructionsNumGuide2.started')
        RetPracticeInstructionsNumGuide2.setAutoDraw(True)
    
    # *RetPracticeInstructionsNumGuide3* updates
    if RetPracticeInstructionsNumGuide3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPracticeInstructionsNumGuide3.frameNStart = frameN  # exact frame index
        RetPracticeInstructionsNumGuide3.tStart = t  # local t and not account for scr refresh
        RetPracticeInstructionsNumGuide3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPracticeInstructionsNumGuide3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPracticeInstructionsNumGuide3.started')
        RetPracticeInstructionsNumGuide3.setAutoDraw(True)
    
    # *RetPracticeInstructionsNumGuide4* updates
    if RetPracticeInstructionsNumGuide4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPracticeInstructionsNumGuide4.frameNStart = frameN  # exact frame index
        RetPracticeInstructionsNumGuide4.tStart = t  # local t and not account for scr refresh
        RetPracticeInstructionsNumGuide4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPracticeInstructionsNumGuide4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPracticeInstructionsNumGuide4.started')
        RetPracticeInstructionsNumGuide4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RetPracticeInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "RetPracticeInstructions" ---
for thisComponent in RetPracticeInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if RetPracticeInstructionsResp.keys in ['', [], None]:  # No response was made
    RetPracticeInstructionsResp.keys = None
thisExp.addData('RetPracticeInstructionsResp.keys',RetPracticeInstructionsResp.keys)
if RetPracticeInstructionsResp.keys != None:  # we had a response
    thisExp.addData('RetPracticeInstructionsResp.rt', RetPracticeInstructionsResp.rt)
thisExp.nextEntry()
# the Routine "RetPracticeInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "RetPracticeInstructions2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
RetPracticeInstructions2Resp.keys = []
RetPracticeInstructions2Resp.rt = []
_RetPracticeInstructions2Resp_allKeys = []
# keep track of which components have finished
RetPracticeInstructions2Components = [RetPracticeInstructions2Text, RetPracticeInstructions2Resp]
for thisComponent in RetPracticeInstructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "RetPracticeInstructions2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *RetPracticeInstructions2Text* updates
    if RetPracticeInstructions2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPracticeInstructions2Text.frameNStart = frameN  # exact frame index
        RetPracticeInstructions2Text.tStart = t  # local t and not account for scr refresh
        RetPracticeInstructions2Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPracticeInstructions2Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPracticeInstructions2Text.started')
        RetPracticeInstructions2Text.setAutoDraw(True)
    
    # *RetPracticeInstructions2Resp* updates
    waitOnFlip = False
    if RetPracticeInstructions2Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPracticeInstructions2Resp.frameNStart = frameN  # exact frame index
        RetPracticeInstructions2Resp.tStart = t  # local t and not account for scr refresh
        RetPracticeInstructions2Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPracticeInstructions2Resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPracticeInstructions2Resp.started')
        RetPracticeInstructions2Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(RetPracticeInstructions2Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(RetPracticeInstructions2Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if RetPracticeInstructions2Resp.status == STARTED and not waitOnFlip:
        theseKeys = RetPracticeInstructions2Resp.getKeys(keyList=['1'], waitRelease=False)
        _RetPracticeInstructions2Resp_allKeys.extend(theseKeys)
        if len(_RetPracticeInstructions2Resp_allKeys):
            RetPracticeInstructions2Resp.keys = _RetPracticeInstructions2Resp_allKeys[-1].name  # just the last key pressed
            RetPracticeInstructions2Resp.rt = _RetPracticeInstructions2Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RetPracticeInstructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "RetPracticeInstructions2" ---
for thisComponent in RetPracticeInstructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if RetPracticeInstructions2Resp.keys in ['', [], None]:  # No response was made
    RetPracticeInstructions2Resp.keys = None
thisExp.addData('RetPracticeInstructions2Resp.keys',RetPracticeInstructions2Resp.keys)
if RetPracticeInstructions2Resp.keys != None:  # we had a response
    thisExp.addData('RetPracticeInstructions2Resp.rt', RetPracticeInstructions2Resp.rt)
thisExp.nextEntry()
# the Routine "RetPracticeInstructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "RetPractice1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from RetPractice1Code
Ret_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Ret_stim/'
Ret_image_fp = os.path.join(Ret_image_fp, ret_stim[ret_shuffled_order[ret_stim_counter]])
RetPractice1_corrkey = str(ret_stim_corr_keys[ret_shuffled_order[ret_stim_counter]])
thisExp.addData('corr_key', RetPractice1_corrkey)
thisExp.addData('stim_name', ret_stim[ret_shuffled_order[ret_stim_counter]])
thisExp.addData('stim_spec', ret_stim_spec[ret_shuffled_order[ret_stim_counter]])
thisExp.addData('enc_stimname', ret_enc_stimname[ret_shuffled_order[ret_stim_counter]])
ret_stim_counter += 1
RetPractice1Stim.setImage(Ret_image_fp)
RetPractice1Resp.keys = []
RetPractice1Resp.rt = []
_RetPractice1Resp_allKeys = []
RetPractice1Berry.setImage('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Repeating_Ret_Stim/fruit.jpeg')
RetPractice1Question.setText('?')
RetPractice1Truck.setImage('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Repeating_Ret_Stim/vehicle.jpg')
RetPractice1House.setImage('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Repeating_Ret_Stim/building.jpg')
# keep track of which components have finished
RetPractice1Components = [RetPractice1Stim, RetPractice1Resp, RetPractice1Berry, RetPractice1Question, RetPractice1Truck, RetPractice1House]
for thisComponent in RetPractice1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "RetPractice1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *RetPractice1Stim* updates
    if RetPractice1Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPractice1Stim.frameNStart = frameN  # exact frame index
        RetPractice1Stim.tStart = t  # local t and not account for scr refresh
        RetPractice1Stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPractice1Stim, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPractice1Stim.started')
        RetPractice1Stim.setAutoDraw(True)
    
    # *RetPractice1Resp* updates
    waitOnFlip = False
    if RetPractice1Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPractice1Resp.frameNStart = frameN  # exact frame index
        RetPractice1Resp.tStart = t  # local t and not account for scr refresh
        RetPractice1Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPractice1Resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPractice1Resp.started')
        RetPractice1Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(RetPractice1Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(RetPractice1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if RetPractice1Resp.status == STARTED and not waitOnFlip:
        theseKeys = RetPractice1Resp.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
        _RetPractice1Resp_allKeys.extend(theseKeys)
        if len(_RetPractice1Resp_allKeys):
            RetPractice1Resp.keys = _RetPractice1Resp_allKeys[-1].name  # just the last key pressed
            RetPractice1Resp.rt = _RetPractice1Resp_allKeys[-1].rt
            # was this correct?
            if (RetPractice1Resp.keys == str(RetPractice1_corrkey)) or (RetPractice1Resp.keys == RetPractice1_corrkey):
                RetPractice1Resp.corr = 1
            else:
                RetPractice1Resp.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # *RetPractice1Berry* updates
    if RetPractice1Berry.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
        # keep track of start time/frame for later
        RetPractice1Berry.frameNStart = frameN  # exact frame index
        RetPractice1Berry.tStart = t  # local t and not account for scr refresh
        RetPractice1Berry.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPractice1Berry, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPractice1Berry.started')
        RetPractice1Berry.setAutoDraw(True)
    
    # *RetPractice1Question* updates
    if RetPractice1Question.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
        # keep track of start time/frame for later
        RetPractice1Question.frameNStart = frameN  # exact frame index
        RetPractice1Question.tStart = t  # local t and not account for scr refresh
        RetPractice1Question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPractice1Question, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPractice1Question.started')
        RetPractice1Question.setAutoDraw(True)
    
    # *RetPractice1Truck* updates
    if RetPractice1Truck.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
        # keep track of start time/frame for later
        RetPractice1Truck.frameNStart = frameN  # exact frame index
        RetPractice1Truck.tStart = t  # local t and not account for scr refresh
        RetPractice1Truck.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPractice1Truck, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPractice1Truck.started')
        RetPractice1Truck.setAutoDraw(True)
    
    # *RetPractice1House* updates
    if RetPractice1House.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
        # keep track of start time/frame for later
        RetPractice1House.frameNStart = frameN  # exact frame index
        RetPractice1House.tStart = t  # local t and not account for scr refresh
        RetPractice1House.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPractice1House, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPractice1House.started')
        RetPractice1House.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RetPractice1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "RetPractice1" ---
for thisComponent in RetPractice1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from RetPractice1Code
if RetPractice1Resp.keys == RetPractice1_corrkey:
    RetPractice1_Feedback = 'Well done!\n\nWe will now practice with a time constraint. The image will again appear on screen for 1.5 seconds, after which you will be able to make a response. You have a limited time to make a response, so be sure to be quick! Each trial will be separated by a blank screen with a cross at the center.\n\nPress 1 to begin.'
else:
    RetPractice1_Feedback = 'Not quite, but you will have more practice now!\n\nThe next practice trials will have a time constraint. The equations will again appear on screen for 1.5 seconds, after which you will be able to make a response. You have a limited time to make a response, so be sure to be quick! Each trial will be separated by a blank screen with a cross at the center.\n\nPress 1 to begin.'
# check responses
if RetPractice1Resp.keys in ['', [], None]:  # No response was made
    RetPractice1Resp.keys = None
    # was no response the correct answer?!
    if str(RetPractice1_corrkey).lower() == 'none':
       RetPractice1Resp.corr = 1;  # correct non-response
    else:
       RetPractice1Resp.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('RetPractice1Resp.keys',RetPractice1Resp.keys)
thisExp.addData('RetPractice1Resp.corr', RetPractice1Resp.corr)
if RetPractice1Resp.keys != None:  # we had a response
    thisExp.addData('RetPractice1Resp.rt', RetPractice1Resp.rt)
thisExp.nextEntry()
# the Routine "RetPractice1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "RetPostPractice1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
RetPostPractice1Text.setText(RetPractice1_Feedback)
RetPostPractice1Resp.keys = []
RetPostPractice1Resp.rt = []
_RetPostPractice1Resp_allKeys = []
# keep track of which components have finished
RetPostPractice1Components = [RetPostPractice1Text, RetPostPractice1Resp]
for thisComponent in RetPostPractice1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "RetPostPractice1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *RetPostPractice1Text* updates
    if RetPostPractice1Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPostPractice1Text.frameNStart = frameN  # exact frame index
        RetPostPractice1Text.tStart = t  # local t and not account for scr refresh
        RetPostPractice1Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPostPractice1Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPostPractice1Text.started')
        RetPostPractice1Text.setAutoDraw(True)
    
    # *RetPostPractice1Resp* updates
    waitOnFlip = False
    if RetPostPractice1Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPostPractice1Resp.frameNStart = frameN  # exact frame index
        RetPostPractice1Resp.tStart = t  # local t and not account for scr refresh
        RetPostPractice1Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPostPractice1Resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPostPractice1Resp.started')
        RetPostPractice1Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(RetPostPractice1Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(RetPostPractice1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if RetPostPractice1Resp.status == STARTED and not waitOnFlip:
        theseKeys = RetPostPractice1Resp.getKeys(keyList=['1'], waitRelease=False)
        _RetPostPractice1Resp_allKeys.extend(theseKeys)
        if len(_RetPostPractice1Resp_allKeys):
            RetPostPractice1Resp.keys = _RetPostPractice1Resp_allKeys[-1].name  # just the last key pressed
            RetPostPractice1Resp.rt = _RetPostPractice1Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RetPostPractice1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "RetPostPractice1" ---
for thisComponent in RetPostPractice1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if RetPostPractice1Resp.keys in ['', [], None]:  # No response was made
    RetPostPractice1Resp.keys = None
thisExp.addData('RetPostPractice1Resp.keys',RetPostPractice1Resp.keys)
if RetPostPractice1Resp.keys != None:  # we had a response
    thisExp.addData('RetPostPractice1Resp.rt', RetPostPractice1Resp.rt)
thisExp.nextEntry()
# the Routine "RetPostPractice1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
RetPractice2Trials = data.TrialHandler(nReps=4.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='RetPractice2Trials')
thisExp.addLoop(RetPractice2Trials)  # add the loop to the experiment
thisRetPractice2Trial = RetPractice2Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRetPractice2Trial.rgb)
if thisRetPractice2Trial != None:
    for paramName in thisRetPractice2Trial:
        exec('{} = thisRetPractice2Trial[paramName]'.format(paramName))

for thisRetPractice2Trial in RetPractice2Trials:
    currentLoop = RetPractice2Trials
    # abbreviate parameter names if possible (e.g. rgb = thisRetPractice2Trial.rgb)
    if thisRetPractice2Trial != None:
        for paramName in thisRetPractice2Trial:
            exec('{} = thisRetPractice2Trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ISI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [FixCross]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixCross* updates
        if FixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixCross.frameNStart = frameN  # exact frame index
            FixCross.tStart = t  # local t and not account for scr refresh
            FixCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixCross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FixCross.started')
            FixCross.setAutoDraw(True)
        if FixCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixCross.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                FixCross.tStop = t  # not accounting for scr refresh
                FixCross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FixCross.stopped')
                FixCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI" ---
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "RetTrial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from RetTrialCode
    Ret_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Ret_stim/'
    Ret_image_fp = os.path.join(Ret_image_fp, ret_stim[ret_shuffled_order[ret_stim_counter]])
    Ret_corrkey = str(ret_stim_corr_keys[ret_shuffled_order[ret_stim_counter]])
    thisExp.addData('corr_key', Ret_corrkey)
    thisExp.addData('stim_name', ret_stim[ret_shuffled_order[ret_stim_counter]])
    thisExp.addData('stim_spec', ret_stim_spec[ret_shuffled_order[ret_stim_counter]])
    thisExp.addData('enc_stimname', ret_enc_stimname[ret_shuffled_order[ret_stim_counter]])
    ret_stim_counter += 1
    RetTrialStim.setImage(Ret_image_fp)
    RetTrialResp.keys = []
    RetTrialResp.rt = []
    _RetTrialResp_allKeys = []
    RetTrialQuestion.setText('?')
    RetTrialBerry.setImage('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Repeating_Ret_Stim/fruit.jpeg')
    RetTrialTruck.setImage('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Repeating_Ret_Stim/vehicle.jpg')
    RetTrialHouse.setImage('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Repeating_Ret_Stim/building.jpg')
    # keep track of which components have finished
    RetTrialComponents = [RetTrialStim, RetTrialResp, RetTrialQuestion, RetTrialBerry, RetTrialTruck, RetTrialHouse]
    for thisComponent in RetTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "RetTrial" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *RetTrialStim* updates
        if RetTrialStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RetTrialStim.frameNStart = frameN  # exact frame index
            RetTrialStim.tStart = t  # local t and not account for scr refresh
            RetTrialStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RetTrialStim, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RetTrialStim.started')
            RetTrialStim.setAutoDraw(True)
        if RetTrialStim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RetTrialStim.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                RetTrialStim.tStop = t  # not accounting for scr refresh
                RetTrialStim.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialStim.stopped')
                RetTrialStim.setAutoDraw(False)
        
        # *RetTrialResp* updates
        waitOnFlip = False
        if RetTrialResp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            RetTrialResp.frameNStart = frameN  # exact frame index
            RetTrialResp.tStart = t  # local t and not account for scr refresh
            RetTrialResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RetTrialResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RetTrialResp.started')
            RetTrialResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(RetTrialResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(RetTrialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RetTrialResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RetTrialResp.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                RetTrialResp.tStop = t  # not accounting for scr refresh
                RetTrialResp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialResp.stopped')
                RetTrialResp.status = FINISHED
        if RetTrialResp.status == STARTED and not waitOnFlip:
            theseKeys = RetTrialResp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
            _RetTrialResp_allKeys.extend(theseKeys)
            if len(_RetTrialResp_allKeys):
                RetTrialResp.keys = _RetTrialResp_allKeys[-1].name  # just the last key pressed
                RetTrialResp.rt = _RetTrialResp_allKeys[-1].rt
                # was this correct?
                if (RetTrialResp.keys == str(Ret_corrkey)) or (RetTrialResp.keys == Ret_corrkey):
                    RetTrialResp.corr = 1
                else:
                    RetTrialResp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *RetTrialQuestion* updates
        if RetTrialQuestion.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            RetTrialQuestion.frameNStart = frameN  # exact frame index
            RetTrialQuestion.tStart = t  # local t and not account for scr refresh
            RetTrialQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RetTrialQuestion, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RetTrialQuestion.started')
            RetTrialQuestion.setAutoDraw(True)
        if RetTrialQuestion.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RetTrialQuestion.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                RetTrialQuestion.tStop = t  # not accounting for scr refresh
                RetTrialQuestion.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialQuestion.stopped')
                RetTrialQuestion.setAutoDraw(False)
        
        # *RetTrialBerry* updates
        if RetTrialBerry.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            RetTrialBerry.frameNStart = frameN  # exact frame index
            RetTrialBerry.tStart = t  # local t and not account for scr refresh
            RetTrialBerry.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RetTrialBerry, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RetTrialBerry.started')
            RetTrialBerry.setAutoDraw(True)
        if RetTrialBerry.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RetTrialBerry.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                RetTrialBerry.tStop = t  # not accounting for scr refresh
                RetTrialBerry.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialBerry.stopped')
                RetTrialBerry.setAutoDraw(False)
        
        # *RetTrialTruck* updates
        if RetTrialTruck.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            RetTrialTruck.frameNStart = frameN  # exact frame index
            RetTrialTruck.tStart = t  # local t and not account for scr refresh
            RetTrialTruck.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RetTrialTruck, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RetTrialTruck.started')
            RetTrialTruck.setAutoDraw(True)
        if RetTrialTruck.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RetTrialTruck.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                RetTrialTruck.tStop = t  # not accounting for scr refresh
                RetTrialTruck.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialTruck.stopped')
                RetTrialTruck.setAutoDraw(False)
        
        # *RetTrialHouse* updates
        if RetTrialHouse.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            RetTrialHouse.frameNStart = frameN  # exact frame index
            RetTrialHouse.tStart = t  # local t and not account for scr refresh
            RetTrialHouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RetTrialHouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RetTrialHouse.started')
            RetTrialHouse.setAutoDraw(True)
        if RetTrialHouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RetTrialHouse.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                RetTrialHouse.tStop = t  # not accounting for scr refresh
                RetTrialHouse.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialHouse.stopped')
                RetTrialHouse.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RetTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RetTrial" ---
    for thisComponent in RetTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if RetTrialResp.keys in ['', [], None]:  # No response was made
        RetTrialResp.keys = None
        # was no response the correct answer?!
        if str(Ret_corrkey).lower() == 'none':
           RetTrialResp.corr = 1;  # correct non-response
        else:
           RetTrialResp.corr = 0;  # failed to respond (incorrectly)
    # store data for RetPractice2Trials (TrialHandler)
    RetPractice2Trials.addData('RetTrialResp.keys',RetTrialResp.keys)
    RetPractice2Trials.addData('RetTrialResp.corr', RetTrialResp.corr)
    if RetTrialResp.keys != None:  # we had a response
        RetPractice2Trials.addData('RetTrialResp.rt', RetTrialResp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'RetPractice2Trials'


# --- Prepare to start Routine "RetPracticeEnd" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
RetPracticeEndResp.keys = []
RetPracticeEndResp.rt = []
_RetPracticeEndResp_allKeys = []
# keep track of which components have finished
RetPracticeEndComponents = [RetPracticeEndText, RetPracticeEndResp]
for thisComponent in RetPracticeEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "RetPracticeEnd" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *RetPracticeEndText* updates
    if RetPracticeEndText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPracticeEndText.frameNStart = frameN  # exact frame index
        RetPracticeEndText.tStart = t  # local t and not account for scr refresh
        RetPracticeEndText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPracticeEndText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPracticeEndText.started')
        RetPracticeEndText.setAutoDraw(True)
    
    # *RetPracticeEndResp* updates
    waitOnFlip = False
    if RetPracticeEndResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RetPracticeEndResp.frameNStart = frameN  # exact frame index
        RetPracticeEndResp.tStart = t  # local t and not account for scr refresh
        RetPracticeEndResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RetPracticeEndResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RetPracticeEndResp.started')
        RetPracticeEndResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(RetPracticeEndResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(RetPracticeEndResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if RetPracticeEndResp.status == STARTED and not waitOnFlip:
        theseKeys = RetPracticeEndResp.getKeys(keyList=['1'], waitRelease=False)
        _RetPracticeEndResp_allKeys.extend(theseKeys)
        if len(_RetPracticeEndResp_allKeys):
            RetPracticeEndResp.keys = _RetPracticeEndResp_allKeys[-1].name  # just the last key pressed
            RetPracticeEndResp.rt = _RetPracticeEndResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RetPracticeEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "RetPracticeEnd" ---
for thisComponent in RetPracticeEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if RetPracticeEndResp.keys in ['', [], None]:  # No response was made
    RetPracticeEndResp.keys = None
thisExp.addData('RetPracticeEndResp.keys',RetPracticeEndResp.keys)
if RetPracticeEndResp.keys != None:  # we had a response
    thisExp.addData('RetPracticeEndResp.rt', RetPracticeEndResp.rt)
thisExp.nextEntry()
# the Routine "RetPracticeEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Blocks40 = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Blocks40')
thisExp.addLoop(Blocks40)  # add the loop to the experiment
thisBlocks40 = Blocks40.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks40.rgb)
if thisBlocks40 != None:
    for paramName in thisBlocks40:
        exec('{} = thisBlocks40[paramName]'.format(paramName))

for thisBlocks40 in Blocks40:
    currentLoop = Blocks40
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks40.rgb)
    if thisBlocks40 != None:
        for paramName in thisBlocks40:
            exec('{} = thisBlocks40[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "EATaskInstructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Block1Counter
    block_counter += 1
    # keep track of which components have finished
    EATaskInstructionsComponents = [EATaskInstructionsText1, EATaskInstructionsText2]
    for thisComponent in EATaskInstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EATaskInstructions" ---
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *EATaskInstructionsText1* updates
        if EATaskInstructionsText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EATaskInstructionsText1.frameNStart = frameN  # exact frame index
            EATaskInstructionsText1.tStart = t  # local t and not account for scr refresh
            EATaskInstructionsText1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EATaskInstructionsText1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EATaskInstructionsText1.started')
            EATaskInstructionsText1.setAutoDraw(True)
        if EATaskInstructionsText1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EATaskInstructionsText1.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                EATaskInstructionsText1.tStop = t  # not accounting for scr refresh
                EATaskInstructionsText1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATaskInstructionsText1.stopped')
                EATaskInstructionsText1.setAutoDraw(False)
        
        # *EATaskInstructionsText2* updates
        if EATaskInstructionsText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EATaskInstructionsText2.frameNStart = frameN  # exact frame index
            EATaskInstructionsText2.tStart = t  # local t and not account for scr refresh
            EATaskInstructionsText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EATaskInstructionsText2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EATaskInstructionsText2.started')
            EATaskInstructionsText2.setAutoDraw(True)
        if EATaskInstructionsText2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EATaskInstructionsText2.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                EATaskInstructionsText2.tStop = t  # not accounting for scr refresh
                EATaskInstructionsText2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATaskInstructionsText2.stopped')
                EATaskInstructionsText2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EATaskInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EATaskInstructions" ---
    for thisComponent in EATaskInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # set up handler to look after randomisation of conditions etc
    EATrialsBlocks40 = data.TrialHandler(nReps=40.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='EATrialsBlocks40')
    thisExp.addLoop(EATrialsBlocks40)  # add the loop to the experiment
    thisEATrialsBlocks40 = EATrialsBlocks40.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEATrialsBlocks40.rgb)
    if thisEATrialsBlocks40 != None:
        for paramName in thisEATrialsBlocks40:
            exec('{} = thisEATrialsBlocks40[paramName]'.format(paramName))
    
    for thisEATrialsBlocks40 in EATrialsBlocks40:
        currentLoop = EATrialsBlocks40
        # abbreviate parameter names if possible (e.g. rgb = thisEATrialsBlocks40.rgb)
        if thisEATrialsBlocks40 != None:
            for paramName in thisEATrialsBlocks40:
                exec('{} = thisEATrialsBlocks40[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ISI" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [FixCross]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixCross* updates
            if FixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixCross.frameNStart = frameN  # exact frame index
                FixCross.tStart = t  # local t and not account for scr refresh
                FixCross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixCross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FixCross.started')
                FixCross.setAutoDraw(True)
            if FixCross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FixCross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    FixCross.tStop = t  # not accounting for scr refresh
                    FixCross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FixCross.stopped')
                    FixCross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI" ---
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "EATrial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from EATrialCode
        EA_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/ExAttn_stim/'
        EA_image_fp = os.path.join(EA_image_fp, ea_stim[shuffled_order[ea_stim_counter]])
        EA_corrkey = str(ea_stim_corr_keys[shuffled_order[ea_stim_counter]])
        thisExp.addData('corr_key', EA_corrkey)
        thisExp.addData('stim_name', ea_stim[shuffled_order[ea_stim_counter]])
        thisExp.addData('magnitude', ea_stim_magnitude[shuffled_order[ea_stim_counter]])
        thisExp.addData('stim_spec', ea_stim_spec[shuffled_order[ea_stim_counter]])
        thisExp.addData('num_big', ea_stim_big[shuffled_order[ea_stim_counter]])
        ea_stim_counter += 1
        EATrialText1.setText('big _ small')
        EATrialText2.setText('?     >     =     <')
        EATrialStim.setImage(EA_image_fp)
        EATrialResp.keys = []
        EATrialResp.rt = []
        _EATrialResp_allKeys = []
        # keep track of which components have finished
        EATrialComponents = [EATrialText1, EATrialText2, EATrialStim, EATrialResp]
        for thisComponent in EATrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "EATrial" ---
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *EATrialText1* updates
            if EATrialText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EATrialText1.frameNStart = frameN  # exact frame index
                EATrialText1.tStart = t  # local t and not account for scr refresh
                EATrialText1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EATrialText1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATrialText1.started')
                EATrialText1.setAutoDraw(True)
            if EATrialText1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EATrialText1.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    EATrialText1.tStop = t  # not accounting for scr refresh
                    EATrialText1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EATrialText1.stopped')
                    EATrialText1.setAutoDraw(False)
            
            # *EATrialText2* updates
            if EATrialText2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                EATrialText2.frameNStart = frameN  # exact frame index
                EATrialText2.tStart = t  # local t and not account for scr refresh
                EATrialText2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EATrialText2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATrialText2.started')
                EATrialText2.setAutoDraw(True)
            if EATrialText2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EATrialText2.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    EATrialText2.tStop = t  # not accounting for scr refresh
                    EATrialText2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EATrialText2.stopped')
                    EATrialText2.setAutoDraw(False)
            
            # *EATrialStim* updates
            if EATrialStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EATrialStim.frameNStart = frameN  # exact frame index
                EATrialStim.tStart = t  # local t and not account for scr refresh
                EATrialStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EATrialStim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATrialStim.started')
                EATrialStim.setAutoDraw(True)
            if EATrialStim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EATrialStim.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    EATrialStim.tStop = t  # not accounting for scr refresh
                    EATrialStim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EATrialStim.stopped')
                    EATrialStim.setAutoDraw(False)
            
            # *EATrialResp* updates
            waitOnFlip = False
            if EATrialResp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                EATrialResp.frameNStart = frameN  # exact frame index
                EATrialResp.tStart = t  # local t and not account for scr refresh
                EATrialResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EATrialResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATrialResp.started')
                EATrialResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(EATrialResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(EATrialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if EATrialResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EATrialResp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    EATrialResp.tStop = t  # not accounting for scr refresh
                    EATrialResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EATrialResp.stopped')
                    EATrialResp.status = FINISHED
            if EATrialResp.status == STARTED and not waitOnFlip:
                theseKeys = EATrialResp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
                _EATrialResp_allKeys.extend(theseKeys)
                if len(_EATrialResp_allKeys):
                    EATrialResp.keys = _EATrialResp_allKeys[-1].name  # just the last key pressed
                    EATrialResp.rt = _EATrialResp_allKeys[-1].rt
                    # was this correct?
                    if (EATrialResp.keys == str(EA_corrkey)) or (EATrialResp.keys == EA_corrkey):
                        EATrialResp.corr = 1
                    else:
                        EATrialResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EATrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "EATrial" ---
        for thisComponent in EATrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if EATrialResp.keys in ['', [], None]:  # No response was made
            EATrialResp.keys = None
            # was no response the correct answer?!
            if str(EA_corrkey).lower() == 'none':
               EATrialResp.corr = 1;  # correct non-response
            else:
               EATrialResp.corr = 0;  # failed to respond (incorrectly)
        # store data for EATrialsBlocks40 (TrialHandler)
        EATrialsBlocks40.addData('EATrialResp.keys',EATrialResp.keys)
        EATrialsBlocks40.addData('EATrialResp.corr', EATrialResp.corr)
        if EATrialResp.keys != None:  # we had a response
            EATrialsBlocks40.addData('EATrialResp.rt', EATrialResp.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        thisExp.nextEntry()
        
    # completed 40.0 repeats of 'EATrialsBlocks40'
    
    
    # --- Prepare to start Routine "EncTaskInstructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    EncTaskInstructionsText1.setText('Learning & Comparison Task')
    # keep track of which components have finished
    EncTaskInstructionsComponents = [EncTaskInstructionsText1, EncTaskInstructionsText2]
    for thisComponent in EncTaskInstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EncTaskInstructions" ---
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *EncTaskInstructionsText1* updates
        if EncTaskInstructionsText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EncTaskInstructionsText1.frameNStart = frameN  # exact frame index
            EncTaskInstructionsText1.tStart = t  # local t and not account for scr refresh
            EncTaskInstructionsText1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EncTaskInstructionsText1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EncTaskInstructionsText1.started')
            EncTaskInstructionsText1.setAutoDraw(True)
        if EncTaskInstructionsText1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EncTaskInstructionsText1.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                EncTaskInstructionsText1.tStop = t  # not accounting for scr refresh
                EncTaskInstructionsText1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EncTaskInstructionsText1.stopped')
                EncTaskInstructionsText1.setAutoDraw(False)
        
        # *EncTaskInstructionsText2* updates
        if EncTaskInstructionsText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EncTaskInstructionsText2.frameNStart = frameN  # exact frame index
            EncTaskInstructionsText2.tStart = t  # local t and not account for scr refresh
            EncTaskInstructionsText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EncTaskInstructionsText2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EncTaskInstructionsText2.started')
            EncTaskInstructionsText2.setAutoDraw(True)
        if EncTaskInstructionsText2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EncTaskInstructionsText2.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                EncTaskInstructionsText2.tStop = t  # not accounting for scr refresh
                EncTaskInstructionsText2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EncTaskInstructionsText2.stopped')
                EncTaskInstructionsText2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EncTaskInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EncTaskInstructions" ---
    for thisComponent in EncTaskInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # set up handler to look after randomisation of conditions etc
    EncTrialsBlocks40 = data.TrialHandler(nReps=40.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='EncTrialsBlocks40')
    thisExp.addLoop(EncTrialsBlocks40)  # add the loop to the experiment
    thisEncTrialsBlocks40 = EncTrialsBlocks40.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEncTrialsBlocks40.rgb)
    if thisEncTrialsBlocks40 != None:
        for paramName in thisEncTrialsBlocks40:
            exec('{} = thisEncTrialsBlocks40[paramName]'.format(paramName))
    
    for thisEncTrialsBlocks40 in EncTrialsBlocks40:
        currentLoop = EncTrialsBlocks40
        # abbreviate parameter names if possible (e.g. rgb = thisEncTrialsBlocks40.rgb)
        if thisEncTrialsBlocks40 != None:
            for paramName in thisEncTrialsBlocks40:
                exec('{} = thisEncTrialsBlocks40[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ISI" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [FixCross]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixCross* updates
            if FixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixCross.frameNStart = frameN  # exact frame index
                FixCross.tStart = t  # local t and not account for scr refresh
                FixCross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixCross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FixCross.started')
                FixCross.setAutoDraw(True)
            if FixCross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FixCross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    FixCross.tStop = t  # not accounting for scr refresh
                    FixCross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FixCross.stopped')
                    FixCross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI" ---
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "EncTrial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from EncTrialCode
        Enc_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Enc_stim/'
        Enc_image_fp = os.path.join(Enc_image_fp, enc_stim[shuffled_order[enc_stim_counter]])
        Enc_corrkey = str(enc_stim_corr_keys[shuffled_order[enc_stim_counter]])
        thisExp.addData('corr_key', Enc_corrkey)
        thisExp.addData('stim_name', enc_stim[shuffled_order[enc_stim_counter]])
        thisExp.addData('stim_spec', enc_stim_spec[shuffled_order[enc_stim_counter]])
        enc_stim_counter += 1
        EncImage.setImage(Enc_image_fp)
        EncTrialRespText.setText('?     >     =     <')
        EncTrialResp.keys = []
        EncTrialResp.rt = []
        _EncTrialResp_allKeys = []
        # keep track of which components have finished
        EncTrialComponents = [EncImage, EncTrialRespText, EncTrialResp]
        for thisComponent in EncTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "EncTrial" ---
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *EncImage* updates
            if EncImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EncImage.frameNStart = frameN  # exact frame index
                EncImage.tStart = t  # local t and not account for scr refresh
                EncImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EncImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EncImage.started')
                EncImage.setAutoDraw(True)
            if EncImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EncImage.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    EncImage.tStop = t  # not accounting for scr refresh
                    EncImage.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EncImage.stopped')
                    EncImage.setAutoDraw(False)
            
            # *EncTrialRespText* updates
            if EncTrialRespText.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                EncTrialRespText.frameNStart = frameN  # exact frame index
                EncTrialRespText.tStart = t  # local t and not account for scr refresh
                EncTrialRespText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EncTrialRespText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EncTrialRespText.started')
                EncTrialRespText.setAutoDraw(True)
            if EncTrialRespText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EncTrialRespText.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    EncTrialRespText.tStop = t  # not accounting for scr refresh
                    EncTrialRespText.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EncTrialRespText.stopped')
                    EncTrialRespText.setAutoDraw(False)
            
            # *EncTrialResp* updates
            waitOnFlip = False
            if EncTrialResp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                EncTrialResp.frameNStart = frameN  # exact frame index
                EncTrialResp.tStart = t  # local t and not account for scr refresh
                EncTrialResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EncTrialResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EncTrialResp.started')
                EncTrialResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(EncTrialResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(EncTrialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if EncTrialResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EncTrialResp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    EncTrialResp.tStop = t  # not accounting for scr refresh
                    EncTrialResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EncTrialResp.stopped')
                    EncTrialResp.status = FINISHED
            if EncTrialResp.status == STARTED and not waitOnFlip:
                theseKeys = EncTrialResp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
                _EncTrialResp_allKeys.extend(theseKeys)
                if len(_EncTrialResp_allKeys):
                    EncTrialResp.keys = _EncTrialResp_allKeys[-1].name  # just the last key pressed
                    EncTrialResp.rt = _EncTrialResp_allKeys[-1].rt
                    # was this correct?
                    if (EncTrialResp.keys == str(Enc_corrkey)) or (EncTrialResp.keys == Enc_corrkey):
                        EncTrialResp.corr = 1
                    else:
                        EncTrialResp.corr = 0
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EncTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "EncTrial" ---
        for thisComponent in EncTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if EncTrialResp.keys in ['', [], None]:  # No response was made
            EncTrialResp.keys = None
            # was no response the correct answer?!
            if str(Enc_corrkey).lower() == 'none':
               EncTrialResp.corr = 1;  # correct non-response
            else:
               EncTrialResp.corr = 0;  # failed to respond (incorrectly)
        # store data for EncTrialsBlocks40 (TrialHandler)
        EncTrialsBlocks40.addData('EncTrialResp.keys',EncTrialResp.keys)
        EncTrialsBlocks40.addData('EncTrialResp.corr', EncTrialResp.corr)
        if EncTrialResp.keys != None:  # we had a response
            EncTrialsBlocks40.addData('EncTrialResp.rt', EncTrialResp.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        thisExp.nextEntry()
        
    # completed 40.0 repeats of 'EncTrialsBlocks40'
    
    
    # --- Prepare to start Routine "IATaskInstructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    IATaskInstructionsComponents = [IATaskInstructionsText1, IATaskInstructionsText2]
    for thisComponent in IATaskInstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "IATaskInstructions" ---
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IATaskInstructionsText1* updates
        if IATaskInstructionsText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IATaskInstructionsText1.frameNStart = frameN  # exact frame index
            IATaskInstructionsText1.tStart = t  # local t and not account for scr refresh
            IATaskInstructionsText1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IATaskInstructionsText1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IATaskInstructionsText1.started')
            IATaskInstructionsText1.setAutoDraw(True)
        if IATaskInstructionsText1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > IATaskInstructionsText1.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                IATaskInstructionsText1.tStop = t  # not accounting for scr refresh
                IATaskInstructionsText1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IATaskInstructionsText1.stopped')
                IATaskInstructionsText1.setAutoDraw(False)
        
        # *IATaskInstructionsText2* updates
        if IATaskInstructionsText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IATaskInstructionsText2.frameNStart = frameN  # exact frame index
            IATaskInstructionsText2.tStart = t  # local t and not account for scr refresh
            IATaskInstructionsText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IATaskInstructionsText2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IATaskInstructionsText2.started')
            IATaskInstructionsText2.setAutoDraw(True)
        if IATaskInstructionsText2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > IATaskInstructionsText2.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                IATaskInstructionsText2.tStop = t  # not accounting for scr refresh
                IATaskInstructionsText2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IATaskInstructionsText2.stopped')
                IATaskInstructionsText2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IATaskInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "IATaskInstructions" ---
    for thisComponent in IATaskInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # set up handler to look after randomisation of conditions etc
    IATrialsBlocks40 = data.TrialHandler(nReps=40.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='IATrialsBlocks40')
    thisExp.addLoop(IATrialsBlocks40)  # add the loop to the experiment
    thisIATrialsBlocks40 = IATrialsBlocks40.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisIATrialsBlocks40.rgb)
    if thisIATrialsBlocks40 != None:
        for paramName in thisIATrialsBlocks40:
            exec('{} = thisIATrialsBlocks40[paramName]'.format(paramName))
    
    for thisIATrialsBlocks40 in IATrialsBlocks40:
        currentLoop = IATrialsBlocks40
        # abbreviate parameter names if possible (e.g. rgb = thisIATrialsBlocks40.rgb)
        if thisIATrialsBlocks40 != None:
            for paramName in thisIATrialsBlocks40:
                exec('{} = thisIATrialsBlocks40[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ISI" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [FixCross]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixCross* updates
            if FixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixCross.frameNStart = frameN  # exact frame index
                FixCross.tStart = t  # local t and not account for scr refresh
                FixCross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixCross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FixCross.started')
                FixCross.setAutoDraw(True)
            if FixCross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FixCross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    FixCross.tStop = t  # not accounting for scr refresh
                    FixCross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FixCross.stopped')
                    FixCross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI" ---
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "IATrial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from IATrialCode
        IA_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/IntAttn_stim/'
        IA_image_fp = os.path.join(IA_image_fp, ia_stim[shuffled_order[ia_stim_counter]])
        IA_corrkey = str(ia_stim_corr_keys[shuffled_order[ia_stim_counter]])
        thisExp.addData('corr_key', IA_corrkey)
        thisExp.addData('stim_name', ia_stim[shuffled_order[ia_stim_counter]])
        thisExp.addData('magnitude', ia_stim_magnitude[shuffled_order[ia_stim_counter]])
        thisExp.addData('stim_spec', ia_stim_spec[shuffled_order[ia_stim_counter]])
        thisExp.addData('has_neg', ia_stim_hasneg[shuffled_order[ia_stim_counter]])
        ia_stim_counter += 1
        IATrialRespText.setText('?     >     =     <')
        IATrialStim.setImage(IA_image_fp)
        IATrialResp.keys = []
        IATrialResp.rt = []
        _IATrialResp_allKeys = []
        # keep track of which components have finished
        IATrialComponents = [IATrialRespText, IATrialStim, IATrialResp]
        for thisComponent in IATrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "IATrial" ---
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *IATrialRespText* updates
            if IATrialRespText.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                IATrialRespText.frameNStart = frameN  # exact frame index
                IATrialRespText.tStart = t  # local t and not account for scr refresh
                IATrialRespText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IATrialRespText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IATrialRespText.started')
                IATrialRespText.setAutoDraw(True)
            if IATrialRespText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > IATrialRespText.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    IATrialRespText.tStop = t  # not accounting for scr refresh
                    IATrialRespText.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'IATrialRespText.stopped')
                    IATrialRespText.setAutoDraw(False)
            
            # *IATrialStim* updates
            if IATrialStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                IATrialStim.frameNStart = frameN  # exact frame index
                IATrialStim.tStart = t  # local t and not account for scr refresh
                IATrialStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IATrialStim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IATrialStim.started')
                IATrialStim.setAutoDraw(True)
            if IATrialStim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > IATrialStim.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    IATrialStim.tStop = t  # not accounting for scr refresh
                    IATrialStim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'IATrialStim.stopped')
                    IATrialStim.setAutoDraw(False)
            
            # *IATrialResp* updates
            waitOnFlip = False
            if IATrialResp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                IATrialResp.frameNStart = frameN  # exact frame index
                IATrialResp.tStart = t  # local t and not account for scr refresh
                IATrialResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IATrialResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IATrialResp.started')
                IATrialResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(IATrialResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(IATrialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if IATrialResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > IATrialResp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    IATrialResp.tStop = t  # not accounting for scr refresh
                    IATrialResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'IATrialResp.stopped')
                    IATrialResp.status = FINISHED
            if IATrialResp.status == STARTED and not waitOnFlip:
                theseKeys = IATrialResp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
                _IATrialResp_allKeys.extend(theseKeys)
                if len(_IATrialResp_allKeys):
                    IATrialResp.keys = _IATrialResp_allKeys[-1].name  # just the last key pressed
                    IATrialResp.rt = _IATrialResp_allKeys[-1].rt
                    # was this correct?
                    if (IATrialResp.keys == str(IA_corrkey)) or (IATrialResp.keys == IA_corrkey):
                        IATrialResp.corr = 1
                    else:
                        IATrialResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in IATrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "IATrial" ---
        for thisComponent in IATrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if IATrialResp.keys in ['', [], None]:  # No response was made
            IATrialResp.keys = None
            # was no response the correct answer?!
            if str(IA_corrkey).lower() == 'none':
               IATrialResp.corr = 1;  # correct non-response
            else:
               IATrialResp.corr = 0;  # failed to respond (incorrectly)
        # store data for IATrialsBlocks40 (TrialHandler)
        IATrialsBlocks40.addData('IATrialResp.keys',IATrialResp.keys)
        IATrialsBlocks40.addData('IATrialResp.corr', IATrialResp.corr)
        if IATrialResp.keys != None:  # we had a response
            IATrialsBlocks40.addData('IATrialResp.rt', IATrialResp.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        thisExp.nextEntry()
        
    # completed 40.0 repeats of 'IATrialsBlocks40'
    
    
    # --- Prepare to start Routine "RetTaskInstructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    RetTaskInstructionsComponents = [RetTaskInstructionsText1, RetTaskInstructionsText2]
    for thisComponent in RetTaskInstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "RetTaskInstructions" ---
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *RetTaskInstructionsText1* updates
        if RetTaskInstructionsText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RetTaskInstructionsText1.frameNStart = frameN  # exact frame index
            RetTaskInstructionsText1.tStart = t  # local t and not account for scr refresh
            RetTaskInstructionsText1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RetTaskInstructionsText1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RetTaskInstructionsText1.started')
            RetTaskInstructionsText1.setAutoDraw(True)
        if RetTaskInstructionsText1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RetTaskInstructionsText1.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                RetTaskInstructionsText1.tStop = t  # not accounting for scr refresh
                RetTaskInstructionsText1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTaskInstructionsText1.stopped')
                RetTaskInstructionsText1.setAutoDraw(False)
        
        # *RetTaskInstructionsText2* updates
        if RetTaskInstructionsText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RetTaskInstructionsText2.frameNStart = frameN  # exact frame index
            RetTaskInstructionsText2.tStart = t  # local t and not account for scr refresh
            RetTaskInstructionsText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RetTaskInstructionsText2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RetTaskInstructionsText2.started')
            RetTaskInstructionsText2.setAutoDraw(True)
        if RetTaskInstructionsText2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RetTaskInstructionsText2.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                RetTaskInstructionsText2.tStop = t  # not accounting for scr refresh
                RetTaskInstructionsText2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTaskInstructionsText2.stopped')
                RetTaskInstructionsText2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RetTaskInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RetTaskInstructions" ---
    for thisComponent in RetTaskInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # set up handler to look after randomisation of conditions etc
    RetTrialsBlocks40 = data.TrialHandler(nReps=40.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='RetTrialsBlocks40')
    thisExp.addLoop(RetTrialsBlocks40)  # add the loop to the experiment
    thisRetTrialsBlocks40 = RetTrialsBlocks40.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRetTrialsBlocks40.rgb)
    if thisRetTrialsBlocks40 != None:
        for paramName in thisRetTrialsBlocks40:
            exec('{} = thisRetTrialsBlocks40[paramName]'.format(paramName))
    
    for thisRetTrialsBlocks40 in RetTrialsBlocks40:
        currentLoop = RetTrialsBlocks40
        # abbreviate parameter names if possible (e.g. rgb = thisRetTrialsBlocks40.rgb)
        if thisRetTrialsBlocks40 != None:
            for paramName in thisRetTrialsBlocks40:
                exec('{} = thisRetTrialsBlocks40[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ISI" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [FixCross]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixCross* updates
            if FixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixCross.frameNStart = frameN  # exact frame index
                FixCross.tStart = t  # local t and not account for scr refresh
                FixCross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixCross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FixCross.started')
                FixCross.setAutoDraw(True)
            if FixCross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FixCross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    FixCross.tStop = t  # not accounting for scr refresh
                    FixCross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FixCross.stopped')
                    FixCross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI" ---
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "RetTrial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from RetTrialCode
        Ret_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Ret_stim/'
        Ret_image_fp = os.path.join(Ret_image_fp, ret_stim[ret_shuffled_order[ret_stim_counter]])
        Ret_corrkey = str(ret_stim_corr_keys[ret_shuffled_order[ret_stim_counter]])
        thisExp.addData('corr_key', Ret_corrkey)
        thisExp.addData('stim_name', ret_stim[ret_shuffled_order[ret_stim_counter]])
        thisExp.addData('stim_spec', ret_stim_spec[ret_shuffled_order[ret_stim_counter]])
        thisExp.addData('enc_stimname', ret_enc_stimname[ret_shuffled_order[ret_stim_counter]])
        ret_stim_counter += 1
        RetTrialStim.setImage(Ret_image_fp)
        RetTrialResp.keys = []
        RetTrialResp.rt = []
        _RetTrialResp_allKeys = []
        RetTrialQuestion.setText('?')
        RetTrialBerry.setImage('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Repeating_Ret_Stim/fruit.jpeg')
        RetTrialTruck.setImage('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Repeating_Ret_Stim/vehicle.jpg')
        RetTrialHouse.setImage('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Repeating_Ret_Stim/building.jpg')
        # keep track of which components have finished
        RetTrialComponents = [RetTrialStim, RetTrialResp, RetTrialQuestion, RetTrialBerry, RetTrialTruck, RetTrialHouse]
        for thisComponent in RetTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "RetTrial" ---
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *RetTrialStim* updates
            if RetTrialStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RetTrialStim.frameNStart = frameN  # exact frame index
                RetTrialStim.tStart = t  # local t and not account for scr refresh
                RetTrialStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RetTrialStim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialStim.started')
                RetTrialStim.setAutoDraw(True)
            if RetTrialStim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RetTrialStim.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    RetTrialStim.tStop = t  # not accounting for scr refresh
                    RetTrialStim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RetTrialStim.stopped')
                    RetTrialStim.setAutoDraw(False)
            
            # *RetTrialResp* updates
            waitOnFlip = False
            if RetTrialResp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                RetTrialResp.frameNStart = frameN  # exact frame index
                RetTrialResp.tStart = t  # local t and not account for scr refresh
                RetTrialResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RetTrialResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialResp.started')
                RetTrialResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(RetTrialResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(RetTrialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if RetTrialResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RetTrialResp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    RetTrialResp.tStop = t  # not accounting for scr refresh
                    RetTrialResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RetTrialResp.stopped')
                    RetTrialResp.status = FINISHED
            if RetTrialResp.status == STARTED and not waitOnFlip:
                theseKeys = RetTrialResp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
                _RetTrialResp_allKeys.extend(theseKeys)
                if len(_RetTrialResp_allKeys):
                    RetTrialResp.keys = _RetTrialResp_allKeys[-1].name  # just the last key pressed
                    RetTrialResp.rt = _RetTrialResp_allKeys[-1].rt
                    # was this correct?
                    if (RetTrialResp.keys == str(Ret_corrkey)) or (RetTrialResp.keys == Ret_corrkey):
                        RetTrialResp.corr = 1
                    else:
                        RetTrialResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *RetTrialQuestion* updates
            if RetTrialQuestion.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                RetTrialQuestion.frameNStart = frameN  # exact frame index
                RetTrialQuestion.tStart = t  # local t and not account for scr refresh
                RetTrialQuestion.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RetTrialQuestion, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialQuestion.started')
                RetTrialQuestion.setAutoDraw(True)
            if RetTrialQuestion.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RetTrialQuestion.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    RetTrialQuestion.tStop = t  # not accounting for scr refresh
                    RetTrialQuestion.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RetTrialQuestion.stopped')
                    RetTrialQuestion.setAutoDraw(False)
            
            # *RetTrialBerry* updates
            if RetTrialBerry.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                RetTrialBerry.frameNStart = frameN  # exact frame index
                RetTrialBerry.tStart = t  # local t and not account for scr refresh
                RetTrialBerry.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RetTrialBerry, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialBerry.started')
                RetTrialBerry.setAutoDraw(True)
            if RetTrialBerry.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RetTrialBerry.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    RetTrialBerry.tStop = t  # not accounting for scr refresh
                    RetTrialBerry.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RetTrialBerry.stopped')
                    RetTrialBerry.setAutoDraw(False)
            
            # *RetTrialTruck* updates
            if RetTrialTruck.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                RetTrialTruck.frameNStart = frameN  # exact frame index
                RetTrialTruck.tStart = t  # local t and not account for scr refresh
                RetTrialTruck.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RetTrialTruck, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialTruck.started')
                RetTrialTruck.setAutoDraw(True)
            if RetTrialTruck.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RetTrialTruck.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    RetTrialTruck.tStop = t  # not accounting for scr refresh
                    RetTrialTruck.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RetTrialTruck.stopped')
                    RetTrialTruck.setAutoDraw(False)
            
            # *RetTrialHouse* updates
            if RetTrialHouse.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                RetTrialHouse.frameNStart = frameN  # exact frame index
                RetTrialHouse.tStart = t  # local t and not account for scr refresh
                RetTrialHouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RetTrialHouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialHouse.started')
                RetTrialHouse.setAutoDraw(True)
            if RetTrialHouse.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RetTrialHouse.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    RetTrialHouse.tStop = t  # not accounting for scr refresh
                    RetTrialHouse.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RetTrialHouse.stopped')
                    RetTrialHouse.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RetTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "RetTrial" ---
        for thisComponent in RetTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if RetTrialResp.keys in ['', [], None]:  # No response was made
            RetTrialResp.keys = None
            # was no response the correct answer?!
            if str(Ret_corrkey).lower() == 'none':
               RetTrialResp.corr = 1;  # correct non-response
            else:
               RetTrialResp.corr = 0;  # failed to respond (incorrectly)
        # store data for RetTrialsBlocks40 (TrialHandler)
        RetTrialsBlocks40.addData('RetTrialResp.keys',RetTrialResp.keys)
        RetTrialsBlocks40.addData('RetTrialResp.corr', RetTrialResp.corr)
        if RetTrialResp.keys != None:  # we had a response
            RetTrialsBlocks40.addData('RetTrialResp.rt', RetTrialResp.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        thisExp.nextEntry()
        
    # completed 40.0 repeats of 'RetTrialsBlocks40'
    
    
    # --- Prepare to start Routine "Block1End" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Block1EndCode
    if block_counter < 5:
        block1endtext = 'You have finished this block! You will now have a brief 30 second break before the beginning of the next one. Feel free to stretch out, but please do not use any technology or leave the testing room.'
    elif block_counter == 5:
        block1endtext = 'You have finished the first set of blocks! You will now have a self-paced break before the start of the next block, up to three minutes long. Please refrain from using technology during the break. The second set of blocks will take approximately 15 minutes to complete.'
    Block1EndText.setText(block1endtext)
    # keep track of which components have finished
    Block1EndComponents = [Block1EndText]
    for thisComponent in Block1EndComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Block1End" ---
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Block1EndText* updates
        if Block1EndText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Block1EndText.frameNStart = frameN  # exact frame index
            Block1EndText.tStart = t  # local t and not account for scr refresh
            Block1EndText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Block1EndText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Block1EndText.started')
            Block1EndText.setAutoDraw(True)
        if Block1EndText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Block1EndText.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                Block1EndText.tStop = t  # not accounting for scr refresh
                Block1EndText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Block1EndText.stopped')
                Block1EndText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block1EndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Block1End" ---
    for thisComponent in Block1EndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
# completed 5.0 repeats of 'Blocks40'


# --- Prepare to start Routine "Block2Break" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from Block2BreakCode
block_counter = 0
Block2BreakKey.keys = []
Block2BreakKey.rt = []
_Block2BreakKey_allKeys = []
# keep track of which components have finished
Block2BreakComponents = [Block2BreakText, Block2BreakKey]
for thisComponent in Block2BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Block2Break" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Block2BreakText* updates
    if Block2BreakText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Block2BreakText.frameNStart = frameN  # exact frame index
        Block2BreakText.tStart = t  # local t and not account for scr refresh
        Block2BreakText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Block2BreakText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Block2BreakText.started')
        Block2BreakText.setAutoDraw(True)
    
    # *Block2BreakKey* updates
    waitOnFlip = False
    if Block2BreakKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Block2BreakKey.frameNStart = frameN  # exact frame index
        Block2BreakKey.tStart = t  # local t and not account for scr refresh
        Block2BreakKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Block2BreakKey, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Block2BreakKey.started')
        Block2BreakKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Block2BreakKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Block2BreakKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Block2BreakKey.status == STARTED and not waitOnFlip:
        theseKeys = Block2BreakKey.getKeys(keyList=['1'], waitRelease=False)
        _Block2BreakKey_allKeys.extend(theseKeys)
        if len(_Block2BreakKey_allKeys):
            Block2BreakKey.keys = _Block2BreakKey_allKeys[-1].name  # just the last key pressed
            Block2BreakKey.rt = _Block2BreakKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block2BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Block2Break" ---
for thisComponent in Block2BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Block2BreakKey.keys in ['', [], None]:  # No response was made
    Block2BreakKey.keys = None
thisExp.addData('Block2BreakKey.keys',Block2BreakKey.keys)
if Block2BreakKey.keys != None:  # we had a response
    thisExp.addData('Block2BreakKey.rt', Block2BreakKey.rt)
thisExp.nextEntry()
# the Routine "Block2Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Blocks10 = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Blocks10')
thisExp.addLoop(Blocks10)  # add the loop to the experiment
thisBlocks10 = Blocks10.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks10.rgb)
if thisBlocks10 != None:
    for paramName in thisBlocks10:
        exec('{} = thisBlocks10[paramName]'.format(paramName))

for thisBlocks10 in Blocks10:
    currentLoop = Blocks10
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks10.rgb)
    if thisBlocks10 != None:
        for paramName in thisBlocks10:
            exec('{} = thisBlocks10[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "EATaskInstructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Block1Counter
    block_counter += 1
    # keep track of which components have finished
    EATaskInstructionsComponents = [EATaskInstructionsText1, EATaskInstructionsText2]
    for thisComponent in EATaskInstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EATaskInstructions" ---
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *EATaskInstructionsText1* updates
        if EATaskInstructionsText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EATaskInstructionsText1.frameNStart = frameN  # exact frame index
            EATaskInstructionsText1.tStart = t  # local t and not account for scr refresh
            EATaskInstructionsText1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EATaskInstructionsText1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EATaskInstructionsText1.started')
            EATaskInstructionsText1.setAutoDraw(True)
        if EATaskInstructionsText1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EATaskInstructionsText1.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                EATaskInstructionsText1.tStop = t  # not accounting for scr refresh
                EATaskInstructionsText1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATaskInstructionsText1.stopped')
                EATaskInstructionsText1.setAutoDraw(False)
        
        # *EATaskInstructionsText2* updates
        if EATaskInstructionsText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EATaskInstructionsText2.frameNStart = frameN  # exact frame index
            EATaskInstructionsText2.tStart = t  # local t and not account for scr refresh
            EATaskInstructionsText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EATaskInstructionsText2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EATaskInstructionsText2.started')
            EATaskInstructionsText2.setAutoDraw(True)
        if EATaskInstructionsText2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EATaskInstructionsText2.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                EATaskInstructionsText2.tStop = t  # not accounting for scr refresh
                EATaskInstructionsText2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATaskInstructionsText2.stopped')
                EATaskInstructionsText2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EATaskInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EATaskInstructions" ---
    for thisComponent in EATaskInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # set up handler to look after randomisation of conditions etc
    EATrialsBlocks10 = data.TrialHandler(nReps=10.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='EATrialsBlocks10')
    thisExp.addLoop(EATrialsBlocks10)  # add the loop to the experiment
    thisEATrialsBlocks10 = EATrialsBlocks10.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEATrialsBlocks10.rgb)
    if thisEATrialsBlocks10 != None:
        for paramName in thisEATrialsBlocks10:
            exec('{} = thisEATrialsBlocks10[paramName]'.format(paramName))
    
    for thisEATrialsBlocks10 in EATrialsBlocks10:
        currentLoop = EATrialsBlocks10
        # abbreviate parameter names if possible (e.g. rgb = thisEATrialsBlocks10.rgb)
        if thisEATrialsBlocks10 != None:
            for paramName in thisEATrialsBlocks10:
                exec('{} = thisEATrialsBlocks10[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ISI" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [FixCross]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixCross* updates
            if FixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixCross.frameNStart = frameN  # exact frame index
                FixCross.tStart = t  # local t and not account for scr refresh
                FixCross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixCross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FixCross.started')
                FixCross.setAutoDraw(True)
            if FixCross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FixCross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    FixCross.tStop = t  # not accounting for scr refresh
                    FixCross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FixCross.stopped')
                    FixCross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI" ---
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "EATrial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from EATrialCode
        EA_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/ExAttn_stim/'
        EA_image_fp = os.path.join(EA_image_fp, ea_stim[shuffled_order[ea_stim_counter]])
        EA_corrkey = str(ea_stim_corr_keys[shuffled_order[ea_stim_counter]])
        thisExp.addData('corr_key', EA_corrkey)
        thisExp.addData('stim_name', ea_stim[shuffled_order[ea_stim_counter]])
        thisExp.addData('magnitude', ea_stim_magnitude[shuffled_order[ea_stim_counter]])
        thisExp.addData('stim_spec', ea_stim_spec[shuffled_order[ea_stim_counter]])
        thisExp.addData('num_big', ea_stim_big[shuffled_order[ea_stim_counter]])
        ea_stim_counter += 1
        EATrialText1.setText('big _ small')
        EATrialText2.setText('?     >     =     <')
        EATrialStim.setImage(EA_image_fp)
        EATrialResp.keys = []
        EATrialResp.rt = []
        _EATrialResp_allKeys = []
        # keep track of which components have finished
        EATrialComponents = [EATrialText1, EATrialText2, EATrialStim, EATrialResp]
        for thisComponent in EATrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "EATrial" ---
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *EATrialText1* updates
            if EATrialText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EATrialText1.frameNStart = frameN  # exact frame index
                EATrialText1.tStart = t  # local t and not account for scr refresh
                EATrialText1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EATrialText1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATrialText1.started')
                EATrialText1.setAutoDraw(True)
            if EATrialText1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EATrialText1.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    EATrialText1.tStop = t  # not accounting for scr refresh
                    EATrialText1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EATrialText1.stopped')
                    EATrialText1.setAutoDraw(False)
            
            # *EATrialText2* updates
            if EATrialText2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                EATrialText2.frameNStart = frameN  # exact frame index
                EATrialText2.tStart = t  # local t and not account for scr refresh
                EATrialText2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EATrialText2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATrialText2.started')
                EATrialText2.setAutoDraw(True)
            if EATrialText2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EATrialText2.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    EATrialText2.tStop = t  # not accounting for scr refresh
                    EATrialText2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EATrialText2.stopped')
                    EATrialText2.setAutoDraw(False)
            
            # *EATrialStim* updates
            if EATrialStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EATrialStim.frameNStart = frameN  # exact frame index
                EATrialStim.tStart = t  # local t and not account for scr refresh
                EATrialStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EATrialStim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATrialStim.started')
                EATrialStim.setAutoDraw(True)
            if EATrialStim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EATrialStim.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    EATrialStim.tStop = t  # not accounting for scr refresh
                    EATrialStim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EATrialStim.stopped')
                    EATrialStim.setAutoDraw(False)
            
            # *EATrialResp* updates
            waitOnFlip = False
            if EATrialResp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                EATrialResp.frameNStart = frameN  # exact frame index
                EATrialResp.tStart = t  # local t and not account for scr refresh
                EATrialResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EATrialResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EATrialResp.started')
                EATrialResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(EATrialResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(EATrialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if EATrialResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EATrialResp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    EATrialResp.tStop = t  # not accounting for scr refresh
                    EATrialResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EATrialResp.stopped')
                    EATrialResp.status = FINISHED
            if EATrialResp.status == STARTED and not waitOnFlip:
                theseKeys = EATrialResp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
                _EATrialResp_allKeys.extend(theseKeys)
                if len(_EATrialResp_allKeys):
                    EATrialResp.keys = _EATrialResp_allKeys[-1].name  # just the last key pressed
                    EATrialResp.rt = _EATrialResp_allKeys[-1].rt
                    # was this correct?
                    if (EATrialResp.keys == str(EA_corrkey)) or (EATrialResp.keys == EA_corrkey):
                        EATrialResp.corr = 1
                    else:
                        EATrialResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EATrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "EATrial" ---
        for thisComponent in EATrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if EATrialResp.keys in ['', [], None]:  # No response was made
            EATrialResp.keys = None
            # was no response the correct answer?!
            if str(EA_corrkey).lower() == 'none':
               EATrialResp.corr = 1;  # correct non-response
            else:
               EATrialResp.corr = 0;  # failed to respond (incorrectly)
        # store data for EATrialsBlocks10 (TrialHandler)
        EATrialsBlocks10.addData('EATrialResp.keys',EATrialResp.keys)
        EATrialsBlocks10.addData('EATrialResp.corr', EATrialResp.corr)
        if EATrialResp.keys != None:  # we had a response
            EATrialsBlocks10.addData('EATrialResp.rt', EATrialResp.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'EATrialsBlocks10'
    
    
    # --- Prepare to start Routine "EncTaskInstructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    EncTaskInstructionsText1.setText('Learning & Comparison Task')
    # keep track of which components have finished
    EncTaskInstructionsComponents = [EncTaskInstructionsText1, EncTaskInstructionsText2]
    for thisComponent in EncTaskInstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EncTaskInstructions" ---
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *EncTaskInstructionsText1* updates
        if EncTaskInstructionsText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EncTaskInstructionsText1.frameNStart = frameN  # exact frame index
            EncTaskInstructionsText1.tStart = t  # local t and not account for scr refresh
            EncTaskInstructionsText1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EncTaskInstructionsText1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EncTaskInstructionsText1.started')
            EncTaskInstructionsText1.setAutoDraw(True)
        if EncTaskInstructionsText1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EncTaskInstructionsText1.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                EncTaskInstructionsText1.tStop = t  # not accounting for scr refresh
                EncTaskInstructionsText1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EncTaskInstructionsText1.stopped')
                EncTaskInstructionsText1.setAutoDraw(False)
        
        # *EncTaskInstructionsText2* updates
        if EncTaskInstructionsText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EncTaskInstructionsText2.frameNStart = frameN  # exact frame index
            EncTaskInstructionsText2.tStart = t  # local t and not account for scr refresh
            EncTaskInstructionsText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EncTaskInstructionsText2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EncTaskInstructionsText2.started')
            EncTaskInstructionsText2.setAutoDraw(True)
        if EncTaskInstructionsText2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EncTaskInstructionsText2.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                EncTaskInstructionsText2.tStop = t  # not accounting for scr refresh
                EncTaskInstructionsText2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EncTaskInstructionsText2.stopped')
                EncTaskInstructionsText2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EncTaskInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EncTaskInstructions" ---
    for thisComponent in EncTaskInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # set up handler to look after randomisation of conditions etc
    EncTrialsBlocks10 = data.TrialHandler(nReps=10.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='EncTrialsBlocks10')
    thisExp.addLoop(EncTrialsBlocks10)  # add the loop to the experiment
    thisEncTrialsBlocks10 = EncTrialsBlocks10.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEncTrialsBlocks10.rgb)
    if thisEncTrialsBlocks10 != None:
        for paramName in thisEncTrialsBlocks10:
            exec('{} = thisEncTrialsBlocks10[paramName]'.format(paramName))
    
    for thisEncTrialsBlocks10 in EncTrialsBlocks10:
        currentLoop = EncTrialsBlocks10
        # abbreviate parameter names if possible (e.g. rgb = thisEncTrialsBlocks10.rgb)
        if thisEncTrialsBlocks10 != None:
            for paramName in thisEncTrialsBlocks10:
                exec('{} = thisEncTrialsBlocks10[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ISI" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [FixCross]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixCross* updates
            if FixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixCross.frameNStart = frameN  # exact frame index
                FixCross.tStart = t  # local t and not account for scr refresh
                FixCross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixCross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FixCross.started')
                FixCross.setAutoDraw(True)
            if FixCross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FixCross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    FixCross.tStop = t  # not accounting for scr refresh
                    FixCross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FixCross.stopped')
                    FixCross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI" ---
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "EncTrial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from EncTrialCode
        Enc_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Enc_stim/'
        Enc_image_fp = os.path.join(Enc_image_fp, enc_stim[shuffled_order[enc_stim_counter]])
        Enc_corrkey = str(enc_stim_corr_keys[shuffled_order[enc_stim_counter]])
        thisExp.addData('corr_key', Enc_corrkey)
        thisExp.addData('stim_name', enc_stim[shuffled_order[enc_stim_counter]])
        thisExp.addData('stim_spec', enc_stim_spec[shuffled_order[enc_stim_counter]])
        enc_stim_counter += 1
        EncImage.setImage(Enc_image_fp)
        EncTrialRespText.setText('?     >     =     <')
        EncTrialResp.keys = []
        EncTrialResp.rt = []
        _EncTrialResp_allKeys = []
        # keep track of which components have finished
        EncTrialComponents = [EncImage, EncTrialRespText, EncTrialResp]
        for thisComponent in EncTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "EncTrial" ---
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *EncImage* updates
            if EncImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EncImage.frameNStart = frameN  # exact frame index
                EncImage.tStart = t  # local t and not account for scr refresh
                EncImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EncImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EncImage.started')
                EncImage.setAutoDraw(True)
            if EncImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EncImage.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    EncImage.tStop = t  # not accounting for scr refresh
                    EncImage.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EncImage.stopped')
                    EncImage.setAutoDraw(False)
            
            # *EncTrialRespText* updates
            if EncTrialRespText.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                EncTrialRespText.frameNStart = frameN  # exact frame index
                EncTrialRespText.tStart = t  # local t and not account for scr refresh
                EncTrialRespText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EncTrialRespText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EncTrialRespText.started')
                EncTrialRespText.setAutoDraw(True)
            if EncTrialRespText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EncTrialRespText.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    EncTrialRespText.tStop = t  # not accounting for scr refresh
                    EncTrialRespText.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EncTrialRespText.stopped')
                    EncTrialRespText.setAutoDraw(False)
            
            # *EncTrialResp* updates
            waitOnFlip = False
            if EncTrialResp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                EncTrialResp.frameNStart = frameN  # exact frame index
                EncTrialResp.tStart = t  # local t and not account for scr refresh
                EncTrialResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EncTrialResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EncTrialResp.started')
                EncTrialResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(EncTrialResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(EncTrialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if EncTrialResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EncTrialResp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    EncTrialResp.tStop = t  # not accounting for scr refresh
                    EncTrialResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EncTrialResp.stopped')
                    EncTrialResp.status = FINISHED
            if EncTrialResp.status == STARTED and not waitOnFlip:
                theseKeys = EncTrialResp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
                _EncTrialResp_allKeys.extend(theseKeys)
                if len(_EncTrialResp_allKeys):
                    EncTrialResp.keys = _EncTrialResp_allKeys[-1].name  # just the last key pressed
                    EncTrialResp.rt = _EncTrialResp_allKeys[-1].rt
                    # was this correct?
                    if (EncTrialResp.keys == str(Enc_corrkey)) or (EncTrialResp.keys == Enc_corrkey):
                        EncTrialResp.corr = 1
                    else:
                        EncTrialResp.corr = 0
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EncTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "EncTrial" ---
        for thisComponent in EncTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if EncTrialResp.keys in ['', [], None]:  # No response was made
            EncTrialResp.keys = None
            # was no response the correct answer?!
            if str(Enc_corrkey).lower() == 'none':
               EncTrialResp.corr = 1;  # correct non-response
            else:
               EncTrialResp.corr = 0;  # failed to respond (incorrectly)
        # store data for EncTrialsBlocks10 (TrialHandler)
        EncTrialsBlocks10.addData('EncTrialResp.keys',EncTrialResp.keys)
        EncTrialsBlocks10.addData('EncTrialResp.corr', EncTrialResp.corr)
        if EncTrialResp.keys != None:  # we had a response
            EncTrialsBlocks10.addData('EncTrialResp.rt', EncTrialResp.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'EncTrialsBlocks10'
    
    
    # --- Prepare to start Routine "IATaskInstructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    IATaskInstructionsComponents = [IATaskInstructionsText1, IATaskInstructionsText2]
    for thisComponent in IATaskInstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "IATaskInstructions" ---
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IATaskInstructionsText1* updates
        if IATaskInstructionsText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IATaskInstructionsText1.frameNStart = frameN  # exact frame index
            IATaskInstructionsText1.tStart = t  # local t and not account for scr refresh
            IATaskInstructionsText1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IATaskInstructionsText1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IATaskInstructionsText1.started')
            IATaskInstructionsText1.setAutoDraw(True)
        if IATaskInstructionsText1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > IATaskInstructionsText1.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                IATaskInstructionsText1.tStop = t  # not accounting for scr refresh
                IATaskInstructionsText1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IATaskInstructionsText1.stopped')
                IATaskInstructionsText1.setAutoDraw(False)
        
        # *IATaskInstructionsText2* updates
        if IATaskInstructionsText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IATaskInstructionsText2.frameNStart = frameN  # exact frame index
            IATaskInstructionsText2.tStart = t  # local t and not account for scr refresh
            IATaskInstructionsText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IATaskInstructionsText2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IATaskInstructionsText2.started')
            IATaskInstructionsText2.setAutoDraw(True)
        if IATaskInstructionsText2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > IATaskInstructionsText2.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                IATaskInstructionsText2.tStop = t  # not accounting for scr refresh
                IATaskInstructionsText2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IATaskInstructionsText2.stopped')
                IATaskInstructionsText2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IATaskInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "IATaskInstructions" ---
    for thisComponent in IATaskInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # set up handler to look after randomisation of conditions etc
    IATrialsBlocks10 = data.TrialHandler(nReps=10.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='IATrialsBlocks10')
    thisExp.addLoop(IATrialsBlocks10)  # add the loop to the experiment
    thisIATrialsBlocks10 = IATrialsBlocks10.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisIATrialsBlocks10.rgb)
    if thisIATrialsBlocks10 != None:
        for paramName in thisIATrialsBlocks10:
            exec('{} = thisIATrialsBlocks10[paramName]'.format(paramName))
    
    for thisIATrialsBlocks10 in IATrialsBlocks10:
        currentLoop = IATrialsBlocks10
        # abbreviate parameter names if possible (e.g. rgb = thisIATrialsBlocks10.rgb)
        if thisIATrialsBlocks10 != None:
            for paramName in thisIATrialsBlocks10:
                exec('{} = thisIATrialsBlocks10[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ISI" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [FixCross]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixCross* updates
            if FixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixCross.frameNStart = frameN  # exact frame index
                FixCross.tStart = t  # local t and not account for scr refresh
                FixCross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixCross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FixCross.started')
                FixCross.setAutoDraw(True)
            if FixCross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FixCross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    FixCross.tStop = t  # not accounting for scr refresh
                    FixCross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FixCross.stopped')
                    FixCross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI" ---
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "IATrial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from IATrialCode
        IA_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/IntAttn_stim/'
        IA_image_fp = os.path.join(IA_image_fp, ia_stim[shuffled_order[ia_stim_counter]])
        IA_corrkey = str(ia_stim_corr_keys[shuffled_order[ia_stim_counter]])
        thisExp.addData('corr_key', IA_corrkey)
        thisExp.addData('stim_name', ia_stim[shuffled_order[ia_stim_counter]])
        thisExp.addData('magnitude', ia_stim_magnitude[shuffled_order[ia_stim_counter]])
        thisExp.addData('stim_spec', ia_stim_spec[shuffled_order[ia_stim_counter]])
        thisExp.addData('has_neg', ia_stim_hasneg[shuffled_order[ia_stim_counter]])
        ia_stim_counter += 1
        IATrialRespText.setText('?     >     =     <')
        IATrialStim.setImage(IA_image_fp)
        IATrialResp.keys = []
        IATrialResp.rt = []
        _IATrialResp_allKeys = []
        # keep track of which components have finished
        IATrialComponents = [IATrialRespText, IATrialStim, IATrialResp]
        for thisComponent in IATrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "IATrial" ---
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *IATrialRespText* updates
            if IATrialRespText.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                IATrialRespText.frameNStart = frameN  # exact frame index
                IATrialRespText.tStart = t  # local t and not account for scr refresh
                IATrialRespText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IATrialRespText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IATrialRespText.started')
                IATrialRespText.setAutoDraw(True)
            if IATrialRespText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > IATrialRespText.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    IATrialRespText.tStop = t  # not accounting for scr refresh
                    IATrialRespText.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'IATrialRespText.stopped')
                    IATrialRespText.setAutoDraw(False)
            
            # *IATrialStim* updates
            if IATrialStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                IATrialStim.frameNStart = frameN  # exact frame index
                IATrialStim.tStart = t  # local t and not account for scr refresh
                IATrialStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IATrialStim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IATrialStim.started')
                IATrialStim.setAutoDraw(True)
            if IATrialStim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > IATrialStim.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    IATrialStim.tStop = t  # not accounting for scr refresh
                    IATrialStim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'IATrialStim.stopped')
                    IATrialStim.setAutoDraw(False)
            
            # *IATrialResp* updates
            waitOnFlip = False
            if IATrialResp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                IATrialResp.frameNStart = frameN  # exact frame index
                IATrialResp.tStart = t  # local t and not account for scr refresh
                IATrialResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IATrialResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'IATrialResp.started')
                IATrialResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(IATrialResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(IATrialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if IATrialResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > IATrialResp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    IATrialResp.tStop = t  # not accounting for scr refresh
                    IATrialResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'IATrialResp.stopped')
                    IATrialResp.status = FINISHED
            if IATrialResp.status == STARTED and not waitOnFlip:
                theseKeys = IATrialResp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
                _IATrialResp_allKeys.extend(theseKeys)
                if len(_IATrialResp_allKeys):
                    IATrialResp.keys = _IATrialResp_allKeys[-1].name  # just the last key pressed
                    IATrialResp.rt = _IATrialResp_allKeys[-1].rt
                    # was this correct?
                    if (IATrialResp.keys == str(IA_corrkey)) or (IATrialResp.keys == IA_corrkey):
                        IATrialResp.corr = 1
                    else:
                        IATrialResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in IATrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "IATrial" ---
        for thisComponent in IATrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if IATrialResp.keys in ['', [], None]:  # No response was made
            IATrialResp.keys = None
            # was no response the correct answer?!
            if str(IA_corrkey).lower() == 'none':
               IATrialResp.corr = 1;  # correct non-response
            else:
               IATrialResp.corr = 0;  # failed to respond (incorrectly)
        # store data for IATrialsBlocks10 (TrialHandler)
        IATrialsBlocks10.addData('IATrialResp.keys',IATrialResp.keys)
        IATrialsBlocks10.addData('IATrialResp.corr', IATrialResp.corr)
        if IATrialResp.keys != None:  # we had a response
            IATrialsBlocks10.addData('IATrialResp.rt', IATrialResp.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'IATrialsBlocks10'
    
    
    # --- Prepare to start Routine "RetTaskInstructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    RetTaskInstructionsComponents = [RetTaskInstructionsText1, RetTaskInstructionsText2]
    for thisComponent in RetTaskInstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "RetTaskInstructions" ---
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *RetTaskInstructionsText1* updates
        if RetTaskInstructionsText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RetTaskInstructionsText1.frameNStart = frameN  # exact frame index
            RetTaskInstructionsText1.tStart = t  # local t and not account for scr refresh
            RetTaskInstructionsText1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RetTaskInstructionsText1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RetTaskInstructionsText1.started')
            RetTaskInstructionsText1.setAutoDraw(True)
        if RetTaskInstructionsText1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RetTaskInstructionsText1.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                RetTaskInstructionsText1.tStop = t  # not accounting for scr refresh
                RetTaskInstructionsText1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTaskInstructionsText1.stopped')
                RetTaskInstructionsText1.setAutoDraw(False)
        
        # *RetTaskInstructionsText2* updates
        if RetTaskInstructionsText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RetTaskInstructionsText2.frameNStart = frameN  # exact frame index
            RetTaskInstructionsText2.tStart = t  # local t and not account for scr refresh
            RetTaskInstructionsText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RetTaskInstructionsText2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RetTaskInstructionsText2.started')
            RetTaskInstructionsText2.setAutoDraw(True)
        if RetTaskInstructionsText2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RetTaskInstructionsText2.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                RetTaskInstructionsText2.tStop = t  # not accounting for scr refresh
                RetTaskInstructionsText2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTaskInstructionsText2.stopped')
                RetTaskInstructionsText2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RetTaskInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RetTaskInstructions" ---
    for thisComponent in RetTaskInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # set up handler to look after randomisation of conditions etc
    RetTrialsBlocks10 = data.TrialHandler(nReps=10.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='RetTrialsBlocks10')
    thisExp.addLoop(RetTrialsBlocks10)  # add the loop to the experiment
    thisRetTrialsBlocks10 = RetTrialsBlocks10.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRetTrialsBlocks10.rgb)
    if thisRetTrialsBlocks10 != None:
        for paramName in thisRetTrialsBlocks10:
            exec('{} = thisRetTrialsBlocks10[paramName]'.format(paramName))
    
    for thisRetTrialsBlocks10 in RetTrialsBlocks10:
        currentLoop = RetTrialsBlocks10
        # abbreviate parameter names if possible (e.g. rgb = thisRetTrialsBlocks10.rgb)
        if thisRetTrialsBlocks10 != None:
            for paramName in thisRetTrialsBlocks10:
                exec('{} = thisRetTrialsBlocks10[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ISI" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [FixCross]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ISI" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixCross* updates
            if FixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixCross.frameNStart = frameN  # exact frame index
                FixCross.tStart = t  # local t and not account for scr refresh
                FixCross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixCross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FixCross.started')
                FixCross.setAutoDraw(True)
            if FixCross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FixCross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    FixCross.tStop = t  # not accounting for scr refresh
                    FixCross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FixCross.stopped')
                    FixCross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ISI" ---
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "RetTrial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from RetTrialCode
        Ret_image_fp = '/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Ret_stim/'
        Ret_image_fp = os.path.join(Ret_image_fp, ret_stim[ret_shuffled_order[ret_stim_counter]])
        Ret_corrkey = str(ret_stim_corr_keys[ret_shuffled_order[ret_stim_counter]])
        thisExp.addData('corr_key', Ret_corrkey)
        thisExp.addData('stim_name', ret_stim[ret_shuffled_order[ret_stim_counter]])
        thisExp.addData('stim_spec', ret_stim_spec[ret_shuffled_order[ret_stim_counter]])
        thisExp.addData('enc_stimname', ret_enc_stimname[ret_shuffled_order[ret_stim_counter]])
        ret_stim_counter += 1
        RetTrialStim.setImage(Ret_image_fp)
        RetTrialResp.keys = []
        RetTrialResp.rt = []
        _RetTrialResp_allKeys = []
        RetTrialQuestion.setText('?')
        RetTrialBerry.setImage('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Repeating_Ret_Stim/fruit.jpeg')
        RetTrialTruck.setImage('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Repeating_Ret_Stim/vehicle.jpg')
        RetTrialHouse.setImage('/Users/matthewdougherty/Desktop/Projects/RetGoals_Git/Stimuli/Repeating_Ret_Stim/building.jpg')
        # keep track of which components have finished
        RetTrialComponents = [RetTrialStim, RetTrialResp, RetTrialQuestion, RetTrialBerry, RetTrialTruck, RetTrialHouse]
        for thisComponent in RetTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "RetTrial" ---
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *RetTrialStim* updates
            if RetTrialStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RetTrialStim.frameNStart = frameN  # exact frame index
                RetTrialStim.tStart = t  # local t and not account for scr refresh
                RetTrialStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RetTrialStim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialStim.started')
                RetTrialStim.setAutoDraw(True)
            if RetTrialStim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RetTrialStim.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    RetTrialStim.tStop = t  # not accounting for scr refresh
                    RetTrialStim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RetTrialStim.stopped')
                    RetTrialStim.setAutoDraw(False)
            
            # *RetTrialResp* updates
            waitOnFlip = False
            if RetTrialResp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                RetTrialResp.frameNStart = frameN  # exact frame index
                RetTrialResp.tStart = t  # local t and not account for scr refresh
                RetTrialResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RetTrialResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialResp.started')
                RetTrialResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(RetTrialResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(RetTrialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if RetTrialResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RetTrialResp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    RetTrialResp.tStop = t  # not accounting for scr refresh
                    RetTrialResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RetTrialResp.stopped')
                    RetTrialResp.status = FINISHED
            if RetTrialResp.status == STARTED and not waitOnFlip:
                theseKeys = RetTrialResp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
                _RetTrialResp_allKeys.extend(theseKeys)
                if len(_RetTrialResp_allKeys):
                    RetTrialResp.keys = _RetTrialResp_allKeys[-1].name  # just the last key pressed
                    RetTrialResp.rt = _RetTrialResp_allKeys[-1].rt
                    # was this correct?
                    if (RetTrialResp.keys == str(Ret_corrkey)) or (RetTrialResp.keys == Ret_corrkey):
                        RetTrialResp.corr = 1
                    else:
                        RetTrialResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *RetTrialQuestion* updates
            if RetTrialQuestion.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                RetTrialQuestion.frameNStart = frameN  # exact frame index
                RetTrialQuestion.tStart = t  # local t and not account for scr refresh
                RetTrialQuestion.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RetTrialQuestion, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialQuestion.started')
                RetTrialQuestion.setAutoDraw(True)
            if RetTrialQuestion.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RetTrialQuestion.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    RetTrialQuestion.tStop = t  # not accounting for scr refresh
                    RetTrialQuestion.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RetTrialQuestion.stopped')
                    RetTrialQuestion.setAutoDraw(False)
            
            # *RetTrialBerry* updates
            if RetTrialBerry.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                RetTrialBerry.frameNStart = frameN  # exact frame index
                RetTrialBerry.tStart = t  # local t and not account for scr refresh
                RetTrialBerry.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RetTrialBerry, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialBerry.started')
                RetTrialBerry.setAutoDraw(True)
            if RetTrialBerry.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RetTrialBerry.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    RetTrialBerry.tStop = t  # not accounting for scr refresh
                    RetTrialBerry.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RetTrialBerry.stopped')
                    RetTrialBerry.setAutoDraw(False)
            
            # *RetTrialTruck* updates
            if RetTrialTruck.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                RetTrialTruck.frameNStart = frameN  # exact frame index
                RetTrialTruck.tStart = t  # local t and not account for scr refresh
                RetTrialTruck.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RetTrialTruck, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialTruck.started')
                RetTrialTruck.setAutoDraw(True)
            if RetTrialTruck.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RetTrialTruck.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    RetTrialTruck.tStop = t  # not accounting for scr refresh
                    RetTrialTruck.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RetTrialTruck.stopped')
                    RetTrialTruck.setAutoDraw(False)
            
            # *RetTrialHouse* updates
            if RetTrialHouse.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                RetTrialHouse.frameNStart = frameN  # exact frame index
                RetTrialHouse.tStart = t  # local t and not account for scr refresh
                RetTrialHouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RetTrialHouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RetTrialHouse.started')
                RetTrialHouse.setAutoDraw(True)
            if RetTrialHouse.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RetTrialHouse.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    RetTrialHouse.tStop = t  # not accounting for scr refresh
                    RetTrialHouse.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RetTrialHouse.stopped')
                    RetTrialHouse.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RetTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "RetTrial" ---
        for thisComponent in RetTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if RetTrialResp.keys in ['', [], None]:  # No response was made
            RetTrialResp.keys = None
            # was no response the correct answer?!
            if str(Ret_corrkey).lower() == 'none':
               RetTrialResp.corr = 1;  # correct non-response
            else:
               RetTrialResp.corr = 0;  # failed to respond (incorrectly)
        # store data for RetTrialsBlocks10 (TrialHandler)
        RetTrialsBlocks10.addData('RetTrialResp.keys',RetTrialResp.keys)
        RetTrialsBlocks10.addData('RetTrialResp.corr', RetTrialResp.corr)
        if RetTrialResp.keys != None:  # we had a response
            RetTrialsBlocks10.addData('RetTrialResp.rt', RetTrialResp.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'RetTrialsBlocks10'
    
    
    # --- Prepare to start Routine "Block2End" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Block2EndCode
    if block_counter < 5:
        block2endtext = 'You have finished this block! You will now have a brief 30 second break before the beginning of the next one. Feel free to stretch out, but please do not use any technology or leave the testing room.'
    elif block_counter == 5:
        block2endtext = 'Congratulations! You have finished the experiment. Please let the experimenter know that you are finished. Thanks for participating!'
    Block2EndText.setText(block2endtext)
    # keep track of which components have finished
    Block2EndComponents = [Block2EndText]
    for thisComponent in Block2EndComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Block2End" ---
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Block2EndText* updates
        if Block2EndText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Block2EndText.frameNStart = frameN  # exact frame index
            Block2EndText.tStart = t  # local t and not account for scr refresh
            Block2EndText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Block2EndText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Block2EndText.started')
            Block2EndText.setAutoDraw(True)
        if Block2EndText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Block2EndText.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                Block2EndText.tStop = t  # not accounting for scr refresh
                Block2EndText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Block2EndText.stopped')
                Block2EndText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block2EndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Block2End" ---
    for thisComponent in Block2EndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
# completed 5.0 repeats of 'Blocks10'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

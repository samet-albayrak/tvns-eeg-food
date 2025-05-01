#ratings sequencer Gurme Beyin lab 
#Maria Veldhuizen
# elemenents of script from task programmed by Sophie Fromm

#V1.1 2021-05-18 Added additional choices in experiment info and incorporated into filename
# choices for dark and light color scheme
# condition
# experimenter initials
# these inputs are appended with right slugs, like pn-m for mersin studies etc


#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b11),
    on November 02, 2018, at 20:33
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division, print_function

import psychopy
#psychopy.useVersion('2020.2.6')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock, hardware, misc
from psychopy.hardware import keyboard
from psychopy import prefs
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

input_files=[]
#retrieve names of input files to be listed in the dropdown menu
for file in os.listdir(os.curdir):
    if file.endswith(".xlsx"):
        input_files.append(file)

# Store info about the experiment session
expName = 'WP1d_bilkent'  # from the Builder filename that created this script
myDlg = gui.Dlg(title='WP1d',size=(1, 1))
myDlg.addField('ParticipantNumber:','0001')#ok_data[0]
myDlg.addField('SubjectNumber:','01')#ok_data[1]
myDlg.addField('SessionNumber:','01')#ok_data[2]
myDlg.addField('Condition:',choices=["earlobe", "cymba conchae", "tragus","C+T"])#ok_data[3]
myDlg.addField('Responsemethod:', choices=["Mouse", "Buttons"])#ok_data[4]
myDlg.addField('Mode:', choices=["Dark","Light"])#ok_data[5]
myDlg.addField('Experimenter:', choices=["SA", "FY","...","MV"])#ok_data[6]
myDlg.addField('Inputfile:', choices=input_files)#use this if you have different csv files to choose from, entries should match csv names #ok_data[7]
ok_data = myDlg.show()
#print(ok_data)
#parse input filename
input_filename, input_file_extension = os.path.splitext(ok_data[7])
expInfo = {'ParticipantNumber': 'pn-b-%s' % ok_data[0], 'SubjectNumber': 'ss-%s' % (ok_data[1]),'SessionNumber': 'se-%s' %(ok_data[2]),'Condition': 'condition-%s' %(ok_data[3]),'InputFile': input_filename,'Experimenter':ok_data[6]}

#dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
#dlg.addField('Group:', choices=["Test", "Control"])
if myDlg.OK:  # or if ok_data is not None
    print(expInfo)
else:
    print('user cancelled')
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['experiment'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s_%s_%s_%s' % (expInfo['SubjectNumber'], expInfo['ParticipantNumber'], expInfo['SessionNumber'],expInfo['Condition'],expInfo['InputFile'],expName,  expInfo['date'])
print(filename)
print('Using %s (with %s) for sound' % (sound.audioLib, sound.audioDriver))
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=r'C:\Users\Dell01\Documents\ratings\WP1d', 
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

if ok_data[5] == 'Light':
    screen_color = 'AliceBlue'
    cust_text_color1 = 'MidnightBlue'#important labels
    cust_text_color2 = 'DarkGrey'#not so important labels
    cust_text_color3 = 'MidnightBlue'#for slider scale
    cust_text_color4 = 'Coral'#for bar on scale
    cust_text_color5 = 'DarkGrey'#for locked bar on scale
else:
    screen_color = 'Black'
    cust_text_color1 = 'AliceBlue'
    cust_text_color2 = 'Grey'
    cust_text_color3 = 'LightGrey'
    cust_text_color4 = 'Red'
    cust_text_color5 = 'LightBlue'#for locked bar on scale


# Start Code - component code to be run before the window creation
kb = keyboard.Keyboard()
# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=screen_color, colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

#This is a bar that is the assignes pointer of virtual mouses (so this mouse looks like a bar)
bar2 = visual.TextStim(win=win, text='|', units='norm', colorSpace='rgb', color=(cust_text_color4), height=.15)
bar3 = visual.TextStim(win=win, text='|', units='norm', colorSpace='rgb', color=(cust_text_color5), height=.15)

# Initialize components for Routine "instruction"
instrmouse= event.Mouse(visible=True) #this is the normal mouse set invisible
instructionClock = core.Clock()

if ok_data[4] == 'Buttons':
    inst_image = visual.ImageStim(win, image='instructions_scales_buttons.jpg',size=(0.6,0.8),pos=(0,-0.5))
    with open('instructions_buttons.txt') as f:
        init_instr_text= f.read()
else:
    inst_image = visual.ImageStim(win, image='instructions_scales_mouse.jpg',size=(0.6,0.8),pos=(0,-0.5))
    with open('instructions_mouse.txt',encoding=None) as f:
        init_instr_text= f.read()


    

text = visual.TextStim(win=win, name='text',
    text=init_instr_text,
    #text='Lutfen asagidaki degerlendirmeleri tamamlayin.\n\n Bir derecelendirme yapmak icin farenin sol dugmesiyle cizgiye tiklayin. Sol dugmeyle tekrar tiklarsaniz, yaptiginiz derecelendirmeyi gondereceksiniz.\n\n Bunun yerine sag dugmeyi tiklarsaniz derecelendirmeyi degistirebilirsiniz.\n\nBaslamak icin farenin sol dugmesine basin!',
    font='Tahoma',
    pos=(0, 0.5), height=0.06, wrapWidth=1.5, ori=0, 
    color=cust_text_color1, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
# color='MidnightBlue',
    
# Initialize components for Routine "trial"
nomouse= event.Mouse(visible=False)
trialClock = core.Clock()

# coordinates for labels in routine "Ratings" 
labels_range=range(0,9)
xco=[-.75,-.5,.75,0,-.85,0,.85,-.75,.75]
yco=[.75,.75,.75,.4,-.15,-.15,-.15,-.75,-.75]

text_labels = []

#to avoid new lines in the output file we have to use wrapWidth, but this changes for each label type, so we set those manually.
# wrapWidth for narrow labels is good at about .15 or .2, that is default above, for labels that can be wider we use manual changes
#wrapWidth=.15,
narrow_lables=[1,4,5,6]
for i in narrow_lables:
     #print(i)
     text_label_details= visual.TextStim(win=win, name="text_label_{}".format(i), text=None, 
                                 font='Tahoma', height=0.06,pos=[xco[i],yco[i]], wrapWidth=.2, ori=0, 
                                 color=cust_text_color1, colorSpace='rgb', opacity=1,languageStyle='LTR',
                                 depth=-1.0);
     text_labels.insert(i, text_label_details)

wide_labels=[0,2,7,8]
for i in wide_labels:
     #print(i)
     text_label_details= visual.TextStim(win=win, name="text_label_{}".format(i), text=None, 
                                 font='Tahoma', height=0.06,pos=[xco[i],yco[i]], wrapWidth=.35, ori=0, 
                                 color=cust_text_color1, colorSpace='rgb', opacity=1,languageStyle='LTR',
                                 depth=-1.0);
     text_labels.insert(i, text_label_details)

# we make an exception for text label 3, which will serve as a special instruction field for in between sections, which needs to be wider
text_label_details= visual.TextStim(win=win, name="text_label_{}".format(3), text=None, 
                                 font='Tahoma', height=0.08,pos=[xco[3],yco[3]], alignText = 'center',wrapWidth=.5, ori=0, 
                                 color=cust_text_color1, colorSpace='rgb', opacity=1,languageStyle='LTR',
                                 depth=-1.0);
text_labels.insert(3, text_label_details)

#change color of not so important labels
grey_labels=[0,1,2,7,8]
for i in grey_labels:
     text_labels[i].setColor(cust_text_color2)

#VASClock = core.Clock()
VAS_bipolarClock = core.Clock()
VAS_bipolar = visual.Slider(win=win, name='VAS_bipolar',
    size=(1.7, 0.1), pos=(0, 0),
    ticks=[-50, 0,50],
    granularity=0, style=('rating',), labelHeight=.05,
    color=cust_text_color3, font='Tahoma',
    autoLog = True, flip=False)

VAS_unipolarClock = core.Clock()

VAS_unipolar = visual.Slider(win=win, name='VAS_unipolar',
    size=(1.7, 0.1), pos=(0, 0),
    ticks=[-100, 100],
    granularity=0, style=('rating',), labelHeight=.05,
    color=cust_text_color3, font='Tahoma',
    autoLog = True, flip=False)

# this is a sounds that plays at the end of a autocontinue wait period, to alert the subject the experiment is continuing.
highA = sound.Sound('A', octave=3, sampleRate=44100, secs=0.8, stereo=True)
highA.setVolume(0.8)

    # Initialize components for Routine "Thank_you"
Thank_youClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Katildiginiz icin tesekkur ederiz.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=cust_text_color1, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
instructionComponents = [text, inst_image, instrmouse]
for thisComponent in instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction"-------

while continueRoutine:
    win.flip()
    instrmouse1, instrmouse2, instrmouse3 = instrmouse.getPressed()
    instrmouse.setVisible(0)
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
        inst_image.setAutoDraw(True)
# *nomouse* updates
    if t >= 0.0 and instrmouse.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrmouse.tStart = t
        instrmouse.frameNStart = frameN  # exact frame index
        instrmouse.status = STARTED
        prevButtonState = instrmouse.getPressed()  # if button is down already this ISN'T a new click
    if instrmouse.status == STARTED:  # only update if started and not stopped!
        buttons = instrmouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if instrmouse1:
                continueRoutine = False
    keys = kb.getKeys(keyList=['escape','1','2','3','4'], waitRelease=True)
    if keys:
        continueRoutine = False4
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#nomouseReset=True
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
core.wait(1,hogCPUperiod=10)# to wait for mouse button up so that the pointer of cursor is not locked.





# set up handler to look after randomisation of conditions etc
ratings = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(ok_data[7]),
    seed=None, name='ratings')
thisExp.addLoop(ratings)  # add the loop to the experiment
thisTrial = ratings.trialList[0]  # so we can initialise stimuli with some values

#event.clearEvents(eventType='mouse')
for thisTrial in ratings:
    nomouse.setVisible(0)
    currentLoop = ratings
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

# ------Prepare to start Routine "Hunger"-------
    #text_labels = labels
    #print(labels[i])
    t = 0
    pressed=0
    frameN = -1
    mouse_able = 1
    continueRoutine = True
    # update component parameters for each repeat      
    ratingsComponents = [nomouse,bar2,bar3]
    print(slider)
    if slider == 1:
        print('slider type1')
    #from the input file we now need to load the right elements, and leave out what we don't need, so it doesn't get drawn on screen
    #that means we will exclude the columns that have 'none' in them
    #text_lables[]
    kb.clock.reset
    if slider==1:#if we have a unipolar VAS, we need fewer elements
        VAS_unipolarClock.reset()
        VAS_RT0 = VAS_unipolarClock.getTime()
        VAS_unipolar.reset()
        ratingsComponents.append(VAS_unipolar)
        nomouse.setPos((-.85,1)) 
        #manchor='None'
    elif slider==2:
        VAS_bipolarClock.reset()
        VAS_RT0 = VAS_bipolarClock.getTime()
        VAS_bipolar.reset()
        ratingsComponents.append(VAS_bipolar)
        nomouse.setPos((0,1)) 
    
    for i in labels_range:
        if labels[i]=="None":
            text_labels[i].setText(text=None)
        else:
            text_labels[i].setText(labels[i])
            ratingsComponents.append(text_labels[i])
    if slider ==0:
        ratingsComponents = [nomouse,text_labels[3],text_labels[7]]
        bar2.setText(text=None)
        bar3.setText(text=None)
        nomouse.setPos((0,1)) 

    for thisComponent in ratingsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

        # -------Start Routine "Ratings"-------
    while continueRoutine:
        

        if mouse_able: 
            bar2_x = nomouse.getPos()[0]
        if bar2_x > .85:
            bar2_x = .85
        if bar2_x < -.85:
            bar2_x = -.85
        bar2.setPos((bar2_x, .02))
        mouse1, mouse2, mouse3 = nomouse.getPressed()
        keys = kb.getKeys(keyList=['escape','1','2','3','4'], waitRelease=True)
        if keys:
            mouse_able = 0#disable mouse
            if '1' in keys:
                print('1 pressed')
                kb.clock.getTime() 
                bar2_x = bar2_x-.01
                for key in keys:
                    kb.clock.getTime() 
                    if key.duration>.25:
                        bar2_x = bar2_x-(key.duration/2)#the longer the key is pressed, the more the bar moves
            if '2' in keys:
                print('2 pressed')
                kb.clock.getTime() 
                bar2_x = bar2_x+.01
                for key in keys:
                    kb.clock.getTime() 
                    if key.duration>.25:
                        bar2_x = bar2_x+(key.duration/2)#the longer the key is pressed, the more the bar moves
            if '3' in keys:
                print('3 pressed')
                mouse1=True
            if '4' in keys:
                print('4 pressed')
                mouse3=True
        # get current time
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame    
        if slider == 1:#if loop for uni vs bipolar VAS
            if t >= 0.0 and VAS_unipolar.status == NOT_STARTED:
            # keep track of start time/frame for later
                VAS_unipolar.tStart = t
                VAS_unipolar.frameNStart = frameN  # exact frame index
                VAS_unipolar.setAutoDraw(True)
        elif slider == 2: 
             if t >= 0.0 and VAS_bipolar.status == NOT_STARTED:
                VAS_bipolar.tStart = t
                VAS_bipolar.frameNStart = frameN
                VAS_bipolar.setAutoDraw(True)   

        #for i in select_labels_range:
        for i in labels_range:
                if t >= 0.0 and text_labels[i].status == NOT_STARTED:
                # keep track of start time/frame for later
                    text_labels[i].tStart = t
                    text_labels[i].frameNStart = frameN  # exact frame index
                    text_labels[i].setAutoDraw(True)
                
        # *bar2* updates
        if t >= 0.0 and bar2.status == NOT_STARTED:
            
        # keep track of start time/frame for later
            bar2.tStart = t
            bar2.frameNStart = frameN  # exact frame index
            bar2.setAutoDraw(True)


    # *nomouse* updates
        if t >= 0.0 and nomouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            nomouse.tStart = t
            nomouse.frameNStart = frameN  # exact frame index
            nomouse.status = STARTED
            prevButtonState = nomouse.getPressed()
            # if button is down already this ISN'T a new click
        if autocontinue == 1:      
            nomouse.status = STARTED
            mouse1 = True 
        if nomouse.status == STARTED:  # only update if started and not stopped!
            if mouse1:
                print('mouse1 condition met')
                nomouse.setExclusive(True)
                core.wait(.2)
                mouse1=0
                pressed=pressed+1
                if pressed == 1:
                    bar3.setPos((bar2_x, .02))
                    if slider > 0:
                        bar3.setAutoDraw(True)
                        bar2.setAutoDraw(False)
                        if slider == 1: #if loop for uni vs bipolar VAS
                            VAS_RT1 = VAS_unipolarClock.getTime()
                            VAS_RT1=round(VAS_RT1,3)
                        elif slider==2:
                            VAS_RT1 = VAS_bipolarClock.getTime()
                            VAS_RT1=round(VAS_RT1,3)
                    elif slider ==0:  
                        VAS_RT1 =0
                        if autocontinue !=1 and pressed ==1:    
                            print('click wait routine entered')
                            print(autocontinue)
                            bar3.setAutoDraw(False)
                            bar2.setAutoDraw(False)
                            nomouse.setExclusive(False)
                            nomouse.setVisible(0)
                            core.wait(.2,hogCPUperiod=10)
                            continueRoutine=False
                        else: 
                            bar3.setAutoDraw(False)
                            bar2.setAutoDraw(False)
                            nomouse.setExclusive(False)
                            nomouse.setVisible(0)
                            core.wait(.2,hogCPUperiod=10)
                    
                if pressed > 1:
                    print('second click')
                    nomouse.setExclusive(False)
                    nomouse.setVisible(0)
                    bar3.setAutoDraw(False)
                    continueRoutine=False
            elif mouse3:
                bar2.setPos((bar2_x, .02))
                bar2.setAutoDraw(True)
                bar3.setAutoDraw(False)
                nomouse.setExclusive(False)
                nomouse.setVisible(0)
                pressed=0
               # Check slider for response to end routine
        if slider == 1:
            if VAS_unipolar.getRating() is not None and VAS_unipolar.status == STARTED:
                continueRoutine = False
        elif slider == 2:
            if VAS_bipolar.getRating() is not None and VAS_bipolar.status == STARTED:
                continueRoutine = False
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ratingsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()


#the onscreen scale is 1.7 units. 
#for unipolar scales, we will transform to a value between 0 and 100 with the formula: ((bar3.pos[0]+0.85)/1.7)*100
#for bipolar scales, we will transform to a value between -50 and +50 with the formula: (bar3.pos[0]/(0.85/0.5))*100
    # -------Ending Routine "Picture"------- change to only save the relevant parts
    for thisComponent in ratingsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if slider >=1:
        ratings.addData("Rating_raw", bar3.pos[0])
        if slider == 1:#if loop for uni vs bipolar VAS
            transformed_rating = round((((bar3.pos[0]+0.85)/1.7)*100), 2)
            ratings.addData("Rating_trans", transformed_rating)
        elif slider == 2:
            transformed_rating = round(((bar3.pos[0]/(0.85/0.5))*100),2)
            ratings.addData("Rating_trans", transformed_rating)
        #ratings.addData("Rating_RT0", VAS_RT0)
        ratings.addData("Rating_RT1", VAS_RT1)
        #ratings.addData("Rating_RT2", VAS_RT2)

    highA = sound.Sound('A', octave=3, sampleRate=44100, secs=0.8, stereo=True)#reset sound (bug)
    highA.setVolume(0.8)

    # the Routine "Picture" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    if autocontinue !=1:
        win.flip()
    #if loop to evaluate if there is wait indicated in the excel file
    #draw label to show wait period
    if autocontinue != 1:
        core.wait(ISI,hogCPUperiod=10)
    else:
        core.wait(ISI-1,hogCPUperiod=10)
        highA.play()
        core.wait(1)
    thisExp.nextEntry()

        
    # ------Prepare to start Routine "Thank_you"-------
t = 0
Thank_youClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Thank_youComponents = [text_4]
for thisComponent in Thank_youComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Thank_you"-------
while continueRoutine:
    # get current time
    t = Thank_youClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Thank_youComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thank_you"-------
for thisComponent in Thank_youComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Thank_you" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# check for quit (the Esc key)
if endExpNow or event.getKeys(keyList=["escape"]):
    core.quit()

# these shouldn't be strictly necessary (should auto-save)
#thisExp.saveAsWideText(filename+'.csv')
#thisExp.saveAsPickle(filename)
#logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()






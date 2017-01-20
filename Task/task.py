##########################
# Task for "The Value of Sharing Information: A Neural Account of Information Transmission"
##########################

##########################
#   4 conditions (20 trials each)
#   --------------
#   1. Facebook Wall (broadcast)
#   2. Message a Friend (narrowcast)
#   3. Save to Read Later (control)
#   4. Content (control)

# Press 't' at the "Ready" screen to begin task
# (this can be changed depending on scanner trigger setup)

# Import PsychoPy
from psychopy import visual, core, event, data, gui, logging, sound

# Import modules
import os
import sys
import random
import csv
import datetime


##########################
# Set up
##########################

subj_id='subj1'
specific_run = None

# Log files (.csv - spreadsheet and .log - longform)

### Get csv logfile name - will be fed with information from the trial handler
log_filename= 'logs/%s.csv' %subj_id
run_data={
    'Participant ID': subj_id,
    'Date': str(datetime.datetime.now()),
    'Description': 'Task'
}

### Set up .log file - mostly automatic (PsychoPy default)

expdir = os.getcwd()
logdir = '%s/logs' % (expdir)
#print logdir

log_file = logging.LogFile("logs/%s.log" % (subj_id),  level=logging.DATA, filemode="w")
globalClock = core.Clock()
logging.setDefaultClock(globalClock)

# Study Parameters

## Make a condition indicator and randomize it
#### Set up for: 80 Trials

## Read friend names for share with friend condition_headline
friends = [ i for i in csv.DictReader(open('friends/friends_%s.csv' % (subj_id),'rU'))]
friends = [ f['name'] for f in friends]

# load trial stimuli
stimuli_run1 = [ row for row in csv.DictReader(open('stimuli/%s_run1.csv' % (subj_id), 'rU'))] 
stimuli_run2 = [ row for row in csv.DictReader(open('stimuli/%s_run2.csv' % (subj_id), 'rU'))]

## set up trial handler
#### dataTypes are going to be columns in the .csv logfile
trials_run1 = data.TrialHandler(stimuli_run1, nReps=1, dataTypes=['clue_onset','read_onset', 'within_fixation','rate_onset','rt','button','between_fixation'],method='sequential')
trials_run2 = data.TrialHandler(stimuli_run2, nReps=1, dataTypes=['clue_onset','read_onset', 'within_fixation','rate_onset','rt','button','between_fixation'],method='sequential')

## Jitter: Optseq generates optimal jitter times and trial order

between_jitter_dist_run1=[1.7, 1.1, 1, 3.6, 1, 3.5, 1.1, 2.3, 1.6, 1.8, 3.8, 2.5, 1, 1.4, 1.1, 1.1, 1, 1.5, 1.5, 1.2, 3.3, 1, 2.5, 2.5, 2.4, 1.3, 1.4, 1.9, 3.4, 1.1, 4.199, 1.2, 2.7, 2.5, 3.199, 1.1, 2.1, 1, 2.9, 4.502]
between_jitter_dist_run2=[2.3, 2.4, 4.7, 3.1, 2.1, 2, 1, 2.7, 1, 1.2, 1.2, 2.6, 3.4, 1, 2.1, 1.9, 2.5, 3.1, 4, 2.2, 1.9, 2.4, 1.3, 1.7, 1.7, 1.1, 1.1, 3, 1.2, 1.6, 1.2, 1.9, 1.6, 2, 1.4, 1.2, 1, 3.699, 1.2, 2.3]
within_jitter_dist_run1=[0.7, 0.9, 2, 1.4, 1.6, 1.7, 1.8, 2.3, 0.5, 1.1, 0.6, 1, 1.1, 1.3, 2.3, 0.6, 2.4, 0.5, 0.7, 0.7, 0.5, 4.3, 1.6, 0.9, 0.8, 0.5, 2, 4.7, 2.8, 2.5, 0.5, 2.1, 0.9, 1.2, 2.599, 3.499, 1.1, 0.6, 0.5, 1.2]
within_jitter_dist_run2=[2.2, 2, 1.7, 1.1, 2.9, 2.6, 1, 0.7, 1.7, 0.6, 0.5, 2.6, 0.7, 0.7, 1.2, 1.1, 2.6, 0.5, 2.1, 1.4, 1, 0.6, 1.6, 2.6, 0.8, 1.3, 0.6, 0.7, 1.3, 2.2, 0.8, 0.8, 2.699, 1.1, 0.9, 0.8, 2.699, 4.499, 0.8, 2.301]

for i in [within_jitter_dist_run1, within_jitter_dist_run2, between_jitter_dist_run1, between_jitter_dist_run2]:
    random.shuffle(i)


# Set up Window and Instructions

### False for testing purposes
useFullScreen=False
win = visual.Window([800,600], monitor="testMonitor", units="deg", fullscr=useFullScreen, allowGUI=False)

### Ready and Fixation screens

fixation = visual.TextStim(win, text="+", height=2, color="#FFFFFF")
ready_screen = visual.TextStim(win, text="Ready.....", height=1.5, color="#FFFFFF")

### Pre-trial phase instructions
instruct_screen = visual.TextStim(win,text='Decide whether \n\n- to Share on Wall \n\n- to Share with Friend \n\n- to Read Yourself, or \n\n- whether the Topic is X', pos=(0,1), wrapWidth=20, color='#FFFFFF', height=1.2)

responsebox_screen = visual.ImageStim(win,image="responsebox.png",pos=(-1,-3.5),size=(10,8))
responsebox_screen_text = visual.TextStim(win, height=1.2,color="#FFFFFF", text="Use these 5 buttons to answer. \n\nThumb = 1\nPinky = 5", pos=(0,+5), wrapWidth=20)

### Clue screen (only if task includes a clue about who the next article is supposed to be shared with BEFORE the article is presented)

clue_screen= visual.TextStim(win,text="", wrapWidth=30,height=1.5)

### Reading screen

headline_read=visual.TextStim(win, text="",pos=(0,4),height=1.2, bold=True, wrapWidth=20)
abstract=visual.TextStim(win,text="",pos=(0,-2),height=1.2,  wrapWidth=20)
cond_info=visual.TextStim(win, text="", pos=(0,7), height=1, wrapWidth=20)
rec_cond_info=visual.Rect(win, width=21, height=1.5, lineWidth=2, pos=(0,7)) 

### Rating screen

CondText=['Share: %s','Share: Wall','Read: Yourself', 'Topic: %s']
condition_headline = visual.TextStim(win, text='', pos=(0,3), color="#FFFFFF", colorSpace=(0,0,0), height=2, wrapWidth=20)
button_labels = { '1': 0, '2': 1, '3': 2, '4': 3, '5': 4 }

##### .keys gives you the first element of a pair in a dictionairy (the second is called value) - so button_labels.keys()
buttons = button_labels.keys()

anchor1 = visual.TextStim(win, text='', pos=(-8,-2), height=1)
anchor5 = visual.TextStim(win, text='', pos=(8,-2), height=1)

ratingStim=[]

xpos = [-8, -4, 0, 4, 8]

for rating in (1,2,3,4,5):
    ratingStim.append(visual.TextStim(win, text='%i' % rating, pos=(xpos[rating-1],-4.2), height=1))



##########################
# Define Function to run trials for each run
##########################



def do_run(run,trials):
    
    # Present ready screen
    
    ready_screen.draw()
    win.flip()
    logging.log(level=logging.DATA, msg="** START RUN %i **" % (run+1) ) 

    ### wait for trigger from scanner (t key press)
    event.waitKeys(keyList=('t'))
    logging.log(level=logging.DATA, msg="** TRIGGER RECEIVED for Run %i **" % (run+1))
    
    ### Reset global clock for beginning of task
    globalClock.reset()
    
    # Present instructions
    
    ### Instructions
    curTime=globalClock.getTime()
    startTime=curTime
    while curTime<(startTime+6.0):
        instruct_screen.draw()
        win.flip()
        curTime=globalClock.getTime()

    ### Responsebox
    curTime=globalClock.getTime()
    startTime=curTime
    while curTime < (startTime+6.0):
        responsebox_screen.draw()
        responsebox_screen_text.draw()
        win.flip()
        curTime=globalClock.getTime()
    
    if run==0:
        ### Set fixidx to start from beginning of list at first trial
        within_jitter_dist=within_jitter_dist_run1
        within_fixidx = -1
        between_jitter_dist=between_jitter_dist_run1
        between_fixidx = -1

    if run==1:
        within_jitter_dist=within_jitter_dist_run2
        within_fixidx = -1
        between_jitter_dist=between_jitter_dist_run2
        between_fixidx = -1
   
   #Loop through trials
    
    for idx, trial in enumerate(trials):
        
        within_fixidx = within_fixidx + 1
        between_fixidx = between_fixidx + 1
        
        ### Log run number in .csv file
        trials.addData('run', run+1)
        
        #print trial['cond'].encode('utf-8')
        
        # Present Stimuli
        
 
        
        ## Reset rating scale color
        
        for rate in ratingStim:
            rate.setColor('#FFFFFF')
        
        ### Send new trial message to .log file 
        logging.log(level=logging.DATA, msg="Trial Onset: Article Nr. %s, Headline: %s, Abstract: %s condition %s" %(trial['id'],trial['headline'],trial['abstract'],trial['cond']))
        
        ###Clue screen
        if trial['cond']=='Friend':
            friend = random.choice(friends)
            clue_screen.setText(CondText[0] % friend)
        if trial['cond']=='Wall':
            clue_screen.setText(CondText[1])
        if trial['cond']=='Read':
            clue_screen.setText(CondText[2])
        if trial['cond']=='Content':
            clue_screen.setText(CondText[3] % trial['content'])
        
        ##### log clue screen onset
        trials.addData('clue_onset', globalClock.getTime())
        logging.log(level=logging.DATA, msg="Clue Onset")

        curTime=globalClock.getTime()
        startTime=curTime
        while curTime < (1.5+startTime):
            clue_screen.draw()
            win.flip()
            curTime=globalClock.getTime()
        
        ###Reading Screen
        
        ##### Set screen texts for trial
        headline_read.setText(trial['headline'])
        abstract.setText(trial['abstract'])
        if trial['cond']=='Friend':
            cond_info.setText(CondText[0] % friend + '?')
        if trial['cond']=='Wall':
            cond_info.setText(CondText[1]+'?')
        if trial['cond']=='Read':
            cond_info.setText(CondText[2]+'?')
        if trial['cond']=='Content':
            cond_info.setText(CondText[3] % (trial['content'])+'?')
            
        ##### Set audio for trial
        audio="audio/%s.wav" % (trial['id'])
        article_audio = sound.Sound(audio)
        
        #####Log reading screen onset
        trials.addData('read_onset',globalClock.getTime())
        logging.log(level=logging.DATA,msg='Read Onset')
        
        curTime=globalClock.getTime()
        startTime=curTime
        
        #####Set trial length
        
        cur_trial_len=int(trial['time'])
        
        #####Play audio
        
        article_audio.play()
        
        #####Present visual stim
                        
        while curTime < (startTime+cur_trial_len):
            headline_read.draw()
            abstract.draw()
            cond_info.draw()
            rec_cond_info.draw()
            win.flip()
            curTime=globalClock.getTime()
        
        ###Within Trial fixation
        within_fixdur=within_jitter_dist[within_fixidx]
        
        ##### Log within-trial fixation
        logging.log(level=logging.DATA,msg='Within fixation')
        trials.addData('within_fixation',globalClock.getTime())
        curTime=globalClock.getTime()
        startTime=curTime
        
        while curTime<(startTime+within_fixdur):
            fixation.draw()
            win.flip()
            curTime=globalClock.getTime()
        
        ###Rating Screen
        

        
        
        if trial['cond']=='Friend':
            condition_headline.setText(CondText[0] % friend+'?')
            anchor1.setText('Very\nUnlikely')
            anchor5.setText('Very\nLikely')
        if trial['cond']=='Wall':
            condition_headline.setText(CondText[1]+'?')
            anchor1.setText('Very\nUnlikely')
            anchor5.setText('Very\nLikely')
        if trial['cond']=='Read':
            condition_headline.setText(CondText[2]+'?')
            anchor1.setText('Very\nUnlikely')
            anchor5.setText('Very\nLikely')
        if trial['cond']=='Content':
            condition_headline.setText(CondText[3] % (trial['content'])+'?')
            anchor1.setText('Certainly\nNot')
            anchor5.setText('Certainly\nYes')
            
        ##### Log onset of rating screen
        logging.log(level=logging.DATA,msg='Rate onset')
        trials.addData('rate_onset',globalClock.getTime())
        
        ## Clear Stuff from previous trial and set up for new one
                
        event.clearEvents()
        keypress = None
        rt = None
        
        
        curTime=globalClock.getTime()
        startTime=curTime
        
        while curTime < (3.0+startTime):
            condition_headline.draw()
            anchor1.draw()
            anchor5.draw()
            for resp in ratingStim:
                resp.draw()
            win.flip()
            curTime=globalClock.getTime()
            
            resp = event.getKeys(keyList = buttons)
                            
            if keypress==True:
                pass
            else:
                if len(resp) > 0 : 
                    resp_value = button_labels[resp[0]]
                    ratingStim[resp_value].setColor('red')
                    trials.addData('button', resp_value+1)
                    trials.addData('rt', globalClock.getTime())
                    logging.log(level=logging.DATA,msg='button press: %s' % (resp_value+1))
                    keypress=True
            
           
        ### Between trial fixation 
        between_fixdur=between_jitter_dist[between_fixidx]
        
        ##### Log between-trial fixation
        logging.log(level=logging.DATA, msg='Between_FIXATION')
        trials.addData('between_fixation', globalClock.getTime())
        curTime=globalClock.getTime()
        startTime=curTime
        
        while curTime < (startTime+between_fixdur):
            fixation.draw()
            win.flip()
            curTime=globalClock.getTime()
         
    # save information from trial handler in .csv log file
    trials.saveAsText(log_filename, delim=",",appendFile=True, dataOut=('n','all_raw'))
    
    trials.saveAsText(log_filename.replace('.csv','_run%i.csv' % (run +1)), delim=",",appendFile=True, dataOut=('n','all_raw'))

    
    # send end log event for Run
    logging.log(level=logging.DATA,msg='*****END RUN %i*****' % (run+1))
        
    # After run fixation - wait for space key
    fixation.draw()
    win.flip()
    event.waitKeys(keyList=('space'))

##################### 
# DO RUNS
####################

### 
#Logging
###

log_file = logging.LogFile("logs/%s.log" % (subj_id),  level=logging.DATA, filemode="w")

globalClock = core.Clock()
logging.setDefaultClock(globalClock)

#####
# just do specific run
if specific_run is not None:
    if specific_run == 1:
        do_run(0, trials_run1)
    elif specific_run == 2:
        do_run(1, trials_run2)
else:
    for run_idx, trials in enumerate([trials_run1,trials_run2]):
        do_run(run_idx, trials)




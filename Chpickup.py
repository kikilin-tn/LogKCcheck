"""
import re
LogMessage = re.compile(r'\w\w\d:\w\w\w\w=\d') #找event[4]
message = 'OK CH1:Line=2'
mo = LogMessage.search(message)
#print(mo.group())
search_id = mo.group()
print(search_id)
"""

import re

logs = []
new_log = []
KC_log = []
cnt = 0
event_beam_width = 0

with open('LG06_0520.txt','r') as f:
    for line in f:
        event=re.split('\t|,|\n',line)
        #print(event)

        if len(event) < 5:
            continue
        event_time = event[0]
        event_id = event[1]
        message = event[3]
        #evnet_beam_width = line[5]
        #print('beam width= ' + evnet_beam_width)
        #print('msg= ' + message)
        #LogMessage = re.compile(r'\w\w\d:\w\w\w\w=\d') #CH2:Line=20
        if event_id == 'KC':
            #print('test' + event[5])
            #print('beam width= ' + evnet_beam_width)
            LogMessage = re.compile(r'\w\w\d:\w\w\w\w=\d*') #CH2:Line=20
            #LogMessage = re.compile(r'.\w\w\d') #CH2
            mo = LogMessage.search(message)
            msg = mo.group()

            LogMessage_ch = re.compile(r'.\w\w\d') #CH2
            mo_ch = LogMessage.search(message)
            msg_ch = mo_ch.group()
            #print(event_time +' '+ msg+' '+event[5])
            #print('test' + event[5])

            print('all ch=' +''+ msg)
            print('ch=' +''+ msg_ch)

        #if event_id == 'PRO' or event_id == 'KC': #or event_id == 'CUT':
            #logs.append(event[0:7])
    #print(logs)

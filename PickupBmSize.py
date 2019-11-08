import re
import time

log_lines = []
filename = input('please input the file name:(ex.LG07_0520.txt)\n')
#time.sleep(30)
with open(filename,'r') as f:
    for line in f:
        event=re.split(',|\t|\n',line)

        if len(event) < 5:
            continue
        event_id = event[1]

        if event_id == 'PRO' or event_id == 'KC':
            log_lines.append(event[0:7])

new_lines = log_lines[::-1]

cnt1 = 0
ch1w1 = []
ch1w2 = []
ch1time = []
ch1w1lines = []
ch1w2lines = []

cnt2 = 0
ch2w1 = []
ch2w2 = []
ch2time = []
ch2w1lines = []
ch2w2lines = []

err1 = []
err2 = []

for line in new_lines:
    if line[1] == 'PRO':

        cnt1 = 0
        ch1w1 = []
        ch1w2 = []
        ch1time = []
        ch1w1lines = []
        ch1w2lines = []
        err1 = []

        cnt2 = 0
        ch2w1 = []
        ch2w2 = []
        ch2time = []
        ch2w1lines = []
        ch2w2lines = []
        err2 = []
        pro_id = line[0] + ' ' + line[3]

    elif line[1] == 'KC'and 'CH1' in line[3]:
        if 'NG' in line[3]:
            print('NG line is happened in ' + line[0] +' '+ line[3][7:]) #to judge NG happen in KC
            err1.append(line[3][7:] + ',')
        cnt1 += 1
        width = line[5]+','
        #w1time = line[0]+','
        w1line = line[3][12:]+','
        if cnt1 % 2 == 1:
            ch1time.append(line[0] + ',')
            ch1w1.append(width)
            ch1w1lines.append(w1line)
        elif cnt1 % 2 == 0:
            ch1w2.append(width)
            ch1w2lines.append(w1line)

    elif line[1] == 'KC'and 'CH2' in line[3]:
        if 'NG' in line[3]:
            print('NG line is happened in ' +line[0] +' '+ line[3][7:]) #ex, show Line=65
            err2.append(line[3][7:] + ',')
        cnt2 += 1
        width2 = line[5] + ','  #beam width
        w2line = line[3][12:] + ',' #cut line
        if cnt2 % 2 == 1:
            #ch2time.append(w2time)
            ch2time.append(line[0] + ',')
            ch2w1.append(width2)
            ch2w1lines.append(w2line)
        elif cnt2 % 2 == 0:
            ch2w2.append(width2)
            ch2w2lines.append(w2line)

    fout = open('beam_width_result.csv', 'a')

    fout.writelines('Product ID:,')
    fout.writelines(pro_id)
    fout.writelines('\n')
    fout.writelines('CH1 KC Time:,')
    fout.writelines(ch1time)
    fout.writelines('\n')
    fout.writelines('CH1 beam1 width:,')
    fout.writelines(ch1w1)
    fout.writelines('\n')
    fout.writelines('CH1 beam2 width:,')
    fout.writelines(ch1w2)
    fout.writelines('\n')
    fout.writelines('CH1 beam1 line:,')
    fout.writelines(ch1w1lines)
    fout.writelines('\n')
    fout.writelines('CH1 beam2 line:,')
    fout.writelines(ch1w2lines)
    fout.writelines('\n')
    fout.writelines('KC error:,')
    fout.writelines(err1)
    fout.writelines('\n')

    fout.writelines('CH2 KC Time:,')
    fout.writelines(ch2time)
    fout.writelines('\n')
    fout.writelines('CH2 beam1 width:,')
    fout.writelines(ch2w1)
    fout.writelines('\n')
    fout.writelines('CH2 beam2 width:,')
    fout.writelines(ch2w2)
    fout.writelines('\n')
    fout.writelines('Ch2 beam1 line:,')
    fout.writelines(ch2w1lines)
    fout.writelines('\n')
    fout.writelines('CH2 beam2 line:,')
    fout.writelines(ch2w2lines)
    fout.writelines('\n')
    fout.writelines('KC error:,')
    fout.writelines(err2)
    fout.writelines('\n')
    fout.writelines('\n')
    # fout.writelines('Product ID:,')
    # fout.writelines(line[0] + ' ' + line[3])
    # fout.writelines('\n')
    fout.close( )

print('file is output to the file: "beam_width_result.csv", please check it.')
time.sleep(3)

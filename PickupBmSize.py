import re

log_lines = []
new_lines = []

pro = 0
cnt1 = 0
ch1w1 = []
ch1w2 = []
ch1time = []
output = []
cntw2 = 0
filename = input('please input the file name:(ex.LG07_0520.txt)\n')
with open(filename,'r') as f:
    for line in f:
        event=re.split(',|\t|\n',line)

        if len(event) < 5:
            continue
        event_id = event[1]

        if event_id == 'PRO' or event_id == 'KC':
            log_lines.append(event[0:7])

    new_lines = log_lines[::-1]
    #print(new_lines)

    for line in new_lines:
        if line[1] == 'PRO':
            #if len(ch1time) <2:
                #continue
            #else:
            #print(ch1time)
            #print(ch1w1)
            #print(ch1w2)

            with open('beam width result.txt', 'a') as f:
                f.writelines('KC Time:, ')
                f.writelines(ch1time)
                f.writelines('\n')
                f.writelines('Width1:, ')
                f.writelines(ch1w1)
                f.writelines('\n')
                f.writelines('Width2:, ')
                f.writelines(ch1w2)
                f.writelines('\n')
                #f.writelines('--------------------------------')
                f.writelines('\n')
                f.writelines('Product ID:, ')
                f.writelines(line[0] + ' ' + line[3])
                f.writelines('\n')

            ch1w1 = []
            ch1w2 = []
            ch1time = []

        elif line[1] == 'KC'and 'CH1' in line[3]:
            cnt1 += 1
            width1 = line[5]+','
            w1time = line[0]+','
            if cnt1 % 2 == 1:
                ch1time.append(w1time)
                ch1w1.append(width1)
            elif cnt1 % 2 == 0:
                ch1w2.append(width1)
#-------------------------------------------------------------------------
# with open('Test_LOG.txt','r') as f:
#     for line in f:
#         event=re.split(',|\t|\n',line)
#
#         if event[1] == 'PRO':
#             #if len(ch1time) <2:
#                 #continue
#             #else:
#             print(ch1time)
#             print(ch1w1)
#             print(ch1w2)
#
#             with open('beam width result.txt', 'a') as f:
#                 f.writelines(ch1time)
#                 f.writelines('\n')
#                 f.writelines(ch1w1)
#                 f.writelines('\n')
#                 f.writelines(ch1w2)
#                 f.writelines('\n')
#                 f.writelines('--------------------------------')
#                 f.writelines('\n')
#                 f.writelines(event[3])
#
#             ch1w1 = []
#             ch1w2 = []
#             ch1time = []
#             #print(ch1)
#             #print('\n' + event[0] + ' ' + event[3]) #time and product name
#
#         elif event[1] == 'KC'and 'CH1' in event[3]:
#             cnt1 += 1
#             width1 = event[5]+','
#             w1time = event[0]+','
#             if cnt1 % 2 == 1:
#                 #output.append(w1time)
#                 ch1time.append(w1time)
#                 ch1w1.append(width1)
#             elif cnt1 % 2 == 0:
#                 #output.append(width1)
#                 ch1w2.append(width1)

        # elif event[1] == 'KC'and 'CH2' in event[3]:
        #     width2 = event[5]
        #     ch2.append(width2)

        # elif event[1] == 'KC'and 'CH2' in event[3]:
        #     ch2width = event[5]

    #print(event)
    #print(KClist1)
        #KClist1.append(ch1width)
# with open('beam_width_result.txt', 'w') as fout:
#     fout.readlines(ch1time)
#     fout.readlines(ch1w1)

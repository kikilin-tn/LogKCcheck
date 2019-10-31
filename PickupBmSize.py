import re

log_lines = []
new_lines = []

cnt1 = 0
ch1w1 = []
ch1w2 = []
ch1time = []

cnt2 = 0
ch2w1 = []
ch2w2 = []
ch2time = []

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

    for line in new_lines:
        if line[1] == 'PRO':
            with open('beam_width_result.txt', 'a') as f:
                f.writelines('CH1 KC Time:, ')
                f.writelines(ch1time)
                f.writelines('\n')
                f.writelines('CH1 width1:, ')
                f.writelines(ch1w1)
                f.writelines('\n')
                f.writelines('CH1 Width2:, ')
                f.writelines(ch1w2)
                f.writelines('\n')

                f.writelines('CH2 KC Time:, ')
                f.writelines(ch2time)
                f.writelines('\n')
                f.writelines('CH2 width1:, ')
                f.writelines(ch2w1)
                f.writelines('\n')
                f.writelines('CH2 Width2:, ')
                f.writelines(ch2w2)
                f.writelines('\n')
                #f.writelines('--------------------------------')
                f.writelines('\n')
                f.writelines('Product ID:, ')
                f.writelines(line[0] + ' ' + line[3])
                f.writelines('\n')

            ch1w1 = []
            ch1w2 = []
            ch1time = []

            ch2w1 = []
            ch2w2 = []
            ch2time = []

        elif line[1] == 'KC'and 'CH1' in line[3]:
            if 'NG' in line[3]:
                print(line[0]) #to judge NG happen in KC
            cnt1 += 1
            width = line[5]+','
            w1time = line[0]+','
            if cnt1 % 2 == 1:
                ch1time.append(w1time)
                ch1w1.append(width)
            elif cnt1 % 2 == 0:
                ch1w2.append(width)

        elif line[1] == 'KC'and 'CH2' in line[3]:
            if 'NG' in line[3]:
                print(line[0]) #to judge NG happen in KC
            cnt2 += 1
            width = line[5]+','  #beam width
            w1time = line[0]+','  #beam KC time
            if cnt2 % 2 == 1:
                ch2time.append(w1time)
                ch2w1.append(width)
            elif cnt2 % 2 == 0:
                ch2w2.append(width)

        # elif line[1] == 'KC'and 'CH1' in line[3]:
        #     cnt1 += 1
        #     width = line[5]+','
        #     w1time = line[0]+','
        #     if cnt1 % 2 == 1:
        #         ch1time.append(w1time)
        #         ch1w1.append(width)
        #     elif cnt1 % 2 == 0:
        #         ch1w2.append(width)

        # elif line[1] == 'KC'and 'CH2' in line[3]:
        #     cnt2 += 1
        #     width = line[5]+','  #beam width
        #     w1time = line[0]+','  #beam KC time
        #     if cnt2 % 2 == 1:
        #         ch2time.append(w1time)
        #         ch2w1.append(width)
        #     elif cnt2 % 2 == 0:
        #         ch2w2.append(width)
print('file is output to the file: "beam_width_result.txt", please check it.')

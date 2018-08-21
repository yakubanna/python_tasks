import sys

text1 = sys.argv[1]
command = list(open(text1).read())
array = [0]
current_command = int(0)
current_array = 0
return_te = []
count = 0
do = True

while current_command != len(command):
    if command[current_command] == '1':  # '1'
        if do:
            array[current_array] += 1
    else:
        current_command += 1
        if command[current_command] == '1':  # '01'
            current_command += 1
            if command[current_command] == '1':  # '011
                if do:
                    current_array -= 1
            else:  # '010'
                if do:
                    array.append(0)
                    current_array += 1
        else:  # '00'
            current_command += 1
            if command[current_command] == '0':  # '000'
                if do:
                    array[current_array] -= 1
            else:  # '001'
                current_command += 1
                if command[current_command] == '1':  # '0011'
                    t = return_te.pop()
                    if do:
                        if int(array[current_array]) > 0:
                            current_command = (t - 5)
                    else:
                        count -= 1
                        if count == 0:
                            do = True
                else:  # '0010'
                    current_command += 1
                    if command[current_command] == '0':  # '00100'
                        return_te.append(current_command)
                        if do:
                            if int(array[current_array]) > 0:
                                do = True
                            else:
                                do = False
                        if not do:
                            count += 1
                    else:
                        current_command += 1
                        if command[current_command] == '0':  # '001010'
                            if do:
                                print(chr(array[current_array]), end='')
                        else:  # '001011'
                            current_command += 1  # '0010110'
                            if do:
                                try:
                                    tep = ord(sys.stdin.read(1))
                                    array[current_array] = tep
                                except Exception:
                                    array[current_array] = 0
    current_command += 1

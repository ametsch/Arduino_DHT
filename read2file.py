#!/usr/bin/python3
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from serial import Serial
from datetime import datetime as dt
import pandas as pd
from matplotlib import pyplot as plt
import os

if not os.path.exists('./output/'):
    os.mkdir('./output')


def int_in_repeat(prompt: str) -> int:
    val = None
    try:
        val = int(input(prompt))
    except:
        print('Invalid entry, must be an INT')
        val = int_in_repeat(prompt)
    return val

global id 
id = 0
points = 0
columns = ['degF', 'percentHumidity', 'rawLight']

port = input('COM Port: ')
delay_reads = int_in_repeat('Delay (in reads): ')
read_count = int_in_repeat('Desired data point count: ')

li = {'degF':[],'percentHumidity':[],'rawLight':[]}

now = dt.now()
pth = f'{now.day}-{now.month}-{now.year}--{now.hour}-{now.minute}-{now.second}'
os.mkdir(f'./output/{pth}')
csv_name = f'./output/{pth}/out.csv'
graph_name = f'./output/{pth}/graph'
    
with Serial() as ser:
    ser.baudrate = 115200
    ser.port = port
    ser.open()
    
    with open(csv_name, 'xt', encoding='ASCII') as f:
        f.write('degF, percentHumidity, rawLight\n')
        pass

    ser.readline().strip()
    while points < read_count:
        temp = str(ser.readline().strip(), 'ASCII')

        if id % delay_reads == 0:
            print(temp)
            with open(csv_name, 'at', encoding='ASCII') as f:
                f.write(f'{temp}\n')
            liTemp = temp.split(', ')
            
            li['degF'].append(liTemp[0])
            li['percentHumidity'].append(liTemp[1])
            li['rawLight'].append(liTemp[2])

            points += 1
        else:
            pass
        id += 1

df = pd.DataFrame(data=li, columns=columns, dtype=float)

plot = df.plot()
plt.minorticks_on()
plt.xlabel('Data Point Number')
plt.ylabel('Data Value')

plt.savefig(f'{graph_name}.png')
plt.show()


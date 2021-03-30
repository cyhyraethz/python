import datetime
import os
import re

try:
  next_alarm = input('time of next alarm (hh:mm): ').split(':')
  next_alarm_hour,next_alarm_minute = [int(i) for i in next_alarm]
  wake_goal = input('eventual wake time goal (hh:mm): ').split(':')
  wake_goal_hour,wake_goal_minute = [int(i) for i in wake_goal]
  daily_increment = int(input('minutes to wake up earlier by each day: '))
except:
  raise TypeError('only integers are allowed')

start_day = datetime.date.today()
wake_goal = wake_goal_hour * 60 + wake_goal_minute
next_alarm = next_alarm_hour * 60 + next_alarm_minute + daily_increment
elapsed_days = 1
wake_times = ''

while next_alarm > wake_goal:
  next_alarm -= daily_increment
  hours = str(next_alarm // 60)
  minutes = str(next_alarm % 60)
  if len(minutes) < 2:
    minutes += '0'
  today = str((start_day + datetime.timedelta(days=elapsed_days)).strftime('%m-%d-%y'))
  wake_times += f'({today}) {hours}:{minutes}\n'
  elapsed_days += 1

print(wake_times)

write_file = False
file_name = 'set-alarm.txt'

if os.path.isfile(file_name):
  write_file = input('set-alarm.txt already exists, overwrite? (y/N): ')
else:
  write_file = input('write output to text file (set-alarm.txt)? (y/N): ')

if re.match(r'^ye?s?$', write_file, re.IGNORECASE) == None:
  write_file = False

if write_file:
  wake_up = open(file_name, "w+")
  wake_up.write(wake_times)
  wake_up.close()

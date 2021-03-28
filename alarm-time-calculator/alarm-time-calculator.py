import datetime
import os

try:
  wake_hour = int(input('Hour of your next alarm: '))
  wake_minute = int(input('Minute of your next alarm: '))
except:
  raise TypeError('Only integers are allowed')

filepath = os.path.join(os.path.expanduser('~') + '/Documents', 'set-alarm.txt')
wake_up = open(filepath, "w+")

start_day = datetime.date.today()
alarm_time = wake_hour * 60 + wake_minute
elapsed_days = 0
wake_times = ''

while alarm_time > 5 * 60:
  alarm_time -= 10
  hours = str(alarm_time // 60)
  minutes = str(alarm_time % 60)
  if len(minutes) < 2:
    minutes += '0'
  today = str((start_day + datetime.timedelta(days=elapsed_days)).strftime('%m-%d-%y'))
  wake_times += f'({today}) {hours}:{minutes}\n'
  elapsed_days += 1

print(wake_times)

wake_up.write(wake_times)
wake_up.close()

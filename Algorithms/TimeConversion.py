full_time = input().split(':')
hour = full_time[0]
second = full_time[1]
final_value = full_time[-1]
millisecond = final_value[:-2]
period = final_value[-2:]

if period == 'PM':
  if hour == '12':
    time = int(hour) 
  else:
    time = int(hour) + 12
  hour = str(time)
else:
    if hour == '12':
      hour = '00'

print(f'{hour}:{second}:{millisecond}')

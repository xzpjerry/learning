from datetime import datetime, timedelta, timezone
import re

def handle_str_dt(dt_str, dtz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    rule_dtz_str = r'UTC([\+\-])(0[0-9]|1[0-2]|[0-9])\:([0-5][0-9])' 
    re_result = re.match(rule_dtz_str, dtz_str)
    if re_result:
        UTC_marker = re_result.group(1)
        UTC_hour = re_result.group(2)
        UTC_min = re_result.group(3)
        num_hours = int(UTC_hour)
        num_min = int(UTC_min)
        return dt, num_hours, num_min, UTC_marker
    else:
        raise TypeError('Illegal')

def to_timestamp(dt_str, tz_str):
    dt, tz_hour, tz_min, marker = handle_str_dt(dt_str, tz_str)
    if marker == '+':
        the_tz = timezone(timedelta(hours = tz_hour))
    else:
        the_tz = timezone(timedelta(hours = -tz_hour))
    dt = dt.replace(tzinfo = the_tz)
    return dt.timestamp()
'''
a = handle_str_dt('2015-6-1 08:10:30', 'UTC+7:00')
print(type(a))
print(a.tzinfo)
a_timezon = timezone(timedelta(hours = -1))

a = a.replace(tzinfo = a_timezon)
print(a.tzinfo)
'''
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')
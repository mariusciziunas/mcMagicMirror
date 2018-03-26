from .models import Config, State
from datetime import datetime, timedelta

def set_alarm_clock_job():
    try:
        config = Config.objects.get(key = 'alarm.time')
    except Config.DoesNotExist:
        pass

    alarm_time = datetime.strptime(config.value, '%H:%M')
    now = datetime.now()
    if ((now.hour + 1 == alarm_time.hour) and (now.minute == alarm_time.minute)):
        alarm_clock_state = 'alarm_active'
        try:
            state = State.objects.get(key = alarm_clock_state)
            state.value = 1
            state.last_updated = datetime.now()
            state.save()
        except State.DoesNotExist:
            print('state [' + alarm_clock_state + '] does not exist in the DB. Creating one')
            State.objects.create(key=alarm_clock_state, value='1')

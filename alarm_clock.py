class AlarmClock:
    def __init__(self):
        self.current_time = '12:00'
        self.alarm_time = '12:00'
        self.turned_on = False

    def set_current_time(self,):
        self.current_time = input('What is the current time?: ')
        print(f'The time is {self.current_time}')

    def set_alarm(self,):
        self.alarm_time = input('What is the alarm time?: ')
        print(f'The alarm time is {self.alarm_time}')

    def toggle_on_off(self):
        if self.turned_on == True:
            self.turned_on = False
            print('The alarm has been switched off')
        else:
            self.turned_on = True
            print('The alarm has been switched on')
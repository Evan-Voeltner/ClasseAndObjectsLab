class CellPhone:
    def __init__(self, model):
        self.model = model
        self.phone_number = ''
        self.contacts = [{
            'name' : 'Dad',
            'phone_number' : '414-555-2102'
        },
        {
            'name' : 'Mom',
            'phone_number' : '414-555-6541'
        },
        {
            'name' : 'Nevin',
            'phone_number' : '414-555-1686'
        },
        {
            'name' : "Nevin's Dad",
            'phone_number' : '414-555-6969'
        }]
        self.messages = []
        self.vibrate_mode = False

    def recieve_text_messsage(self, text_message):
        self.messages.append(text_message)
        print(text_message)

    def toggle_vibrate_mode(self):
        if self.vibrate_mode == True:
            self.vibrate_mode = False
            print('Vibrate mode is off')
        else:
            self.vibrate_mode = True
            print('Vibrate mode is on')

    def send_text_message(self):
        text_message = input('Write your message: ')
        print(text_message)
        return(text_message)
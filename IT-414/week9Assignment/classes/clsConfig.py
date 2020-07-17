
class Configuration:
    def __init__(
        self,
        mail_server,
        mail_port,
        username,
        password,
        from_email,
        to_email,
        twilio_account_id,
        twilio_auto_token,
        twilio_trial_number,
        twilio_cell_number,
        last_text
    ):
        self.mail_server = mail_server
        self.mail_port = mail_port
        self.username = username
        self.password = password
        self.from_email = from_email
        self.to_email = to_email
        self.twilio_account_id = twilio_account_id
        self.twilio_auto_token = twilio_auto_token
        self.twilio_trial_number = twilio_trial_number
        self.twilio_cell_number = twilio_cell_number
        self.last_text = last_text

    def update_last_text(self, value):
        self.last_text = value

    def get_last_text(self): 
        return self.last_text 

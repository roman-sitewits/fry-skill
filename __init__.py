from mycroft import MycroftSkill, intent_file_handler


class Fry(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fry.intent')
    def handle_fry(self, message):
        self.speak_dialog('fry')


def create_skill():
    return Fry()


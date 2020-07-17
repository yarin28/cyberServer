import json


class Message:
    def __init__(self, message, sender, time):
        self.message = message
        self.sender = sender
        self.time = time

    def __repr__(self):
        return 'the class itself'

    def __str__(self):
        return f'{self.message} +{self.sender} +{self.time}'

    def add_message(self, messeges):
        messeges.append(self)
        return messeges

def obj_to_dict(obj):
    return obj.__dict__



def write_messeges(messeges):
    dt = {}
    dt.update(vars(Message))
    json_string = json.dumps\
        (messeges, default=obj_to_dict)
    with open("Message_log.json", "w") as file:
        file.write(json_string)

def read_messeges():
    mm = []
    with open("Message_log.json", "r") as file:
        mm = json.loads(file.read())
    return mm


def main():
    messages = []
    messages += [Message("hello", 1, 1112),
                 Message("hi", 2, 1113),
                 Message("popo", 1, 1114), ]
    dt = {}
    dt.update(vars(Message))
    json_string = json.dumps \
        (messages, default=obj_to_dict)
    with open("Message_log.json", "w") as file:
        file.write(json_string)


if __name__ == "__main__":
    read_messeges()

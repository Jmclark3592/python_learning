messages = ['i love you', 'you\'re doing great', 'i\'m really proud of you']
sent_messages = []

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(unsent, sent):
    while unsent:
        sent_message = unsent.pop()
        print(f"sent message {sent_message}")
        sent.append(sent_message)

send_messages(messages[:], sent_messages)

print(f"messages in first list {messages}")
print(f"messages in second list {sent_messages}")
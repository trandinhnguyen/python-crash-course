def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    messages_copy = messages[:]
    # messages_copy = messages.copy()

    while messages_copy:
        message = messages_copy.pop()
        sent_messages.append(message)


messages = ['hello', 'hi', 'bye']
sent_messages = []

send_messages(messages, sent_messages)
# send_messages(messages[:], sent_messages)
show_messages(messages)
show_messages(sent_messages)

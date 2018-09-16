class OffsetIsOutQueueException(Exception):
    pass


class Queue():
    def __init__(self, messages):
        self.messages = messages
        self.messages_count = len(self.messages)

    def get_message(self, offset):
        if offset > self.messages_count:
            raise OffsetIsOutQueueException
        pass


def get_messages_in_queue(queue_instance):
    pass


if __name__ == '__main__':
    messages_in_queue = get_messages_in_queue(queue_instance)
    for message in messages_in_queue:
        print(message)

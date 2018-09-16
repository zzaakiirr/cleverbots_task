import unittest

from Queue import Queue, OffsetIsOutQueueException, get_messages_in_queue


class MessagesInQueueTest(unittest.TestCase):
    def setUp(self):
        messages = ['message1', 'message2', ]
        self.queue = Queue(messages)
        self.messages_in_queue = get_messages_in_queue(self.queue)

    def test_get_messages_in_queue_run_through_queue_instance_messages(self):
        for message in self.messages_in_queue:
            assertIn(message, queue.messages)

    def test_get_message_return_offset_is_out_queue_exception(self):
        with self.assertRaises(OffsetIsOutQueueException):
            self.queue.get_message(offset=self.queue.messages_count + 1)

    def test_return_correct_data(self):
        expected_messages = self.messages
        returned_messages = self.messages_in_queue
        self.assertEqual(expected_data, returned_messages)


if __name__ == '__main__':
    unittest.main()

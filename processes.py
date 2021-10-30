from service import Service

class Processes:
    def process_one(self, pipe12):
        pid = '1'
        counter = 0
        counter = Service.event(pid, counter)  # a
        counter = Service.send_message(pipe12, pid, counter)  # b
        counter = Service.event(pid, counter)  # c
        counter = Service.get_message(pipe12, pid, counter)  # d
        counter = Service.send_message(pipe12, pid, counter)  # e

    def process_two(self, pipe23, pipe21):
        pid = '2'
        counter = 0
        counter = Service.get_message(pipe21, pid, counter)  # f
        counter = Service.get_message(pipe23, pid, counter)  # g
        counter = Service.send_message(pipe21, pid, counter)  # h
        counter = Service.get_message(pipe21, pid, counter)  # i
        counter = Service.get_message(pipe23, pid, counter)  # j

    def process_three(self, pipe32):
        pid = '3'
        counter = 0
        counter = Service.event(pid, counter)  # k
        counter = Service.send_message(pipe32, pid, counter)  # l
        counter = Service.send_message(pipe32, pid, counter)  # m
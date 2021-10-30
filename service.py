from datetime import datetime

class Service:
    @staticmethod
    def local_time(counter):
        return ': Время по Лэмпорту = ' + str(counter) + ', Локальное время = ' + str(datetime.now()
                                                                         .strftime("%H:%M:%S.%f"))
    @staticmethod
    def sync_received_timestamp(new_timestamp, counter):
        return max(new_timestamp, counter) + 1

    @staticmethod
    def event(pid, counter):
        counter += 1
        print('Что-то произошло в процессе {}'. \
              format(pid) + Service.local_time(counter))
        return counter

    @staticmethod
    def send_message(pipe, pid, counter):
        counter += 1
        pipe.send(('', counter))
        print('Сообщение отправлено из процесса ' + str(pid) + Service.local_time(counter))
        return counter

    @staticmethod
    def get_message(pipe, pid, counter):
        message, timestamp = pipe.recv()
        counter = Service.sync_received_timestamp(timestamp, counter)
        print('Сообщение получено от процесса ' + str(pid) + Service.local_time(counter))
        return counter

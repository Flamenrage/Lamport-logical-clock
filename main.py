from multiprocessing import Process, Pipe
from processes import Processes


if __name__ == '__main__':
    oneandtwo, twoandone = Pipe()
    twoandthree, threeandtwo = Pipe()

    processes = Processes()
    first_process = Process(target=processes.process_one, args=(oneandtwo,))
    second_process = Process(target=processes.process_two, args=(twoandthree, twoandone))
    third_process = Process(target=processes.process_three, args=(threeandtwo,))

    first_process.start()
    second_process.start()
    third_process.start()

    first_process.join()
    second_process.join()
    third_process.join()
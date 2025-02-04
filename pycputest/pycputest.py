####################################################
#  ____         ____ ____  _   _ _____         _
# |  _ \ _   _ / ___|  _ \| | | |_   _|__  ___| |_
# | |_) | | | | |   | |_) | | | | | |/ _ \/ __| __|
# |  __/| |_| | |___|  __/| |_| | | |  __/\__ \ |_
# |_|    \__, |\____|_|    \___/  |_|\___||___/\__|
#        |___/
####################################################
# made by mingfei with LM studio
####################################################

# importing libraries
import multiprocessing
import time
import numpy as np


# stress testing function
def cpu_intensive_task(index, start_time, test_time):
    print(f"Process {index} started.")
    while (time.perf_counter() - start_time) < test_time:
        try:
            # get a random number & calculate sin, cos, tan of the said number
            x = np.random.rand(10000000)
            y = np.sin(x)
            z = np.cos(y)
            w = np.tan(z)
            print(f"random: {x}")
        except Exception as e:
            # error handling
            print(f"Error in process {index}: {str(e)}")
            print("Program exiting...")
        finally:
            # release any resources used by the process
            pass


# main function
def main():
    num_physical_cores = multiprocessing.cpu_count()
    # get test time from user
    try:
        test_time = int(input("How long you want this test to run:"))
    except Exception as e:
        # error handling
        print(f"Error in input: {str(e)}")
        print("Program exiting...")
        exit()

    # stdout message
    print("CPU Stressing Tool started. Press Ctrl+C to stop.")
    print(f"Running for {test_time} second(s) on {num_physical_cores} physical cores.")

    # timer
    start_time_all = time.perf_counter()

    # spawn multiple processes to use all cores
    processes = []
    for i in range(num_physical_cores):
        index = i
        p = multiprocessing.Process(
            target=cpu_intensive_task, args=(index, start_time_all, test_time))
        p.start()
        processes.append(p)


# run only if not being imported by other program
if __name__ == "__main__":
    main()

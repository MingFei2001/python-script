# PyCPUTest
```
 ____         ____ ____  _   _ _____         _
|  _ \ _   _ / ___|  _ \| | | |_   _|__  ___| |_
| |_) | | | | |   | |_) | | | | | |/ _ \/ __| __|
|  __/| |_| | |___|  __/| |_| | | |  __/\__ \ |_
|_|    \__, |\____|_|    \___/  |_|\___||___/\__|
       |___/
```

## Overview
PycpuTest is a Python script designed to stress the CPU's capabilities by performing computationally intensive tasks for a specified time period. This project utilizes multiple processes to take full advantage of multiple-core CPUs.

### [LM Studio](https://lmstudio.ai/)
> *It's a cool project ngl*

This code was developed while I was playing with LM Studio. The idea for a CPU stressing tool emerged as a test project.

## ⚠️ Lag Warning
> Largely attempted to get CPU stressing results may cause lag due to excessive CPU usage... but let's be real, you probably want to stress your CPU anyway lol.

## Features
- CPU Stressing: PycpuTest generates random numbers, calculates their sine, cosine, and tangent values, and stores these calculations in memory for an extended period.
- Multithreading/Multiprocessing: The script utilizes Python's multiprocessing module to spawn multiple processes that execute the same task concurrently.

## Installation
1. Clone this repository using your preferred method (e.g. `git clone https://github.com/MingFei2001/pycputest.git`)
2. Open a terminal or command prompt and navigate to the project directory.
3. Install dependencies by running `pip install -r requirements.txt`.
4. Run the script by typing `python test.py`. (Good luck 🤞!!)

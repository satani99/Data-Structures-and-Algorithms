def towerofhanoi(numberofdisks, startpeg=1, endpeg=3):
    if numberofdisks:
        towerofhanoi(numberofdisks-1, startpeg, 6-startpeg-endpeg)
        print(f"Move disk {numberofdisks} from peg {startpeg} to peg {endpeg}")
        towerofhanoi(numberofdisks-1, 6-startpeg-endpeg, endpeg)


towerofhanoi(numberofdisks=4)

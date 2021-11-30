import time
from plant_monitor import Plant

if __name__ == '__main__':
    arrowhead = Plant('arrowhead', 1, 0, 60)
    while True:
        if arrowhead.dry():
            print(arrowhead.moisture)
            #arrowhead.water()
        time.sleep(1)

    

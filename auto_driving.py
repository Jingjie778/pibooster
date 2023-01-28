import picar_4wd as fc
import random

def main():
    while True:
        scan_list = fc.scan_step(30)
        if not scan_list:
            continue
        det = random.randint(0,1)
        if scan_list[3:7] != [2,2,2,2]:
            if(det):
                fc.turn_left(10)
            else:
                fc.turn_right(10)
        else:
            fc.forward(20)
            
if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()

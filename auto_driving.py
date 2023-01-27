import picar_4wd as fc
import random
power = 20

def main():
    while True:
        scan_list = fc.scan_step(30)
        if not scan_list:
            continue
            
        left_sum =scan_list[0] + scan_list[1] + scan_list[2]
        right_sum =scan_list[7] + scan_list[8] + scan_list[9]
        if scan_list[3:7] != [2,2,2,2]:
            if(left_sum > right_sum):
                fc.turn_left(10)
            elif(left_sum < right_sum):
                fc.turn_right(10)
            else:
                fc.backward(5)
        else:
            fc.forward(20)
            
if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()

import picar_4wd as fc
power = 20

def main():
    while True:
        scan_list = fc.scan_step(30)
        if not scan_list:
            continue
            
        if scan_list[3:7] != [2,2,2,2]:
            if(scan_list[0] or scan_list[1] or scan_list[2]):
                fc.turn_left(10)
            elif(scan_list[7] or scan_list[8] or scan_list[9]):
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

import picar_4wd as fc
power = 20

def main():
    while True:
        scan_list = fc.scan_step(30)
        if not scan_list:
            continue
            
        tmp = scan_list[3:7]
        print(tmp)
        print(scan_list)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()

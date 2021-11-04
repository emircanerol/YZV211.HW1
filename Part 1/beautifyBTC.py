def arrange():
    # delete unnecessary rows and round numbers to 2 digits
    with open("/Users/emircanerol/Desktop/BTCUSD_minute.csv",'r') as f:
        c = open("/Users/emircanerol/Desktop/BTCUSD_min.csv",'w')
        first_line = f.readline()
        first_line = ",".join(first_line.strip().split(',')[:-1]) + '\n'
        c.write(first_line)
        del first_line
        for line in f:
            line = line.strip().split(',')
            line[0] = line[0][:-3]
            line[3] = "%.2f"%(float(line[3]))
            line[4] ="%.2f"%(float(line[4]))
            line[5] ="%.2f"%(float(line[5]))
            line[6] ="%.2f"%(float(line[6]))
            del line[7]
            del line[2]
            line = ",".join(line) + '\n'
            c.write(line)
        c.close()
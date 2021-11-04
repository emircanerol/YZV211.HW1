def FillEmptyData(btc):
    with open('BTCUSDnew.csv', 'r') as f:
        not_empty = open('BTCUSD_min2.csv', 'w')
        titles = f.readline().strip().split(',')
        prev_line = f.readline().strip().split(',')
        not_empty.write(",".join(titles[:-1]) + '\n' + ",".join(prev_line) + '\n')
        prev_unix = prev_line[0]
        for line in f:
            line = line.strip().split(',')
            unix = line[0]
            if int(unix) == (int(prev_unix) - 60):
                prev_line = line
                prev_unix = unix
                not_empty.write(",".join(line) + '\n')
                continue

            space_len = int((int(prev_unix) - int(unix)) / 60) - 1
            for i in range(space_len, 0, -1):
                new_unix = int(unix) + (60 * i)
                new_line = prev_line
                new_line[0] = str(new_unix)
                not_empty.write(",".join(new_line) + '\n')
            prev_unix = unix
            prev_unix = unix
            not_empty.write(",".join(line) + '\n')

    not_empty.close()

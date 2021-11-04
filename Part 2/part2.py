def remove_unnecessity():
    # file paths
    fp = '/Users/emircanerol/Downloads/hw1_data.csv'
    fp_renew = '/Users/emircanerol/Downloads/hw1_data_renewed.csv'

    delimiter = ':'

    # open the file in read mode
    with open(fp, 'r') as f:
        # index is for removing regions
        index = 0
        # new_file to write updated data
        new_file = open(fp_renew, 'w')
        # titles are determined and wrote on the file
        headers = ['State Name',
                   'April 1, 2010 Census',
                   'April 1, 2011 Base',
                   'July 1, 2010 Population',
                   'July 1, 2011 Population']
        new_file.write(delimiter.join(headers) + '\n')

        # every line is seperated up to quotes(") and all unnecessary
        # signs are removed with strip function
        for line in f:
            # index indicates line number
            index += 1
            # commas are removed
            line = line.replace(',', '')
            # signs are orderly removed
            # with split function string is separated
            line = line.strip('\n').strip(',').strip('.').split('"')
            new_line = []
            # empty strings are removed
            for element in line:
                if element != '':
                    new_line.append(element)
            # empty arrays and texts are removed
            if len(new_line) == 5 and index not in range(6, 10):
                new_file.write(delimiter.join(new_line) + '\n')
    # file is closed in order to save memory
    new_file.close()
    # file path and separator is returned
    return fp_renew, delimiter


def create_df():
    fp, delim = remove_unnecessity()
    import pandas as pd
    # data is read by read_csv
    population = pd.read_csv(fp, delimiter=delim)
    # data frame is sorted with decreasing order
    population = population.sort_values(by=['April 1, 2010 Census'], ascending=False)
    # indices are updated
    population = population.reset_index(drop=True)
    # file is saved
    population.to_csv('state_populations.csv')


# function call
create_df()

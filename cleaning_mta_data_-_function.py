

def fix_turnstile_data(filenames):
    """
    Takes list of MTA raw data filenames and cleans them up.
    
    Takes a list of filenames (containing MTA raw data) and cleans up
    the file, saving this new version as "updated_<filename>.txt".
    """
    for name in filenames:
        new_csv = open('updated_' + name, 'a')
        with open(name, 'r') as f:
            for line in f:
                line = line.strip().split(',')

                prefix = ','.join(line[:3])
                content = line[3:]
        
                while content:
                    temp = []
                    for i in range(5):
                        temp.append(content.pop(0))
                    newline = prefix + ',' + ','.join(temp)+'\n'
                    new_csv.write(newline)
        new_csv.close()


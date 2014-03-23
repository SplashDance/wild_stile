def fix_turnstile_data(filenames):
    
    for name in filenames:
        new_csv = open('updated_' + name, 'a')
        with open(name, 'r') as f:
            for line in f:
                line = line.split(',')
                for element in line:
                    element.strip()

                prefix = ','.join(line[:3])
                content = line[3:]
        
                while content:
                    temp = []
                    for i in range(5):
                        temp.append(content.pop(0))
                    newline = prefix + ',' + ','.join(temp)+'\n'
                    new_csv.write(newline)
        new_csv.close()


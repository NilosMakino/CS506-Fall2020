import csv

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path, newline='') as csvfile: 
        reader = csv.reader(csvfile, delimiter=' ', quotechar='"')
        
        matrix = []
        for row in reader: 
            newrow = []
            for x in row[0].split(','):
                if x.isnumeric():
                    newrow += [int(x)]
                else:
                    newrow += [x]
            matrix += [newrow]
        return matrix

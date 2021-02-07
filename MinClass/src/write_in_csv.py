import csv
import os
import networkx

from src.read import get_graph


def csv_file_name(path):
    file_list = os.listdir(path)
    for i in file_list:
        if i[-3:] == 'csv':
            return i

def cvs_file_write(path,csv_file_name,col_name,data):
    csv_file1 = open(path+csv_file_name)
    csv_reader = csv.reader(csv_file1)
    csv_file2 = open(path+"data/"+col_name+".csv", 'wt')
    csv_file3 = open(path+"none_data/"+col_name+".csv",'wt')
    csv_writer2 = csv.writer(csv_file2)
    flag = 1
    for row in csv_reader:
        if flag != 1:
            if data.get(row[2]) != None:
                row.append(data.get(row[2]))
            else:
                row.append('None')
            csv_writer2.writerow(row)
            try:
                data.pop(row[2])
            except Exception as e:
                pass
        else:
            row.append(col_name)
            csv_writer2.writerow(row)
            flag = 0
    # print(data)
    csv_writer3 = csv.writer(csv_file3)
    row = ["class_name",col_name]
    csv_writer3.writerow(row)
    for none_data in data:
        row = [none_data,data.get(none_data)]
        csv_writer3.writerow(row)
    csv_file1.close()
    csv_file2.close()
    csv_file3.close()
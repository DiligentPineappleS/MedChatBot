# Chinese medical dialogue data 中文医疗问答数据集







import json
import random
import os

def rs_json(file_path,save_path):
    file_name  = os.path.basename(file_path)
    file_name = file_name.replace('.csv','')
    json_file = open(save_path+file_name+'.json', mode='w',encoding='utf-8')
    f = open(file_path, encoding='utf-8') 
    i=0
    data_list = []
    for line in f:
        lin = line.split(',')
        if i==0:
            i = i+1
            continue        
        print(lin)
        if len(lin) == 4:
            if len(lin[1]+','+lin[2])<200 and len(lin[3])<200:
                temp_data_json = {}
                med_type = lin[1]
                input = lin[1]+','+lin[2]
                answer = lin[3]
                temp_data_json['instruction'] = f"现在你是一个{med_type}医生，请根据患者的问题给出建议："
                temp_data_json['input'] =  input
                temp_data_json['output'] = answer
                data_list.append(temp_data_json)
        i = i+1

    random.shuffle(data_list)
    json.dump(data_list, json_file, indent=4,ensure_ascii=False)   
    json_file.close() 

def data_csv2json(read_dir,save_path):
    
    if os.path.isdir(read_dir):
        read_path_list = os.listdir(read_dir)
        for read_path in read_path_list:
            temp_read_path = os.path.join(read_dir,read_path)
            if os.path.isfile(temp_read_path) and  temp_read_path.endswith('.csv'):
                rs_json(temp_read_path,save_path)
            else:
                file_list = os.listdir(temp_read_path)
                for file in file_list:
                    file_path = temp_read_path+"/"+file 
                    if os.path.isfile(file_path) and  file_path.endswith('.csv'):
                        rs_json(file_path,save_path) 
    elif os.path.isfile(read_dir)  and  file.endswith('.csv'):
        rs_json(read_dir,save_path)







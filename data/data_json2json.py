
import json
import random
# 1. 处理ChatMed_Consult_Dataset/ChatMed_Consult-v0.3.json
#数据介绍：

    #query: 互联网真实问题.
    #response: OpenAI GPT-3.5 生成答案.
    #样例：
        # {"query": "喉咙发紧干精神有点紧绷早上起来手也没有力气。一直在担心。", "response": "您可能需要注意以下几点：\n\n1. 饮食方面，注意多喝水并避免食用刺激性食物，如辣椒、咖啡、酒等。\n\n2. 保持室内空气湿润，可以使用加湿器或者放置一盆水。\n\n3. 适当休息，避免过度疲劳。可以尝试进行一些轻度的运动或者放松的活动，如瑜伽、冥想等。\n\n4. 如果症状持续或者加重，建议就医或者咨询医生。可能需要进一步的检查和治疗。"}
        # {"query": "为什么昨晚强行想和女友发生关系但是就是硬不起来", "response": "我了解您的情况可能会让您感到尴尬和不舒服，但是这是一个很常见的问题，很多男性都会遇到。可能有多种原因导致这种情况发生，例如情绪问题、压力、过度疲劳、药物或饮酒的影响、身体疾病等等。建议您寻求医生或专业人士的帮助，他们可以帮助您找出原因并提供适当的治疗方案。同时，保持健康的生活方式，如健康饮食、充足睡眠、适度运动等，也可以有助于改善您的情况。"}

def ChatMed_Consult(data_path,save_path):
    json_file = open(save_path, mode='w',encoding='utf-8')
    data_list =[]
    f =  open(data_path, 'r')

    for lin in f:
        print(lin,json.loads(lin))
        line = json.loads(lin)
        temp_data_json = {}
        temp_data_json['instruction'] = '现在你是一名医生，请根据患者的问题给出建议：'
        temp_data_json['input'] =  line["query"]
        temp_data_json['output'] = line["response"]
        data_list.append(temp_data_json)
    random.shuffle(data_list)
    json.dump(data_list, json_file, indent=4,ensure_ascii=False)   
    json_file.close()   
    
    
    


    
    
     
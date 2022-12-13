

import json
from datetime import datetime
import pytz



my_datetime_cet = datetime.now().astimezone(pytz.timezone('Europe/Berlin')).strftime('%Y-%m-%d %H:%M:%S')

global_max_temp = 26
global_min_temp =14
global_max_humid =350
global_min_humid =64
global_max_voc =2.1
global_min_voc =0.5

max_temp = 20
min_temp = 15
avg_temp = 16
max_hum = 308
min_hum = 140
avg_hum = 200
max_VOC = 2
min_VOC = 1.3
avg_VOC = 1.9

iteration = 7 #n_images

measurements = {f"{iteration}": {
            # set temperature
			"temperature": {"max":max_temp, "min":min_temp, "avg":avg_temp},
            # set humidity
			"humidity": {"max":max_hum, "min":min_hum, "avg":avg_hum},
            # set VOC
			"VOC": {"max":max_VOC, "min":min_VOC, "avg":avg_VOC},
            # set time
            "time":{"time": f"{my_datetime_cet}"}
		}}


global_min_max = {
        "global_max_temp":global_max_temp,
        "global_min_temp":global_min_temp,
        "global_max_humid":global_max_humid,
        "global_min_humid":global_min_humid,
        "global_max_voc":global_max_voc,
        "global_min_voc":global_min_voc
    }

with open('graph.json','r+') as file:
    file_data = json.load(file)
    file_data["measurements"].update(measurements)
    json.dump(file_data, file, indent = 4)

    # update global min and max
    file_data["global_min_max"] = global_min_max
    file.seek(0)  #  Sets file's current position at offset.
    json.dump(file_data, file, indent = 4)
    file.truncate()
file.close()



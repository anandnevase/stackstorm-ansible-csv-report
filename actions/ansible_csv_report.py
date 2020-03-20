from st2common.runners.base_action import Action
import json
import sys
import csv

class JsonStringToObject(Action):

    def run(self, input_json, csv_path):
      data = json.loads(input_json)
      out_file = open(csv_path, 'w') 
      with open(output_file, 'w') as csvfile:
        fieldnames = ['Hostname', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for host in data['hosts'].keys():
          writer.writerow({'Hostname': host, 'Status': 'failed' if (data['hosts'][host]['dark']==0) else 'passed'})

      return true

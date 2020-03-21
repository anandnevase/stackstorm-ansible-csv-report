from st2common.runners.base_action import Action
import json
import sys
import csv

class JsonStringToObject(Action):

    def run(self, input_json, csv_path):
      data = json.loads(input_json)
      with open(csv_path, 'w') as csvfile:
        fieldnames = ['Hostname', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for host in data.iterkeys():
          writer.writerow({'Hostname': host, 'Status': 'failed' if (data[host]['dark']!=0) else 'passed'})

      return true

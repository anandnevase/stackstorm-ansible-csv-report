from st2common.runners.base_action import Action
import json
import ast
import csv

class JsonStringToObject(Action):

    def run(self, input_json, csv_path):
      data = ast.literal_eval(json.loads(input_json))
      with open(csv_path, 'w') as csvfile:
        fieldnames = ['Hostname', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for host, value in data.iteritems():
          writer.writerow({'Hostname': host, 'Status': 'failed' if (value['dark']!=0) else 'passed'})

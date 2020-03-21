#!/usr/local/bin/python
# coding: utf8
import json
import datetime
import sys

def main(argv):
  dt = datetime.datetime.today()
  
  with open('/config/data/energy_daily_simples_kw.json', 'r') as data_file:
    try:
      data = json.load(data_file)
    except ValueError:
      data = {
        str(dt.year): {
          dt.strftime("%B"): {
            str(dt.day): 0.0
          }
        }
      }
  
  with open('/config/data/energy_daily_simples_kw.json', 'w') as data_file:
    data[str(dt.year)][dt.strftime("%B")][str(dt.day)] = float(argv)
    json.dump(data, data_file)

if __name__ == "__main__":
  try:
    main(sys.argv[1])
  except IndexError:
    raise ValueError("Argument required")
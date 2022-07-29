# # from funcs import send_email
# from dateutil import parser
# from datetime import date, datetime
# import dateparser

# config_start_date = dateparser.parse("tomorrow at 12:00 AM")
# config_end_date = dateparser.parse("yesterday at 09:00 AM")
# current_time = datetime.now()

# print(current_time>config_start_date)

import sys,json

f = open(sys.argv[1], 'r') #input.ipynb
j = json.load(f)
of = open(sys.argv[2], 'w') #output.py
if j["nbformat"] >=4:
        for i,cell in enumerate(j["cells"]):
                of.write("#cell "+str(i)+"\n")
                for line in cell["source"]:
                        of.write(line)
                of.write('\n\n')
else:
        for i,cell in enumerate(j["worksheets"][0]["cells"]):
                of.write("#cell "+str(i)+"\n")
                for line in cell["input"]:
                        of.write(line)
                of.write('\n\n')

of.close()
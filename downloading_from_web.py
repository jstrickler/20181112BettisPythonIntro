#!/usr/bin/env python
import requests
import os
#  response = requests.get(URL, option .....)

response = requests.get('http://www.python.org')
if response.status_code == requests.codes.OK:  # 200
    print(response.content.decode())

URL = "https://navalnuclearlab.energy.gov/ckfinder/userfiles/files/October%202018%20Update%20to%20the%20Kesselring%20Site%20Refueling%20and%20Overhaul%20of%20the%20S8G%20Prototype.pdf"

FILE_NAME = 'nnlstuff.pdf'
response = requests.get(URL)
if response.status_code == requests.codes.OK:
    pdf_data = response.content
    with open(FILE_NAME, 'wb') as pdf_out:
        pdf_out.write(pdf_data)

os.system("open {}".format(FILE_NAME))





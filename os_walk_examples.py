#!/usr/bin/env python
import os
from datetime import datetime

START_DIR = "."

for curr_dir, dir_list, file_list in sorted(os.walk(START_DIR)):
    print(curr_dir)
    for file_name in file_list:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            # print("   file path:", file_path)
            file_size = os.path.getsize(file_path)
            raw_ts = os.path.getmtime(file_path)
            time_stamp = datetime.fromtimestamp(raw_ts)
            print("  {:5d} {} {}".format(
                file_size, time_stamp.date(), file_name)
            )

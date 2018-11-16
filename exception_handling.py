#!/usr/bin/env python

file_name = 'wombat_disco.txt'

try:
    with open(file_name) as file_in:
        pass
except IOError as err:
    print("Unable to open file:", err)

MAX_ERRORS = 5

a = 23.5

values = [4.5, 6.7, "4.9", 8.1, 3.9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.2, 5.0]

error_count = 0

for i, v in enumerate(values):
    try:
        result = a / v
#        raise DeprecationWarning('AHA!')
    except ZeroDivisionError as err:
        print("Problem with element {}: {} -- {}".format(
            i, v, err))
        error_count += 1
        if error_count == MAX_ERRORS:
            exit()
    except (TypeError, ValueError) as err:
        print("Whoops:", err)
    except Exception as err:
        print("default case:", err)
    else:
        print(result)
    finally:
        print("processed", v)

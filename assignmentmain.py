def c_message(msg):
    c_msg = ""
    count = 1

    for i in range(1, len(msg)):
        if msg[i] == msg[i - 1]:
            count += 1
        else:
            if count > 1:
                c_msg += msg[i - 1] + str(count)
            else:
                c_msg += msg[i - 1]
            count = 1

    # Handle the last character(s)
    if count > 1:
        c_msg += msg[-1] + str(count)
    else:
        c_msg += msg[-1]

    return c_msg

# Read input
msg = input()

# Compress the message and print the result
c_msg = c_message(msg)
print(c_msg)

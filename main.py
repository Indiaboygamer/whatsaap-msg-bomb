import pywhatkit as kit
import time

number = ""  # number with country code

message = "" #enter your message

# Send message with loop
for i in range(10):
    kit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
    time.sleep(1)  # delay between messages

import subprocess
from string import digits
import time
import http.client
import random

# This method is not mine
def send(message):
    conn = http.client.HTTPSConnection("discordapp.com")
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\n" + message + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
    }

    webhook = '<Our discord webhook>'

    conn.request("POST", webhook, payload, headers)

    res = conn.getresponse()
    data = res.read()
    response = data.decode("utf-8")

    # checks if there is a response
    if response:
        # check if it's a rate limit
        if "You are being rate limited" in response:
            # find the wait time, it will be on the same line as "retry after"
            index1 = response.find('"retry_after"')
            wait = ''
            # we are going to go through the string starting after "retry_after" and look for digits
            for character in response[index1 + 15:]:
                # we do '+ 15' to skip the start of the line and just grab the digits after
                if character.isdigit():
                    wait += character
                elif character == '\n':
                    # ordering may be different, so we will set it to stop when the new line character is hit
                    break

            # turn wait into a number
            wait = int(wait)

            # wait is milliseconds, so must convert to seconds
            # we will also add 0.1 seconds to it just to ensure we are over the wait time
            wait = wait / 1000 + 0.1

            # now we will wait that amount of time and try sending the message again
            print("waiting " + str(wait) + " seconds")
            time.sleep(wait)
            send(message)

        else:
            # print the response if its something else
            print(data.decode("utf-8"))


# Open our Prefix output
with open('PrefixCheckOutput.txt') as f:
    testOutput = f.read().splitlines()

# For every line in the file, find the user and call discord.
for line in testOutput:
    data = line.split(',')

	#With this batch file we request the filelog of the path specified in the PrefixOutput.txt
    item = subprocess.Popen(['PollP4Changes.bat', data[0]], shell=True, stdout=subprocess.PIPE)

    item.wait()

    for line2 in item.stdout:
        output = line2.decode("utf-8")
		
		#Extract the name from the returned output
        nameStart = output.find('by')

        if nameStart < 0:
            continue
        nameStart += 3

        nameEnd = output.find("@", nameStart)
        name = output[nameStart:nameEnd]

        remove_digits = str.maketrans('', '', digits)
        name = name.translate(remove_digits)

		#Some special case handling of names that are different on our Discord
        if name == 'Niels':
            name = 'Nelis'
        elif name == 'Jens':
            name = 'Quill'
        elif name == 'Daniel':
            name = 'Kocken'

        message = name + '\n' + data[0] + '\n' + data[1]

        send(message)
        print (message + '\n---------------------------------------')

        time.sleep(0.52)

#Codeword used by the Discord Bot to know that we have send all our file-issues
send('MikuOut')

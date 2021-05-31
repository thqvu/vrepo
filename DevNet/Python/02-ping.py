import wexpect

ping = wexpect.spawn("ping localhost")
result = ping.expect([wexpect.EOF, wexpect.TIMEOUT])
print(ping.before)
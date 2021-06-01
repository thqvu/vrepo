import pexpect

ping = pexpect.spawn("ping localhost")
result = ping.expect([pexpect.EOF, pexpect.TIMEOUT])
print(ping.before)
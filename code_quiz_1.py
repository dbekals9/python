log = "User123LoggedInUSER456"

clog = log[0:4:] + log[7:19:]
l_log = clog.lower()
d_log = dict.fromkeys(l_log)

s_log = ''

for s in d_log:
    s_log += s

print(s_log)
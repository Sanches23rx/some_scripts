f = open("C:/Users/rudzs/OneDrive/Рабочий стол/УНИВЕР/6сем/Системы аутентификации ИБ/Лаб2/dns.log","r")
dns_logs = []
for line in f.readlines():
    if (line[0] == '#'):
        continue
    dns_logs.append(line.split()[9])
f.close()
f = open("C:/Users/rudzs/OneDrive/Рабочий стол/УНИВЕР/6сем/Системы аутентификации ИБ/Лаб2/allhosts","r")
allhosts = []
for line in f.readlines():
    if line[0] == '#':
        continue
    allhosts.append(line.split()[1])
f.close()
count = 0
for i in range(len(dns_logs)):
    if dns_logs[i] in allhosts:
        count += 1
print("Count: ",count)
a = count/len(dns_logs)
print("Percents: ", a)

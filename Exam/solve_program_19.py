#print the last part of the yes ip in the last loop
ips_list = [
('192.168.0.15', 'y'),
('192.168.0.22', 'y'),
('192.168.0.14', 'y'),
('192.168.0.24', 'n'),
('192.168.0.81', 'n'),
('192.168.0.11', 'y')
]
for item in ips_list:
    if item[1] == 'y':
        print(item[0], item[1])
        print(item[0][-2:])
        
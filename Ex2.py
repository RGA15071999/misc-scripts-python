dict = {'Robert': [15, 'Photon'],
     'Khazhak': [15, 'Physmath'],
     'David': [16, 'Photon'],
     'Son': [16, 'Quant'],
     'Artyom': [16, 'Quant'],
     'Tigran': [16, 'Physmath'],
     'Erik': [16, 'Physmath'],
     'Victorya': [16, 'Physmath'],
     'Hayk': [16, 'Ayb'],
     'Mels': [16, 'Ayb'],
     'Lusy': [16, 'Ayb'],
     'Hasmik': [16, 'Photon'],
     'Misha': [17, 'Photon'],
     'Vahram': [17, 'HPTH'],
     'Anna': [17, 'Photon'],
     'Naira': [17, 'Photon'],
     'Artur': [17, 'Evrika'],
     'Sona': [18, 'AUA']}
ages = []
count = 0
for i in dict:
    add = dict[i][0]
    ages.extend([add])
    count += 1
mean = 0
for i in range(0, count):
    mean += ages[i]
mean = mean/count
print 'The average age is', mean
std = 0
for i in range(0, count):
    std += pow((ages[i] - mean), 2)
std = pow((float(std) / count), 0.5)
print 'Standart Deviation is', ' ', std
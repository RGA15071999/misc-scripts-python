ann_rate = input('Choose annual rate')
while ann_rate > 1 or ann_rate < 0:
    print "ERROR: Choose number between 0 and 1"
    ann_rate = input('Choose annual rate')
mon_invt = input('How much money would you invest???')
mon_rate = ann_rate/12
amt_paid = mon_invt*12
amt_all = 0
for i in range(0, 12):
    amt_all += mon_invt + amt_all*mon_rate
    print '%0.2f' % amt_all
amt_earn = amt_all - amt_paid
print '%0.2f' % amt_earn


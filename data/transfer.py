import re
# f1 = open('./Slashdot/slashdot.txt')
# f2 = open('./Slashdot/my_slashdot.txt','w')
f1 = open('./Epinions/epinions.txt')
f2 = open('./Epinions/my_epinions.txt','w')
for s in f1.readlines():
    # s1 = s.replace('\t', '');
    s1 = map(int, list(s.split('\t')))
    s1[0] += 1
    s1[1] += 1
    s1 = map(str, s1);
    f2.write(' '.join(s1))
    f2.write('\n')
f1.close()
f2.close()

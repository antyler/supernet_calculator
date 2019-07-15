def func(d,x,i):
    if i == ('omcs-bmcs-{}-nonprod-pvtlb'.format(x)):
        d = (3*d)
        #print('anka')
    elif i == ('omcs-bmcs-{}-prod-pvtlb'.format(x)):
        d = (3*d)
        #print('adsf')
    elif i == ('omcs-bmcs-{}-nonprod-db'.format(x)):
        pass
    elif i == ('omcs-bmcs-{}-prod-db'.format(x)):
        pass
    elif i == ('omcs-bmcs-{}-nonprod-publb'.format(x)):
        d = (2*d)
        if d == 2:
            d = d+1
        #print('raman')
    elif i == ('omcs-bmcs-{}-prod-publb'.format(x)):
        d = (2*d)
        if d == 2:
            d = d+1
        #print('raman')
    else:
        d = d
        #print('cham')
    return d
def func_1(*args):
    args = list(args)
    print(args)
    o = []
    if '/29' in args[0]:
        r = args[0].count('/29')
        r = r*8
        o.append(r)
        #print(r)
    else:
        r = 0
    if '/28' in args[0]:
        s = args[0].count('/28')
        s = s*16
        #print(s)
        o.append(s)
    else:
        s = 0
    if '/27' in args[0]:
        t = args[0].count('/27')
        t = t*32
        #print(t)
        o.append(t)
    else:
        t = 0
    if '/26' in args[0]:
        k = args[0].count('/26')
        k = k*64
        #print(k)
        o.append(k)
    else:
        k = 0
    if '/25' in args[0]:
        v = args[0].count('/25')
        v = v*128
        #print(v)
        o.append(v)
    else:
        v = 0
    if '/24' in args[0]:
        w = args[0].count('/24')
        w = w*256
        #print(w)
        o.append(w)
    else:
        w = 0
    if '/23' in args[0]:
        z = args[0].count('/23')
        z = z*256
        #print(z)
        o.append(z)
    if '/22' in args[0]:
        z1 = args[0].count('/22')
        z1 = z1*512
        #print(z)
        o.append(z1)
    else:
        z = 0
    print (o)
    return sum(o)

while True:
    x = input("Customer CUST ID")
    if len(x) == 4:
        x = x.upper()
        break
    else:
        print("SORRY,Enter 4 character CUS ID")
a = "omcs-bmcs-CUST-shared-infra      /28','omcs-bmcs-CUST-shared-win        /30','omcs-bmcs-CUST-shared-webproxy   /30'," \
    "'omcs-bmcs-CUST-nonprod-sftp      /30'," \
    "'omcs-bmcs-CUST-prod-sftp         /30','omcs-bmcs-CUST-prod-fss          /29','omcs-bmcs-CUST-nonprod-fss       /29"
a = a.replace('CUST',x)
b = ['omcs-bmcs-CUST-nonprod-db','omcs-bmcs-CUST-nonprod-pvt-mt','omcs-bmcs-CUST-nonprod-pvt-win-mt','omcs-bmcs-CUST-nonprod-pub-mt', \
    'omcs-bmcs-CUST-nonprod-pvtlb','omcs-bmcs-CUST-prod-db','omcs-bmcs-CUST-prod-pvt-mt', \
    'omcs-bmcs-CUST-prod-pvt-win-mt','omcs-bmcs-CUST-prod-pub-mt','omcs-bmcs-CUST-prod-pvtlb', \
    'omcs-bmcs-CUST-nonprod-publb','omcs-bmcs-CUST-prod-publb']
count = 7
c =[]
print("")
print("PreSS '0' if particular subnet is not needed")
print("")
for i in b:
    i = i.replace('CUST',x)
    while True:
        #i = i.replace('CUST',x)
        d = int(input("Enter no. of Servers for {}".format(i)))
        t = func(d,x,i)
        if t == 0:
            break
        elif t in range(1,3):
            e='/29'   # 5-Free
            print(e)
            c.append(e)
            count += 1
            break
        elif t in range(3,9):
            e='/28'   # 13-Free
            print(e)
            c.append(e)
            count += 1
            break
        elif t in range(9,25):
            e='/27'   # 29-Free
            print(e)
            c.append(e)
            count += 1
            break
        elif t in range(25,49):
            e='/26'   # 61-Free
            print(e)
            c.append(e)
            count += 1
            break
        elif t in range(49,105):
            e='/25'   # 125-Free
            print(e)
            c.append(e)
            count += 1
            break
        elif t in range(105,214):
            e='/24'   # 253-Free
            print(e)
            c.append(e)
            count += 1
            break
        elif t in range(214,500):
            e='/23'   # 509-Free
            print(e)
            c.append(e)
            count += 1
            break
        else:
            print("Invalid IP range,SORRY")

m = input("Do you need Subnet for Exa servers:\n"
      "Press\n"
      "p - prod\n"
      "n - nonprod\n"
      "b - Both prod&nonprod\n"
      "o - NOT Required")

while True:
    if m == 'p' :
        print( "##########Final template#############" )
        print('omcs-bmcs-{}-prod-ExaDB       /27'.format(x))
        print('omcs-bmcs-{}-prod-ExaDBBkp    /28'.format(x))
        count =+ 2
        break
    elif m == 'n':
        print( "##########Final template#############" )
        print("omcs-bmcs-{}-nonprod-ExaDB     /27".format(x))
        print("omcs-bmcs-{}-nonprod-ExaDBBkp  /28".format(x))
        count =+ 2
        break
    elif m == 'b':
        print( "##########Final template#############" )
        print("omcs-bmcs-{}-nonprod-ExaDB     /27".format(x))
        print("omcs-bmcs-{}-prod-ExaDBBkp     /28".format(x))
        print("omcs-bmcs-{}-prod-ExaDB        /27".format(x))
        print("omcs-bmcs-{}-nonprod-ExaDBBkp  /28".format(x))
        count = + 4
        break
    elif m == 'o':
        print( "##########Final template#############" )
        break
    else:
        print("Invalid entry, please re-enter")


print("")
#print(a.replace("','",'\n'))

myDict = {k:v for (k,v) in zip(b,c)}
for k,v in myDict.items():
    k = k.replace('CUST', x)
    print (k,v)
    i = i.replace('CUST',x)
#print(c)  #### prints main template
print("---------------------")
print("")
print(a.replace("','",'\n'))

r = func_1(c)
r = int(r)
print('Total IP for new subnet :',r)
r = r+48
print("Total IPs after above subnet allocation, New + Core::", r)
print("")
var = input("Please Calculate and enter how much extra IPs you want in the supernet(numbers are by default in *percentage) - 15, 20, 25, 30::")

if var == '10':
    r = int( 115/100*r)
elif var == '15':
    r = int(120/100*r)
elif var == '20':
    r = int(120/100*r)
elif var == '25':
    r = int(125/100*r)
elif var == '30':
    r = int(130/100*r)
else:
    r = int(120/100*r)


print("Total Ips after extra {} addition:: ".format(var),r)

if r in range(1,9):
    print('Required supernet   /29')
elif r in range(9,17):
    print( 'Required supernet  /28')
elif r in range(17,33):
    print( 'Required supernet  /27')
elif r in range(33,65):
    print('Required supernet   /26')
elif r in range(65,129):
    print( 'Required supernet  /25')
if r in range(129,257):
    print('Required supernet   /24')
elif r in range(257,513):
    print('Required supernet   /23')
elif r in range(513,1025):
    print('Required supernet   /22')
elif r in range(1025,2049):
    print('Required supernet   /21')
elif r in range(2049,4097):
    print('Required supernet   /20')
else:
    print('Supernet of size (/19 or +8192 IPs) needs approval of higher authority')











'''
z = ''
z=z.join(c)
print(z)
if '/29' in z:
    z.replace('/29','8')
    print('hi',z)
'''
'''
while True:
    if m == p:
        print('omcs-bmcs-{}-prod-ExaDB       /27'.format(x))
        print('omcs-bmcs-{}-prod-ExaDBBkp    /28'.format(x))
        count =+ 2
    elif m == n:
        print("omcs-bmcs-{}-nonprod-ExaDB     /27".format(x))
        print("omcs-bmcs-{}-nonprod-ExaDBBkp  /28".format(x))
        count =+ 2
    elif m == 'np':
        print("omcs-bmcs-{}-nonprod-ExaDB     /27".format(x))
        print("omcs-bmcs-{}-prod-ExaDBBkp     /28".format(x))
        print("omcs-bmcs-{}-prod-ExaDB        /27".format(x))
        print("omcs-bmcs-{}-nonprod-ExaDBBkp  /28".format(x))
        count = + 4
    elif m == x:
            break
    else:
        print("Invalid entry, please re-enter")

print("Total no. of subnets:",count)
'''







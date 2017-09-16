text = open("words.txt","r")
mytext=text.read().strip().replace('\n','')
mytext=mytext.strip().replace('\ufeff','')
#with open('words.txt') as f:
#    mytext = [line.rstrip('\n') for line in f]
test = []
alist = []
def frequency(x):
    new_text = x.split(" ")
    number = -1
    for i in new_text:          
        if i not in alist:
            #test[i[1]]+=1
            number+=1
            #test["i"] = number
            test.append([i,number])
            alist.append(i)
        else:
            alist.append(i)
    print (alist)
    for j in test:
        print()
        print(j[0],j[1],alist.count(j[0]))         
frequency(mytext)


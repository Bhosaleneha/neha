test_str="missippi"
count=0
count1=0
count2=0
count3=0
for x in test_str:
   if x=='i':
      count=count+1
   elif x=='s':
      count1=count1+1
   elif x=='p':
      count2=count2+1
   else:
      count3=count3+1
 print("i="+str(count))
 print("s="+str(count1))
 print("p="+str(count2))
 print("m="+str(count3))

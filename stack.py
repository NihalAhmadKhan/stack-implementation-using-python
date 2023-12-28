#PRORAM TO IMPLEMENT STACK USING LIST
l=[]
while True:
  c=int(input(
      '''
   Choose An Operation
   1. Push Elements
   2. Pop Elements
   3. Peek Elements
   4. Display Stack
   5. Exit

      '''
  ))
  if c==1:
    n=input("\n\nEnter The Value :")
    l.append(n)
    print(l,"\n")
  elif c==2:
    if len(l)==0:
      print("\nEmpty Stack")
    else:
      p=l.pop()
      print(p)
      print(l)
  elif c==3:
    if len(l)==0:
      print("Empty Stack")
    else:
      print("Last Stack Element",l[-1])
  elif c==4:
    print("Displaying stack",l)
  elif c==5:
    break
  else:
    print("Invalid Input")

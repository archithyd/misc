def swap(st,j):
    lis1=st.split()
    print(lis1)
    temp=lis1[j]
    lis1[j]=lis[1]
    lis1[1]=temp
    return "".join(lis1)



lis2=[]
for i in range(int(input())):
    num1, num2=map(int, input().split())
    lis="bb"
    for j in range(num1-2):
        lis+=("a")
    lis2.append(lis)
    dupli = lis
    for j in range(2,num1):
        lis2.append(swap(dupli,j))

print(lis2)

"""curr1=l1
        curr2=l2
        curr1_1val=0
        curr2_2val=0
        while curr1!=None:
            curr1_1val+=1
            curr1=curr1.next
        while curr2!=None:
            curr2_2val+=1
            curr2=curr2.next
        ans=0
        while curr1!=None and curr2!=None:
            if curr1_1val>curr2_2val:
                if curr1.val+curr2.val>=10:
                    if curr1.next==None or curr2.next==None:
                        newnode=ListNode(0)
                        curr1.next=newnode
                    curr1.val=(curr1.val+curr2.val)%10
                    curr1.next.val+=1
                else:
                    curr1.val=(curr1.val+curr2.val)
                ans=l1
            else:
                if curr1.val+curr2.val>=10:
                    if curr1.next==None or curr2.next==None:
                        newnode=ListNode(0)
                        curr2.next=newnode
                    curr2.val=(curr1.val+curr2.val)%10
                    curr2.next.val+=1
                else:
                    curr2.val=(curr1.val+curr2.val)
                ans=l2
            curr1=curr1.next
            curr2=curr2.next
        """
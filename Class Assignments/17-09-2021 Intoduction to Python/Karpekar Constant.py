'''PROGRAM DESCRIPITON: 1) Take a 4 digit number non-repeating number and arrange it in ascending and descending order to get two new numbers.

                        2) Then subtract the highest number from lower number till you get the number 6147.

                        3) If the end result is 6147 then return TRUE else FALSE.
 '''

# PROGRAMMED BY: PULI SNEHITH REDDY
# MAIL ID : snehithreddyp@gmail.com
# DATE    : 17-09-2021
# VERSION : 3.7.9
# CAVEATS : None
# LICENSE : None

n=int(input())
res=[]
while(1):
    n=list(str(n))
    a1=sorted(n)
    s="".join(a1)
    n=int(s[::-1])-int(s)
    print("Greatest number:",s[::-1])
    print("Smallest number:",s)
    print("Difference:",n)
    print("-------------------------")
    if n in res:
        print("FALSE")
        break
    if n==6174:
        print("TRUE")
        break
    res.append(n)
    
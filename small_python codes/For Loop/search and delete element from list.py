q = []
c = 1
for i in range(5):
    a = int(input(f"No. {c} : "))
    q.append(a)
    c +=1
print(q)
d = int(input("Enter a number to find and delete from List : "))
q.remove(d)           # delete user element from list
print(q)



Output:

No. 1 : 1
No. 2 : 2
No. 3 : 3
No. 4 : 4
No. 5 : 5
[1, 2, 3, 4, 5]
Enter a number to find and delete from List : 2
[1, 3, 4, 5]

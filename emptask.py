emp={'eno':[1,2,3],'ename':['A','B','C'],'esal':[1000,2000,3000]}
print("\n the employee datset is:")
print(emp)
print("-------------------------------------------------")
print("\n the employee name are:",emp['ename'])
print("-------------------------------------------------")
print("\n the employee sal;aries are:")
print("-------------------------------------------------")
for i in emp['esal']:
    print(i)

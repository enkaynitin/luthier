print ("All units in Thousands.")

fa = input("Fixed Assets :")


r = input("Rent :")
oex = input("Other expenses such as electricity bills, etc :")

m = input("No. of employee :")
salary = input("Enter Salary of employee :")
maint = input("Enter maintainance cost :")

def running_cost():
	run_c = r + oex  + m*salary + maint
	print ("Monthly rent, bills, salary, maintainance : {0}".format(run_c))
	print ("Running cost with buffer for 3 months : {0}".format(run_c * 3))


g = input("Enter no. of guitars :")
u = input("Enter no. of ukulele :")


gm = input("Enter material cost of guitar :")
um = input("Material cost of Ukulele :")


us = input("Enter selling price of ukulele :")
gs = input("Enter selling price of guitar :")




diff_selling_and_material = (g*gs + u*us ) - (g*gm + u*um )
p = (diff_selling_and_material - m * salary - r - oex - maint)

print ("Monthly profit to company : %d" %p)

for n in range(12): 
	print ("Profit to company after {0} month : {1}".format(n, p * n))

print ("Yearly profit to company : %d" %(12*p))

running_cost()






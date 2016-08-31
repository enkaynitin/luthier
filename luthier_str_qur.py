print ("All units in Thousands.")

fa = input("Fixed Assets :")


r = input("Rent :")
oex = input("Other expenses such as electricity bills, etc :")
maint = input("Enter maintainance cost :")

l = input("No. of luthiers :")
salary = input("Enter Salary of each luthier :")


def running_cost():
	run_c = r + oex  + l*salary + maint
	print ("Monthly rent, bills, salary, maintainance : {0}".format(run_c))
	print ("Running cost with buffer for 3 months : {0}".format(run_c * 3))


v1 = input("Enter no. of violin1 :")
v2 = input("Enter no. of violin2 :")
va = input("Enter no. of viola :")
cel = input("Enter no. of cello :")

v1m = input("Enter material cost of violin1 :")
v2m = input("Enter material cost of violin2 :")
vam = input("Enter material cost of viola :")
celm = input("Enter material cost of cello :")

v1s = input("Enter selling price of violin1 :")
v2s = input("Enter selling price of violin2 :")
vas = input("Enter selling price of viola :")
cels = input("Enter selling price of cello :")


diff_selling_and_material = (v1*v1s +v2*v2s +va*vas + cel*cels ) - (v1*v1m + v2*v2m +va*vam + cel*celm)
p = (diff_selling_and_material - l * salary - r - oex - maint)

print ("Monthly profit to company : %d" %p)

for n in range(12): 
	print ("Profit to company after {0} month : {1}".format(n, p * n))

print ("Yearly profit to company : %d" %(12*p))

running_cost()






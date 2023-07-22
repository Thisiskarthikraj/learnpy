# String with special characters 
special_string=input("enter a string :")
print("String before conversion: ",special_string)
# Create a list with normal characters using the isalnum() method
# use the join() function to convert the list to string
normal_string="".join(ch for ch in special_string if ch.isalnum())
# print the normal string 
print("string after conversion:",normal_string)
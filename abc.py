code
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

output
Input the Filename: abc.py
The extension of the file is : "python"

#Opens the file for reading, reads the data in, replaces space with empty set to keep it clean
# and splits the data based on the line 
file=open("rush2.csv","r",encoding='latin-1')
data=file.read()
data=data.replace(" ", "")
#data=data.split("\n")

print (data)

for line in range(1,len(data)):
	
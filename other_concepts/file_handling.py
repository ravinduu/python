data_file = open("data.txt","r") 				#open file and save it in variable, "r" is for read file
print(data_file.read()) 						#print content in file.

write_to_file = open("write.txt","w") 			#open file for write data "w" is for write
write_to_file.write("Hello")

file1 = open("write.txt","a")					#"a" is for append
file1.write(" World!")

#"rb" for read binary
#"wb" for write binary

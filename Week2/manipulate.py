##open text files
with open('cool_docs.txt','r') as cool_docs:
    read_file=cool_docs.read()
print(read_file)


# with open('cool_docs.txt','r') as cool_docs:
#     read_file=cool_docs.readlines()
# for list in read_file:
#     print(list)

with open('cool_docs.txt','w') as cool_docs:
    write_file=cool_docs.write('i am okay')
print(write_file)
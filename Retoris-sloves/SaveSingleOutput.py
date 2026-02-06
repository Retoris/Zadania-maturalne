def SaveSingleOutput(output):
    filename = input("Give a name for yours file: ")
    with open(filename,'wt',newline='\n',encoding='utf-8') as outfile:
        outfile.write(output)
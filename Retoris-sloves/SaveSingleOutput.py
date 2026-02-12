def SaveSingleOutput(filename,output):
    with open(filename,'wt',newline='\n',encoding='utf-8') as outfile:
        if type(output) is int:
            output = str(output)
        outfile.write(output)
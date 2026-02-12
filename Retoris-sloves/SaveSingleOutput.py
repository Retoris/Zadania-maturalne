def SaveSingleOutput(filename,output):
    with open(filename,'wt',newline='\n',encoding='utf-8') as outfile:
        outfile.write(output)
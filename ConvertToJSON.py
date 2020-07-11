
def parse(input,output,start,order):
    argument=""
    SpaceExist=False
    OneArgumentExist=False

    i=start
    while i<len(input):
    #for i in range(start,len(input)):
    
        #debug
        find="More information from this agent"
        if (input[i:i+len(find)]==find):
            debug=0

        if input[i]==":":
            output=output+"\""+argument+"\""+":"
            argument=""
            OneArgumentExist=True
            
        elif input[i]=='\n':
            if SpaceExist==False:
                if order==0: #GO DEEPER INTO THE LOOP
                    #output=output+"\""+argument+"\""+":,"
                    if len(argument)==0:
                        output=output+"{"
                    else:
                        output=output+"\""+argument+"\""+":{"
                        argument=""
                    i,output=parse(input,output,i+1,1)
                    
                else:   #GO OUT OF THE LOOP
                    if (OneArgumentExist):
                        output=output[:-1]+"},"
                        return (i-len(argument)-1,output)
                    else:
                        if output[-15:-3]!="Key features" and output[-19:-3]!="Full description" and len(argument)>40:
                            output=output[:-7]+argument+"\""+":"+"\""+"\""+"},"
                            return (i,output)
                        elif (argument=="More information from this agent"):
                            #output=output[:-2]+","+"\""+argument+"\""
                            #return (i,output)
                            output=output[:-1]+"},"
                            return (i-len(argument)-1,output)

                        else:
                            output=output+"\""+argument+"\""+":"+"\""+"\""+"},"
                            return (i,output)
            else:
                output=output+"\""+argument+"\""+","
                argument=""
                SpaceExist=False

        else:
            if (input[i-1:i+1]!=": "):
                argument=argument+input[i]
            else:
                donothing=0

        if i<len(input):
            if input[i:i+2]==": ":
                SpaceExist=True
        i=i+1
    if (order==1):
        output=output+"\""+argument+"\""+":"+"\""+"\""+"}"
        argument=""
    else:
        if (argument==""):
            output=output+"}"
        else:
            output=output+"\""+argument+"\""+"}"
        
    return (len(input),output)
    
if __name__ == '__main__':
    input="Letting information:\nFurnishing: Unfurnished\nLetting type: Long term\nReduced on Rightmove: 07 November 2019 (30 days ago)\nKey features\nParking Space for Rent Gated Development Great location Easy access to transport links Good road connections\nFull description\nLONG LET. This Parking Space for rent is situated within a gated development in Wandsworth offering fantastic connections to the A4, A3 and South Circular.\n\nMerton Road is situated within easy reach of Wandsworth Town station (National Rail) and East Putney station (District Line) with easy access in and out of Central London via the A3.\n\nMore information from this agent\nProperty details\nSuper sized images"
    output="{"
    a=parse(input,output,0,0)
    print(a[1])
     

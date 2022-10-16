
#Add function
def add(list_of_operands):
      #print(list_of_operands)
      checking=check(list_of_operands)           #calling check()function to check if enough operands are given
      if checking!=0:                           #checking!=0 implies to 'if eoungh operands are give'
            total_sum=0
            for operand  in list_of_operands:
                total_sum+=operand
            return(total_sum)
      else:
           return 0
      

#Subtract function
def subtract(list_of_operands):
      checking=check(list_of_operands)
      if checking!=0:   
              total_difference=0
              for operand in list_of_operands:
                  total_difference-=operand
              return(total_difference)
      else:
            return 0
#Multiplication function
def multiplication(list_of_operands):
      checking=check(list_of_operands)
      if checking!=0:   
            total_product=1
            for operand in list_of_operands:
                  total_product*=operand
            return(total_product)
      else:
            return 0
#Division function
def division(list_of_operands):
      #print(list_of_operands)
      checking=check(list_of_operands)
      if checking!=0:   
            total_division=list_of_operands[0]
            length=len(list_of_operands)
            for i in range(1,length,1):
                  total_division/=list_of_operands[i]
            return(total_division)
      else:
            return 0
#Greatest Number fucntion
def greatest_number(list_of_operands):
      greatest=list_of_operands[0]
      for index in range(1,len(list_of_operands),1):
       number2=list_of_operands[index]
       if greatest>number2:
             pass
       else:
             greatest=number2
      return greatest
#Smallest Number function
def smallest_number(list_of_operands):
      smallest =list_of_operands[0]
      for index in range(1,len(list_of_operands),1):
       number2=list_of_operands[index]
       if smallest<number2:
             pass
       else:
             smallest=number2
      return smallest

#HCF funtion
def HCF(list_of_operands):
      checking=check(list_of_operands)
      if checking !=0:
            H=smallest_number(list_of_operands)     
            length=len(list_of_operands)
            while H>=1:
                  count=0
                  for i in range(length):
                        
                        if list_of_operands[i]%H==0:
                              count+=1
                        else:
                              break
                  if count==length:
                             # print("Chalyo")
                              return H
                  H-=1
      else:
            return 0
      
#LCM function      
def LCM(list_of_operands):
      checking=check(list_of_operands)
      if checking!=0:                   
            L=1
            length=len(list_of_operands)   
            limit=list_of_operands[0]
            for i in range(1,length,1):
                  limit*=list_of_operands[i]
            while L<=limit:
                  count=0
                  for i in range(length):
                        if L%list_of_operands[i]==0:
                              count+=1
                  if count==length:
                        return L
                  L+=1
      else:
            return 0
      

def Exit():
      exit()         #for users,to close the program
def sorry():
     print("Sorry,not able to recognise the operation")
def help():
     print("(i)FUNCTIONS of SmartCalcu:","   Addition","   Subtraction","   Multiplication",
           "   Division","   Greatest Number","   Smallest Number","   HCF","   LCM",sep="\n")
     
     print("(ii)INFORMATIONS:","   Type 'exit','end' or 'close' to close the SmartCalcu",sep="\n")
     
def check(list_of_operands):
      if(len(list_of_operands)<2):
            return 0

      
#Function to select the operation to be performed            
def operation(list_of_word,list_of_operands):
            dict_of_commands={"exit":Exit,"close":Exit,"end":Exit,"help":help,"sorry":sorry}
            dict_of_operations={"add":add,"addition":add,"sum":add,"plus":add,"+":add,"subtract":subtract,"subtraction":subtract,
                        "minus":subtract,"-":subtract, "product":multiplication,"multiply":multiplication,"multiplied":multiplication,
                        "multiplication":multiplication,"*":multiplication,"divided":division,"division":division,"divide":division,"/":division,
                        "greater":greatest_number,"greatest":greatest_number,"largest":greatest_number,"larger":greatest_number,
                        "largest":greatest_number,"maximum":greatest_number,"smaller":smallest_number,"smallest":smallest_number,
                        "lesser":smallest_number,"least":smallest_number,"minimum":smallest_number,
                        
                        "hcf":HCF,"gcd":HCF,"lcm":LCM,}
            count=0
            length=len(list_of_word)
           # print("Length=",length)
            #print(list_of_word) print(list_of_operands)
            if list_of_operands!=[]:          #first if else block
                        while 1:     
                                    try:
                                      for word in list_of_word:
                                          result=dict_of_operations[word](list_of_operands)
                                         # print("try",word)
                                          if result==0:
                                             print("Not enough operands")
                                             break
                                          else:
                                             print("Result=",result)
                                             break
                                  
                                    except:
                                          count+=1
                                          list_of_word.remove(word)
##                                          print("list:",list_of_word)
##                                          print("count:",count)
##                                          print("Length:",length)
                                    else: 
                                          break

                        if count==length:
                             dict_of_commands["sorry"]()       #print("Sorry,not able to do this operation")

            #first if else block
            else:
                        while 1:
                              try:                               #parent try-except block to know if any commands are given
                                  for word in list_of_word:             
                                          dict_of_commands[word]()               
                              except:
                                    try:                                 #child try-block to know if any random words given without operands
                                          dict_of_operations[word]    
                                    except:
                                          dict_of_commands['sorry']()
                                          break
                                    else:
                                          count+=1
                                          list_of_word.remove(word)
                              else:
                                    break

                        if(count==length):
                            print("No operands")                  #if no operands are given for the defined operands
       
def  extract_operator_word(): 
      instruction=input()
      ins=[x for x in instruction.split(" ")]
      length_of_ins=len(ins)
      #print(length_of_ins)
      count=0
      list_of_operands=[]
      list_of_word=[]
      
      while(1)   :
            try: 
               for string in ins:
                   count+=1
                   #print(type(string))
                   operand=float(string)
                   list_of_operands.append(operand)
                  
                   #ins.remove(string)

                   if(count==length_of_ins):
                             break
                   ins.remove(string)
               if(count==length_of_ins):
                        break
                  
            except:
                    #print("exception:",string)
                    ins.remove(string)
                    string=string.lower()
                    list_of_word.append(string)
                    
                        
##      print(ins)
##      print("List of Word:",list_of_word)
##      print("List of Operands:",list_of_operands)
      result=operation(list_of_word,list_of_operands)
      
def main():
      responses=["Hi,welcome to SmartCalcu....","Enter the instructions:"]
      print(responses[0],responses[1],sep="\n")
      while True:
             extract_operator_word()
             print("\ncontinue..")
            
main()

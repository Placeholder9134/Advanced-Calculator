class output: 
  equation = [] 
  lStart = 0 
  lEnd = 0 
  rStart = 0 
  rEnd = 0 

def rightNum(DS, x):
  start = x + 1
  end = start 

  while True:
    print(DS.equation)
    print(end)
    if DS.equation[end] == "+" or DS.equation[end] == "-" or  DS.equation[end] == "/" or DS.equation[end] == "*":
      print("The right Number is: " + str(DS.equation[start:end]))
      DS.rStart = start
      DS.rEnd = end
      return DS.equation[start:end]

    if DS.equation[end] == DS.equation[len(DS.equation) - 1]:
      print()
      print("The right Number is: " + str(DS.equation[start:end+1]))
      DS.rStart = start
      DS.rEnd = end
      return DS.equation[start:end+1]
      
    end += 1
    
# Two Cases: 
# ----------------------------
# First Case: The number you are trying to get is at the beginning of the list. 
# pos =  0 1 2  3 4 
# 1.)   [5,0,0, + 1]
# How did you know if the number is 500 and not 5001? 

# Other Case: If the number is NOT at the beginning of the list. 
# pos =  0. 1. 2. 3. 4. 5. 6
# 2.)   [5, +, 5, 0, 0, *. 6]
# How did you know the number was 500? and not 5006?
# start on the position of the math sign you found and keep going left until you hit a symbol.

def leftNum(DS, x):
  index = x
  end = index # save spot for end equation[?:end]
  while True:
    index -= 1
    if(index==0):
      break
      
    if DS.equation[index] == "+" or DS.equation[index] == "-" or  DS.equation[index] == "/" or DS.equation[index] == "*":
      index +=1
      
      break

  start = index
  DS.lStart = start
  DS.lEnd = end-1
  print("The left Number is: " + str(DS.equation[start:end]))
  return DS.equation[start:end]

# What can we utilize in order to create our new equation from our old equation? 
# Previously, we relied on the fact that the numbers were going to be in single digits.. 
# hint: getLeftNum and getRightNum can help us..

# 4.) 
#   newList = []
#   for x in range(len(DS.equation)):
#      if x < leftNumStart and x > leftNumEnd: 
#          newList.append(DS.equation[x])

#   0
# [4500]

# if (x < lStart or x > lEnd) and (x < rStart or x > rEnd): 
# lStart = 3 
# lEnd = 4 
# x = 6
#  0 1 2 3 4 5 6 7
# [5,0,+,4,0,*,9,0]
# [5,0,+,3600,]

def update(DS,answer,x): # This was entirely based on single digit numbers.
  print("Entered update")
  newList = []
  print("Leftnum start: " + str(DS.lStart))
  print("Leftnum end: " + str(DS.lEnd))
  print("Rightnum start: " + str(DS.rStart))
  print("Rightnum end: " + str(DS.rEnd))
  
  for i in range(len(DS.equation)):
  # 0 1 2 3 4 5 6 7
    if i == x:
      newList.append(answer)
    elif i < DS.lStart or i > (DS.rEnd): 
      newList.append(DS.equation[i]) # now i here represents the positions, do we insert position into the new equation? o.O
  # set points of lstart and rend, if it is not between it then include it. Remove everything between lstart and rend and replace it with your answer.
    
  
  #  0 1 2 3 4 5 6 7
  # [5,0,+,4,0,*,9,0]
  # [5,0,+,9,0] -> [5,0,+,9] || error 
  # y = 1
  # x = 5

  print("This is our new equation: " + str(newList))
  


  # The main functionality you need to think about is, how can we use 
  # len of the leftnum? Ex: if it's 4. 
  # we need to go from 1,2,3,4 and pop those. 
  
  
  # try using 
  # x-len(leftNum):x
  # x:x+len(rightNum)
  return newList
  

# use the length of leftNum, go left that number of times from x then stop. Pop this and do the same with rightNum.

# 1.) The numbers are arbitrary, length unknown. 
# 2.) We identify the indexes of the left and right num? 
# 3.) Within our leftNum and rightNum functions. 



def convertToFloat(fakeNum): # convert the list full of numbers into a float 
  # 1.) Create a for loop to go through each element one by one  
  # 2.) In each loop, concatenate the element into a tmpvar. 
  # 3.) Once the loop completes, convert the tmpvar into a float data type. 
  # 4.) Return tmpvar
  # fakeNum = ["2", "0", "0"]
  something = ""
  for i in fakeNum:
    something += str(i)
  something = float(something)
  return something

def main(): 
  DS = output()
  
  equation = input("Please input your equation: ") # It automatically stores everything as a string. 
  DS.equation = list(equation)
  restartFlag = True 
  # As long as you do not reach the end of the list and both flags are not True. 
  while (restartFlag == True or restartFlag == True):
    for x in range(len(DS.equation)):
      if DS.equation[x] == "*":
        leftNumber = leftNum(DS, x)
        rightNumber = rightNum(DS,x)
        multiplicationAnswer = convertToFloat(leftNumber) * convertToFloat(rightNumber)
        DS.equation = update(DS,multiplicationAnswer,x)
        restartFlag = True
        break
      else: 
        restartFlag = False

      if DS.equation[x] == "/":
        leftNumber = leftNum(DS, x)
        rightNumber = rightNum(DS,x)
        divisionAnswer = convertToFloat(leftNumber) / convertToFloat(rightNumber) 
        DS.equation = update(DS,divisionAnswer,x)
        restartFlag = True
        break 
      else: 
        restartFlag = False
  
  restartFlag = True # restartFlag will turn into False prior to this point since we exited out of the while loop above which only exits if restartFlag is False

  while (restartFlag == True or restartFlag == True):    
    for x in range(len(DS.equation)):
      if DS.equation[x] == "+":
        leftNumber = leftNum(DS, x)
        rightNumber = rightNum(DS,x)
        additionAnswer = convertToFloat(leftNumber) + convertToFloat(rightNumber)
        DS.equation = update(DS,additionAnswer,x)
        restartFlag = True
        break
      else: 
        restartFlag = False

      if DS.equation[x] == "-":
        leftNumber = leftNum(DS, x)
        rightNumber = rightNum(DS,x)
        subtractAnswer = convertToFloat(leftNumber) - convertToFloat(rightNumber)
        DS.equation = update(DS,subtractAnswer,x)
        restartFlag = True
        break 
      else: 
        restartFlag = False
  print(DS.equation)



if __name__ == "__main__":
  main()

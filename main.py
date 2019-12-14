import random
import color


#Note that this code is only for the statistics project therefore, I did not want to do any extra worlk
#Code currently only works for 2 trials because the value that is stored is set to 1-2. If you would want to conduct more trials. You must add a new value variable named Value3, Value4, etc and append the digits. As for the amount of people will be unlimited. 

#-Idea to fix the variable would be to string splice every data value after the 10th digit and print the values or append them.


Ask = input("Part A or B?")


if Ask == "A":
  def t(Time):
    print ("\n\n\n\n\nPart [A]")
    for H in range (Time):
      DiceT(Rolls,H,TMeans)
    print("----------------------------------------------------------------------------------------------")
    TotalMeans(TMeans)



  def DiceT(Rolls,H,TMeans):

    for R in range (1,N+1):
      print (("__________________________\n\n"),(color.blue)("[Trial"), (color.yellow)(H + 1),(color.blue)("]"),("\n__________________________"))
      List = []

      for D in range (Rolls):
        print ("Rolls: ", D + 1)
        Side = random.randrange(0,10)
        for I in range (0,15):
          Side = random.randrange(0,10)

          List += str(Side)
          print ("Person#",I+1, ":", Side)
        Value1 = []
        Value2 = []
        print ("")
        
      for S in range (0,15):
        Value1.append(List[S])

      for NewDig in range (15,30):
        Value2.append(List[NewDig])
        

      print ("Results for Trial:")
      print (Value1)
      print (Value2)

      V = []
      for FV in range (0,15):
        V.append((Value1[FV]) + (Value2[FV]))

      print (V)

      V = [w.replace('00', '100') for w in V]
      print (V)

    
      
      V = list(map(int, V))

      Combined = 0
      Mean = 0
      for M in range (0,15):
        Combined += V[M]
        Mean = Combined/15
      
      TMeans.append(Mean)
      print (Mean)

  def TotalMeans(TMeans):
    AverageMean = 0
    print ("Total means:\n")
    TMeans = list(map(float, TMeans))
    for TM in range (0,15):
      print(TMeans[TM])
      AverageMean += ((TMeans[TM])/15)
    print ("The average mean for every trial(15) is: ", AverageMean)
      



  #If the value for V is equal to 0, calculate the value as 100. 


  TMeans = []
  Rolls = 2
  N = 1
  Time = 15
  t(Time)


  """
  Rolls = int(input("How many rolls would you like to conduct?"))
  N = int(input("Enter 1"))
  Time = int(input("How many times do you want to run this?"))
  t(Time)
  """

  #Input 15 for times because the python space does not allow it to exceed to 30.
elif Ask == "B":
  def t(Time):
    print ("\n\n\n\n\nPart [B]")
    for H in range (Time):
      DiceT(Rolls,H,TMeans)
    print("----------------------------------------------------------------------------------------------")
    TotalMeans(TMeans)



  def DiceT(Rolls,H,TMeans):

    for R in range (1,N+1):
      print (("__________________________\n\n"),(color.blue)("[Trial"), (color.yellow)(H + 1),(color.blue)("]"),("\n__________________________"))
      List = []

      for D in range (Rolls):
        print ("Rolls: ", D + 1)
        Side = random.randrange(0,10)
        for I in range (0,15):
          Side = random.randrange(0,10)

          List += str(Side)
          print ("Person#",I+1, ":", Side)
        Value1 = []
        Value2 = []
        print ("")
        
      for S in range (0,15):
        Value1.append(List[S])

      for NewDig in range (15,30):
        Value2.append(List[NewDig])
        

      print ("Results for Trial:")
      print (Value1)
      print (Value2)

      V = []
      Value1 = list(map(int, Value1))
      Value2 = list(map(int, Value2))


      for FV in range (0,15):
        if Value1[FV] < Value2[FV]:
          Value1 = list(map(str, Value1))
          Value2 = list(map(str, Value2))
          V.append((Value2[FV]) + (Value1[FV]))
        else:
          Value1 = list(map(str, Value1))
          Value2 = list(map(str, Value2))
          V.append((Value1[FV]) + (Value2[FV]))

      print (V)

      V = [w.replace('00', '100') for w in V]
      print (V)

    
      
      V = list(map(int, V))

      Combined = 0
      Mean = 0
      for M in range (0,15):
        Combined += V[M]
        Mean = Combined/15
      
      TMeans.append(Mean)
      print (Mean)

  def TotalMeans(TMeans):
    AverageMean = 0
    print ("Total means:\n")
    TMeans = list(map(float, TMeans))
    for TM in range (0,15):
      print(TMeans[TM])
      AverageMean += ((TMeans[TM])/15)
    print ("The average mean for every trial(15) is: ", AverageMean)
      



  #If the value for V is equal to 0, calculate the value as 100. 


  TMeans = []
  Rolls = 2
  N = 1
  Time = 15
  t(Time)


  """
  Rolls = int(input("How many rolls would you like to conduct?"))
  N = int(input("Enter 1"))
  Time = int(input("How many times do you want to run this?"))
  t(Time)
  """

  #Input 15 for times because the python space does not allow it to exceed to 30.


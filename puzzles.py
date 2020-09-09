 print("**** Welcome to my game : Puzzles ****")





# player vales




Health = 100




bottle = 100




thirst = 100








name = input("Enter your name:")




print("Hello," +name)




age = input("Enter your age:")




if int(age) >=16:




  print("Great")  




else:




  print("Too young kiidzz")




want_to_play = input("Do you want to play? yes or no:")




if want_to_play == "yes":




    print("Great")




else:




  print("Bye")




  












print("your health is "+str(Health))








#Level one




print("***# Alright Level One #***")




print("Empty set and empty street")




level_one = input("Empty Home do you want to enter?:")




if level_one == "yes":




  print("U entered the home")




  print("U found a health kit: health +10")




  Health = Health + 10




  print(Health)




else:




  print("......you walked down the road.")  








print("..you see a lake...")




sublevel_one = input("Do you want to drink the water?")




if sublevel_one == "yes":




  print("you filled water bottle.")




  




  print("your boolter is filled : " +str(bottle ))




else:




  print("you thinking where do you go from here...")




  thirst = thirst - 25




  print("minus 25 to your thirst")




  print(thirst)




  print("you feel thirsty")




  




ans = input("You notice a river and a village. Which do you go (river/village? :)")




if ans =="village":




  print("you goto the village but the people domt like you you lose 10 health")




  Health -= 10




  print(Health)




else:




  print("you reach a river at the start of the lake..")












if Health <= 0:




    print("wasted").upper() 




else:




    print("You LIVE.")  





# usain bolt, me and shah rukh khan ran a race..
# Surprisingly Usain came first.,me second and Shah rukh third
# Make func.s that give the results to the world

def position(athlete):
    if athlete=='usain':
        print("1st")
    elif athlete=='me':
        print("2nd")
    elif athlete=='srk':
        print("3rd")
    else:
        print(athlete)
        print("did not participated in the race.. Where the heck was hr?/")

print("Enter athlete's name: ")
runner=input()
position(runner)



#another way using dictionaries
# podium={ 'usain':'1st', 'me':'2nd' , 'srk':'3rd'}
# def position(athlete):
   # print(podium[athlete])
     

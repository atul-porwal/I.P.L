import random
def bolling(user_team,opponent_team):
	player=user_team
	score_list=[0,0,0,0,0,0,0,0,0,0]
	deliveries_of_balls=['yorker','bounce','shortpitch','googly','offspin','carrom ball','knuckle ball']
	w=0
	total_runs=0
	conditions=[1,2,3,4,'w',6]
	for over in range(1,7):
		print('Over',over)
		present_boller=random.choice(player)
		print("Baller",present_boller)
		print("Batsman:",opponent_team[0],"&",opponent_team[1])
		for ball in range(1,7):
			print('Select your ball',','.join(deliveries_of_balls),ball*"*")
			user=input()
			condition=random.choice(conditions)
			if condition == 'w':
				w+=1
				print(opponent_team[0]+':out',score_list[0])
				opponent_team.pop(0)
				score_list.pop(0)
				print("Batsman",opponent_team[0],"&",opponent_team[1])

			elif condition%2==1:
				score_list[0]+=condition
				print (opponent_team[0],score_list[0])
				print(opponent_team[1],score_list[1])
				total_runs+=condition
				opponent_team[0],opponent_team[1]=opponent_team[1],opponent_team[0]
				score_list[0],score_list[1]=score_list[1],score_list[0]
			else:
				score_list[0]+=condition
				print(opponent_team[0],score_list[0])
				print(opponent_team[1],score_list[1])
				total_runs+=condition
		print("score",total_runs,w,"complete over:",over)
	return(total_runs)
def batting(_userteam,_opponentteam):
	player=_userteam
	score_list=[0,0,0,0,0,0,0,0,0,0,0]
	deliveries_of_balls=['yorker','bounce','shortpitch','googly','offspin','carrom ball','knuckle ball']
	player_choice=['Hit','Defence','Helicopter shot','offcut','legcutt','flip shot','Back shot']
	conditions=[1,2,3,4,'w',6]
	overs=5
	w=0
	total_runs=0
	for over in range(1,overs+1):

		print('Over:',over)
		present_boller=random.choice(_opponentteam)

		print("Baller:",present_boller)
		print("Batsman:",player[0],player[1])
		for ball in range(1,7):
			# print(ball*"*")
			delivery=random.choice(deliveries_of_balls)
			print("This is ",delivery,ball*"*")
			print("Tell your shot:",','.join(player_choice))
			user=input()
			condition=random.choice(conditions)
			if condition == 'w':
				print(player[0]+':out',score_list[0])
				w+=1
				player.pop(0)
				score_list.pop(0)
				print("Batsman",player[0],"&",player[1])

			elif condition%2==1:

				# print(condition)
				score_list[0] += condition
				print(player[0],score_list[0])
				print(player[1],score_list[1])
				total_runs+=condition
				
				player[0],player[1]=player[1],player[0]
				score_list[0],score_list[1]=score_list[1],score_list[0]
			else:
				
				print((player[1]),score_list[1])

				score_list[0] += condition
				print(player[0],score_list[0])
				total_runs+=condition
		print('Score',total_runs,"/",w,'complete over:',over)
	return(total_runs)


def Toss(a,team_player,Your_Team_players):
	import random
	choice=['Head','Tail']
	result=random.choice(choice)
	if a==result:
		print('        Congrats You won the toss start your batting\n')
		a=batting(Your_Team_players,team_player)
		print("                          2nd inning start")
		print("your bolling")
		b=bolling(Your_Team_players,team_player)
		if a>b:
			print("congrats you won the match ")
		else:
			print("You Lost the match")
	else:
		print('        You lost the Toss start your balling')
		b=bolling(team_player,Your_Team_players)
		print("                               2nd inning start")
		print("        your batting")
		a=batting(team_player,Your_Team_players)
		if b>a:
			print("YOU won the match")
		else:
			print("you lost the match")
	

def my_team(Your_Team_players,dic):
	team_List=[1,2,3,4]
	c=1
	value=random.choice(team_List)
	team_player=dic[value]
	if team_player==Your_Team_players:
		if value==4:
			value-=1
			team_player=dic[value+1]
		else:
			team_player=dic[value+1]



	print("\nIt is Opponent team>>>>\n")
	List_of_opponent_players=[]
	for i in team_player:
		print(c,i)
		c+=1
	print('Toss(Head or Tail)')
	user_input=input()
	Toss(user_input,team_player,Your_Team_players)

def chose_team():
	print("select YOU TEAM")
	dic={1:['Viral kholi','M.S.Dhoni','Rohit sharma','Haril pandya','K.L.rahul','Jadeja','Rishab pant','Jasprit bumrah','Mohammad shami','Ishant sharma','chahal']
	,2:['Smith','David warner','Finch','Mithial','K.richardson','maxwell','P.Cummins','N.Layon','Mathhew wade','Astron agar','Adam zampa'],
	3:['babar azim','Sarfaraj Ahamad','mohamaad amir','Shoaob malik','Hasan ali','Farak Zaman','Mohammad Hafiz','Naseem Shah','Shabed khan','Afridi','Haffizuddin'],
	4:['Gayle','Pollard','J.Holder','S.Hetmyer','E.Lewis','Thomas','Bravo','Sunil amborus','Rovman','Ashley','N.poorna']}
	
	print ("1.Ind", "2.Aus", "3.Pak", "4.Wes")
	
	whichteam=input('Select your team:')
	print()
	print("This is your team players")
	Your_Team_players=(dic[int(whichteam)])
	c=1
	for i in Your_Team_players:
		print(c,i)
		c+=1
	my_team(Your_Team_players,dic)
	
chose_team()
# select=input('select team:')
# if select=='ind':
# 	user_team=Team1
# 	opponent_team=Team2
# else:
# 	user_team=Team2
# 	opponent_team=Team1
# print("What would like to batt/ball:")
# user=input()
# if user=='bat':
# 	a=batting(user_team,opponent_team)
# 	b=bolling(user_team,opponent_team)
# 	if a>b:
# 		print("You Won")
# 	else:
# 		print("You Lost")
# else:
# 	a=bolling(user_team,opponent_team)
# 	b=batting(user_team,opponent_team)
# 	if a>b:
# 		print("you won")
# 	else:
# 		print('you lost')		


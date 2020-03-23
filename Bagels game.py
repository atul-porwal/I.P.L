# import random
# print("\n                              welcome to Bagels game\n")
# print('  Pico         One digit is correct but in the wrong position.\n')
# print('  Fermi        One digit is correct and in the right position.\n')
# print('  bagels       No digit is correct.\n')

# def get_secretno():
# 	numbers=list(range(10))
# 	random.shuffle(numbers)
# 	# print(numbers)
# 	secret_no=''
# 	for get_no in range(3):
# 		secret_no+=str(numbers[get_no])
# 	return (secret_no)






# def getclue(guess,secret_no):
# 	if guess==secret_no:
		
# 		return "you won"
# 	result=[]
# 	list1=[]
# 	for no in range(len(secret_no)):
# 		if guess[no] in secret_no:
# 			if guess[no] not in list1:
# 				list1.append(guess[no])
# 				if guess[no]==secret_no[no]:
# 					result.insert(no,"fermi")
# 				else:
# 					result.append("pico")
# 			else:
# 				print("secret number doesn't have duplicates so bhaad me javu")
# 				break
# 		else:
# 			result.append("bagels")
# 	return(result)


# def play_again():
# 	user=input("Do you wanna play again (y/n)")
# 	if user=="y":
# 		print("\n               your game start again       ")
# 		chances()

# 	else:
# 		print("Thanks for playing")



# def chances():
# 	chance=4
# 	print("your game starts now")
# 	a=get_secretno()
# 	# print(a)
# 	for i  in range(chance):
# 		print(chance,"choice")
# 		guess=input("enter your choice")
# 		chance-=1
# 		result_of_game=getclue(guess,a)
# 		if result_of_game=="you won":
# 			print(result_of_game)
# 			play_again()

# 		else:
# 			print(result_of_game)
# 	if chance==0:
# 		print("sorry yoy lost the game and your secret_no is :",a)	
# 		play_again()	
# chances()






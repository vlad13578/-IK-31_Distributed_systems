
print("Hello World!")
user_names = ['std1', 'std2', 'std3', 'std4']
user_logins = ['std_1', 'std_2', 'std_3', 'std_4']
user_passwords = ['12601', '12602', '12603', '12604']
Status_cycle = 1

def DecCommand(cmd):
	global Status_cycle
	ena_space = 0	
	param_count = 0
	comand = ""
	parameter = []
	tmp=""
	for char in cmd:
		if (char == "'") | (char == '"'):
			ena_space = 1 - ena_space
		elif (char == ' ') & (param_count == 0):
			comand = tmp
			tmp = ""
			param_count = param_count + 1
		elif (char == ' ') & (param_count > 0) & (ena_space == 0):
			param_count = param_count + 1
			parameter.append(tmp)
			tmp = ""
		else:
			tmp = tmp + char
	if param_count == 0:
		comand = tmp
		tmp = ""
	elif param_count > 0:
		parameter.append(tmp)
		tmp = ""
		
	print('Entered command = "' + comand + '", ' + "parameters =", parameter)
	
	if comand == "ping":
		if len(parameter) == 1:
			tmp = "Ping " + parameter[0] + " ...\n"
			tmp = tmp + "Ping " + parameter[0] + " request success."
			return tmp
		else:
			return "PING ERROR (Incorect input argument)"
	elif comand == "echo":
		tmp = ""
		for i in range(len(parameter)):
			tmp = tmp + parameter[i]
			if (i + 1) != len(parameter):
				tmp = tmp + "\n"
		return tmp
	elif comand == "login":
		if len(parameter) == 2:
			user_number=-1
			for i in range(len(user_logins)):
				if user_logins[i] == parameter[0]:
					user_number=i
					break
			if user_number > -1:
				if user_passwords[i] == parameter[1]:
					return "LOGIN SUCCESS:\n Hello, " + user_names[user_number]
				else:
					return "LOGIN ERROR (Incorect input login or password)"
			else:
				return "LOGIN ERROR (Incorect input login or password)"
		else:
			return "LOGIN ERROR (Incorect input argument)"
	elif comand == "list":
		tmp = ""
		for i in range(len(user_names)):
			tmp = tmp + str(i+1) + ". " + user_names[i]
			if (i + 1) != len(user_names):
				tmp = tmp + "\n"
		return tmp
	elif comand == "msg":
		if len(parameter) == 2:
			if parameter[0] in user_names:
				return "MESSAGE SENDING SUCCESS"
			else:
				return "MESSAGE SENDING ERROR (This user not found)"
		else:
			return "MESSAGE SENDING ERROR (Incorect input argument)"
	elif comand == "file":
		if len(parameter) == 2:
			if parameter[0] in user_names:
				try:
				    f = open(parameter[1])
				    f.close()
				except FileNotFoundError:
				    return "FILE SENDING ERROR (File not found)"
				return "FILE SENDING SUCCESS"
			else:
				return "FILE SENDING ERROR (User not found)"
		else:
			return "FILE SENDING ERROR (Incorect input argument)"
	elif comand == "exit":
		Status_cycle = 0
		return "Exit from cycle"
	else:
		tmp = 'No Command = "' + comand + '"'
		return tmp


while(Status_cycle == 1):
	print("="*40)
	str_cmd = input("Input Command: ")
	str_out = DecCommand(str_cmd)
	print("-"*40)
	print("\nResults:")
	print(str_out)


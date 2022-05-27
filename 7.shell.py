import subprocess,os
mode = int(input())
if mode == 1 :
    while True:
        print("input your command(CTRl + C to terminal):")
        input_command = str(input())
        if input_command == "exit":
            break
        else:
            os.system(input_command)
else:    
    while True:
        print("input your command(CTRl + C to terminal):")
        input_command = str(input())
        if input_command == "exit":
            break
        else:
            output = subprocess.Popen(input_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
   
import subprocess

def run_command_live(command):
    process = subprocess.Popen(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    while True:
        output = process.stdout.readline()
        if output:
            print(output.strip())  
        if process.poll() is not None:
            break

    remaining_output, remaining_error = process.communicate()
    if remaining_output:
        print(remaining_output.strip())
    if remaining_error:
        print("Error:", remaining_error.strip())

while True:
    i = input("Please input the commands: ")
    if i.lower() == "exit()":
        break
    run_command_live(i)

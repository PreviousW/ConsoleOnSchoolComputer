import subprocess

def run_command(command):
    result = subprocess.run(command, text=True, capture_output=True)
    return result.stdout, result.stderr

while True:
    i = input("please input the commands : ")
    if i == "exit()":
        break
    stdout, stderr = run_command(i)
    print("Output:", stdout)
    if stderr:
        print("Error:", stderr)

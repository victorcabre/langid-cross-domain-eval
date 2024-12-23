import subprocess
import time

def run_command(lang):
    command = f"grep \"^{lang.strip()}\" data/cut.train | cut -f 2 | ./textcat/text_cat -n > textcat/lm/{lang.strip()}.lm"
    subprocess.run(command, shell=True)
    

# Read language labels (__label__abc)
with open("data/language_names.txt") as file:
    langs = file.readlines()

# Run all training commands
start = time.time()
for lang in langs:
    run_command(lang)

end = time.time()
sequential_time = end - start

print(f"Total time (sequential simulation): {sequential_time:.2f} seconds")

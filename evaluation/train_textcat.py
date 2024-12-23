import subprocess
import concurrent.futures
import time

# Returns total time of generation of a language profile for a single language
def run_command(lang):
    start = time.time()
    command = f"grep \"^{lang.strip()}\" data/all.0.train | cut -f 2 | ./textcat/text_cat -n > textcat/lm_temp/{lang.strip()}.lm"
    subprocess.run(command, shell=True)
    end = time.time()
    return end - start


# Read language labels (__label__abc)
with open("data/language_names.txt") as file:
    langs = file.readlines()

# Run commands concurrently
sequential_time = 0
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Execute the run_command for each language in parallel
    # But we accumulate the time as if they were run sequentially
    for time_taken in executor.map(run_command, langs):
        sequential_time += time_taken

print(f"Total time (sequential simulation): {sequential_time:.2f} seconds")

import subprocess
import sys

print(subprocess.check_output(["echo", "abc"]).decode())


# print(sys.executable)
# result = subprocess.run([sys.executable, "-c", "print('ocean')"])
# print(result)     # subprocess.run returns a subprocess.CompletedProcess obj


# result = subprocess.run(
#     [sys.executable, "-c", "print('ocean')"], capture_output=True,
# )
# print("stdout:", result.stdout)   # stdout: ocean
# print("stderr:", result.stderr)   # stderr:


# result = subprocess.run(
#     [sys.executable, "-c", "raise ValueError('oops')"], capture_output=True
# )
# print("stdout:", result.stdout) # stdout:
# print("stderr:", result.stderr) # ValueError: 'oops'

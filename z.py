import os,sys,subprocess

file_path = os.path.join(os.getcwd(),"dist","QuickSMS.exe") 
# os.startfile(file_path)
# file_path = file_path.replace("\\", "\\\\")

print("file_path = ",file_path)  

o = subprocess.Popen([file_path, "--ask_product_key=False"],shell=True)
# o = subprocess.Popen([file_path,],shell=True)
# o = subprocess.Popen(["main.py", "--ask_product_key=False"],shell=True)

# o.wait()  


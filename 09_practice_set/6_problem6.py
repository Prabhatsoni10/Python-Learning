# Write a program to mine a log file and find out whether it contain 'python' or not.
with open(f"dummy.HTML")as f :
    content = f.read()

if("python"in content):
    print("yes python is in the string ")    
else:
    print("no!,python is not in the string ")
import time

def countdown(t):
  while(t):
    mins,secs = divmod(t,60)
    timer = f"{mins:02}:{secs:02}"
    print(f"{timer}\n")
    time.sleep(1)
    t = t -1
  print("Timer End!")

countdown(int(input("Enter time in seconds: ")))
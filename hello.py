print("Hello! ")
answer = input("How are you? ")
good = {"good","g","well","verywell","verygood","happy"}
bad = {"bad","b","sad","verybad","verysad","unwell","veryunwell"}
if answer.strip().lower() in good:
  print("good 👍 ")
elif answer.strip().lower() in bad:
  print("really? ")
else:
  print("what are you saying? ")

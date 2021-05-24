def order(sentence):
  # code here
  final = []
  s = sentence.split()
  for i in range((len(s))):
      for i in s:
          if i == 1:
            final += s
            print(s)
  print(final)

#   for i in split:
#       if i.isalnum() == True:
#         i.split()
#         print(i)

# text = "is2 Thi1s T4est 3a"
text = "is2 Thi1s T4est 3a"
order(text)
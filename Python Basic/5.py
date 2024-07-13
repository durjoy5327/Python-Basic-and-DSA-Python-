word_count={}
with open("F:\\python practice\\Assignment\\poem.txt","r") as f:
  for line in f:
    words=line.split(' ')
    for word in words:
      if word in word_count:
        word_count[word]+=1
      else:
        word_count[word]=1


word_occurence= list(word_count.values())
maximum = max(word_occurence)
for word, count in word_count.items():
  if maximum==count:
    print(f"Maximum word in poem is '{word}' = {count}")


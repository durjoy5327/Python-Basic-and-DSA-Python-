"""
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

"""




heros=['spider man','thor','hulk','iron man','captain america']

print(f" the length of the heros list is {len(heros)}\n")

print(f"After adding black panther({heros.append('black panther')}) the list of heros : {heros}\n")

print(f"After removig {heros.remove('black panther')} halk from the list of heros: {heros}\n")
print(f"After adding black panther after halk({heros.insert(3,'black panther')}) the list is : {heros}\n")

heros[1:3]=['doctor strange']
print(f"Replacing hulk and thor with doctor strange : {heros}\n")

heros.sort()
print("After sorting heros list : ", heros)
# split - split a string 
# returns a list

msg = "I am a good boy"

# default split from spaces " "
msg.split()

# split for a character
file = "music.mp4"
file.split(".")

# count the words in a string
a = "What do you mean"
len(a.split())

# ---------------------------------------
# JOIN
# Converts a list to string
name = ["aman", "khanna"]
# specify kisse join krna and then .join(list)
" ".join(name)

new_list = ["aman", "khanna", 785]
# now we cant join directly as 785 is an int
" ".join(str(i) for i in new_list)

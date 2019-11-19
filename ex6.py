types_of_pepole = 10
x = f"There are {types_of_pepole} types of pepole."

binary = "binary" 
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evalouation = "Isn't the joke so funny?! {}"

print(joke_evalouation.format(hilarious))

w = "This is the left side of ...."
e = "a string with a right side." 

print(w + e)
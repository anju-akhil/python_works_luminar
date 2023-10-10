#method overloading
#create a function max_word that will accept any number of parameters and return lengthy string
def max_word(*args):
    lengthy_word=max(args,key=lambda w:len(w))
    return lengthy_word
print(max_word("hello","evening","goodmorning"))
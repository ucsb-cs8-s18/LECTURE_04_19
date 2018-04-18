# LECTURE_04_19


# Let's talk about function call vs function definition.

Function definitions looks like this:

```
def f(x):
  return x * x
 
def longerString(a,b):
  if len(b)>len(a):
     return b
  else
     return a
```

Function calls look like this:

```
x = f(3)
print(longerString('cat','chicken'))
y = f(f(2))
```

Function calls are when you actually USE the function to compute a result and return a value.

When you call a function, if you fall off the end without doing a return, Python automatically does a `return None`.

In a function definition, the parameters are the things in parentheses right after the function name.  

For example, here the parameter is `x`:

```
def f(x):
  return x * x
```

Here, the parameters are: `a` and `b`:

```
def longerString(a,b):
  if len(b)>len(a):
     return b
  else
     return a
```

Parameters in a function definition ALWAYS have to be variable names.  This is is not legal:

```
def f("x"):        # NO!  "x" is not a variable
   return x * x

def longerString(first string, second string):  #NO! no spaces in variable names
    ...
```

In a function call, you can have a variable (as long as it is already defined), or a literal value, or an expression.

For example,these are all legal:

```
y = 3
x = f(y)
a = f(4)
b = f(3 + 2)
```




# Logic vs. syntax (see examples)

Also, let's talk about code that is logically correct, but has incorrect syntax (see examples in repo).

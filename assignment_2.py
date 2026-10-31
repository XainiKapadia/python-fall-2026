stdCode = 34551001
stdName = 'Mohammed'
stdLastname = 'Ali'
stdMidterm = 80
stdFinal = 98.5
stdGPA = 3.7
stdActive = True
stdCourses = ['Python', 'Math', 'English']
stdBirthDate = (2001, 5, 14)
stdProfile = {'name': 'Mohammed', 'city': 'Alexandria'}
stdSkills = {'typing', 'Excel', 'typing'}
stdAdvisor = None

# 1. Use type() to print the data type of stdCode, stdName and stdFinal.

print(type(stdCode))
print(type(stdName))
print(type(stdFinal))

# 2. Print the data type of stdActive and stdAdvisor.

print(type(stdActive))
print(type(stdAdvisor))

# 3. Print the data type of stdCourses, stdBirthDate, stdProfile and stdSkills.

print(type(stdCourses))
print(type(stdBirthDate))
print(type(stdProfile))
print(type(stdSkills))

# 4. PREDICT: How many items will print(stdSkills) show? Why?
# My guess: 2 items, because sets do not allow duplicate values.

print(stdSkills)

# 5. Create a variable x = 5j and print its data type.

x = 5j
print(type(x))

# 6. Create a variable r = range(5). Print its data type, then print list(r) to see the numbers inside it.

r = range(5)
print(type(r))
print(list(r))

#7. Convert stdMidterm to a float using float(). Print the new value and its type.

NewstdMidterm = float(stdMidterm)
print(NewstdMidterm)
print(type(NewstdMidterm))

#8. PREDICT: What will print(int(stdFinal)) show? Does it round up?
# My guess: yes

print(int(stdFinal))

#9. Convert stdCode to a string and print how many characters it has using len()

NewstdCode = str(stdCode)
print(len(NewstdCode))

#10. Create a frozenset from stdCourses and print its data type

NewstdCourses = frozenset(stdCourses)
print(type(NewstdCourses))

#11. Create a variable msg = b"Hello" and print its data type.

msg = b"Hello"
print(type(msg))

#12. PREDICT the data type of each value below, then check with type():
# 10 10.0 "10" [10] (10,) {10} {'a':10} True
# My guesses: int, float, string, list, tupple, set, dictionary, bool

print(type(10))
print(type(10.0))
print(type("10"))
print(type([10]))
print(type((10,)))
print(type({10}))
print(type({'a': 10}))
print(type(True))

#13. PREDICT: What is the data type of stdMidterm + stdFinal
# My guess: float

print(type(stdMidterm + stdFinal))

#14. PREDICT: What is the data type of stdMidterm/2? (Hint: 80/2=40...or is it?)
# My guess: float, because / returns float and // returns int

print(type(stdMidterm / 2))

#15. Fill in the blank so the output is <class 'tuple'>?
#print(type(_))

print(type(stdBirthDate))

#BONUS: Why does print(type(1)) show <class 'int'> and not <class 'tuple'>?
# My Answer: it doesnt have a comma 

print(type(1))
stdCode = 34551001
stdMidterm = 80
stdFinal = 98
stdName = 'Mohammed'
stdLastname = 'Ali'
print('Student Name: Mohammed Ali - Student Code:' + str(stdCode))
print('Student Grade Final:' + str(stdFinal))
print(stdName, stdLastname)
#print(stdFinal+''+stdLastname)
print(stdFinal==stdMidterm)
print(stdFinal!=stdMidterm)
print('Average (Midterm and Final) is:' + str((stdMidterm + stdFinal)/2))
#stdCode = 1
#print('New Student Code:', stdCode)
print((not(stdName=='Ayesha')or(stdFinal>stdMidterm)) and (stdMidterm!=stdFinal))
print('345' in str(stdCode))
print('345' not in str(stdCode))
print(5 * 2 % 5)
print('Final is : ' + str(stdFinal))
print('3' * 3)
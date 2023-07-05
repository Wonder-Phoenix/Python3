import random
import inspect

# Programme créer avec un ami pour s'entrainer sur les listes

testList =[]
for i in range(0,random.randint(3,6)):
    testList.append(random.randint(1,6))
print("testList =",str(testList))
testValue = testList[random.randint(0,len(testList)-1)]
#print("testValue =",str(testValue))
testObject =[]
for i in range(0,random.randint(1,3)):
    testObject.append(random.randint(1,10))
#print("testObject =",str(testObject))
testIndex = random.randint(0,len(testList)-1)
#print("testIndex =",str(testIndex))

methodsList =[]
for method in testList.__dir__():
    if method[0:2] !='__' :
        methodsList.append(method)
random.shuffle(methodsList)
#methodsList

print("testList =",str(testList))
for method in methodsList:
    listArg = inspect.getfullargspec(eval("testList."+method))
    print()
    testListSauv=testList.copy()
    #print(method,listArg.args)
    if len(listArg.args) == 1:
        testMethod = "testList."+method+"()"
        testMethodPrint = testMethod
    elif listArg.args[1] == 'iterable':
        testMethod = "testList."+method+"("+"testObject"+")"
        testMethodPrint = "testList."+method+"("+str(testObject)+")"
    elif listArg.args[1] == 'object':
        testMethod = "testList."+method+"("+"testValue"+")"
        testMethodPrint = "testList."+method+"("+str(testValue)+")"
    elif listArg.args[1] == 'index' and len(listArg.args) == 2:
        testMethod = "testList."+method+"("+"testIndex"+")"
        testMethodPrint = "testList."+method+"("+str(testIndex)+")"
    elif listArg.args[1] == 'index' and listArg.args[2] == 'object' and len(listArg.args) == 3:
        testMethod = "testList."+method+"("+"testIndex,testValue"+")"
        testMethodPrint = "testList."+method+"("+str(testIndex)+","+str(testValue)+")"
    elif listArg.args[1] == 'value':
        testMethod = "testList."+method+"("+"testValue"+")"
        testMethodPrint = "testList."+method+"("+str(testValue)+")"
    print(testMethodPrint)
    resultat = eval(testMethod)
    evaluation=input()
    try :
        evaluation = eval(evaluation)
    except :
        evaluation = "c'est faux"
    if resultat!=None:
        print(str(resultat))
        if method == 'pop' :
            print(str(testList))
            if evaluation==resultat or evaluation==testList:
                print("gagné")
            else :
                print("perdu")
        else:
            if evaluation==resultat:
                print("gagné")
            else :
                print("perdu")
    else :
        print(str(testList))
        if evaluation==testList:
            print("gagné")
        else :
            print("perdu")    
    testList = testListSauv.copy()
print("fini")

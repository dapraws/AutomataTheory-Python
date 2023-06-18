sentence = input()
state = 'start'
status = len(sentence) != 0
listWord = sentence.split()
listLabel = []
condition = []
action = []
stack = []

for word in listWord :
    word += '#'
    state = 'Q0'
    i = 0
    while word[i] != '#':
        varBool = ['a','b','c', 'd', 'e']
        logicalOp = ['|','&']
        varInt = ['p','q','r', 's', 't']
        mathOp = ['+','-','/', '*']
        if state == 'Q0' and word[i] == 'i':
            state = 'IF-1'
        elif state == 'IF-1' and word[i] == 'f':
            state = 'IF'
            listLabel.append(state)
        elif word[i] in varBool :
            state = 'BOOLEAN'
            condition.append(word[i])
            if 'CONDITION' not in listLabel :
                listLabel.append('CONDITION')
        elif state == 'Q0' and word[i] in logicalOp :
            state = 'LOGICALOP-1'
        elif state == 'LOGICALOP-1' and word[i] == word[i-1] :
            state = 'LOGICALOP'
            condition.append(word[:len(word)-1])
        elif word[i] in varInt :
            state = 'INTEGER'
            action.append(word[i])
            if 'ACTION' not in listLabel :
                listLabel.append('ACTION')
        elif word[i] in mathOp :
            state = 'MATHOPERATOR'
            action.append(word[i])
        elif word[i] == '=' :
            state = 'ASSIGN'
            action.append(word[i])
        elif word[i] == '{' :
            state = 'ACTSTART'
            listLabel.append(state)
        elif word[i] == '}' :
            state = 'ACTSTOP'
            listLabel.append(state)
        else :
            state = 'denied'
            status = False
            listLabel.append(state)
        i += 1  
    state = 'Q0'


print(listLabel)
print(condition)

stateCondition = 'start'
boolTerminal = ['a','b','c', 'd', 'e']
boolQ0 = ['BOOL', 'BOOL', 'BOOL', 'BOOL', 'BOOL']
logicopTerminal = ['||', '&&']
logicopQ0 = ['LOGICOP', 'LOGICOP']
j = 0
while j < len(condition) and status:
    if stateCondition == 'start' :
        if condition[j] not in boolTerminal :
            stateCondition = 'ERROR'
            status = False
        else :
            stateCondition = boolQ0[boolTerminal.index(condition[j])]
    elif stateCondition == 'BOOL' :
        if condition[j] not in logicopTerminal :
            stateCondition = 'ERROR'
            status = False
        else :
            stateCondition = logicopQ0[logicopTerminal.index(condition[j])]
    elif stateCondition == 'LOGICOP' :
        if condition[j] not in boolTerminal :
            stateCondition = 'ERROR'
            status = False
        else :
            stateCondition = boolQ0[boolTerminal.index(condition[j])]
    j += 1
statusCondition =  stateCondition == 'BOOL' 

stateAction = 'start'
intTerminal = ['p', 'q', 'r', 's', 't']
intQ0 = ['INT1', 'INT1', 'INT1', 'INT1', 'INT1']
intQ1 = ['INT2', 'INT2', 'INT2', 'INT2', 'INT2']
mathopTerminal = ['+', '-', '/', '*']
mathopQ0 = ['MATHOP', 'MATHOP', 'MATHOP', 'MATHOP', 'MATHOP']
j = 0
while j < len(action) :
    if stateAction == 'start' :
        if action[j] not in intTerminal :
            stateAction = 'ERROR'
            status = False
        else :
            stateAction = intQ0[intTerminal.index(action[j])] 
    elif stateAction == 'INT1' :
        if action[j] == '=' :
            stateAction = 'ASSIGN'
        else :
            stateAction = 'ERROR'
            status = False
    elif stateAction == 'ASSIGN' :
        if action[j] not in intTerminal :
            stateAction = 'ERROR'
            status = False
        else :
            stateAction = intQ1[intTerminal.index(action[j])] 
    elif stateAction == 'INT2' :
        if action[j] not in mathopTerminal :
            stateAction = 'ERROR'
            status = False
        else :
            stateAction = mathopQ0[mathopTerminal.index(action[j])] 
    elif stateAction == 'MATHOP' :
        if action[j] not in intTerminal :
            stateAction = 'ERROR'
            status = False
        else :
            stateAction = intQ1[intTerminal.index(action[j])] 
    j += 1

statusAction = stateAction == 'INT2' 


stack.append('#')
stack.append('IF')
state = 'start'
status = True
i = 0
while len(stack) != 0 and status:
    print(stack)
    if state == 'start' and stack[-1] == listLabel[i] :
        stack.pop()
        stack.append('CONDITION')
        state = 'IF'
    elif state == 'IF' and stack[-1] == listLabel[i] :
        stack.pop()
        if statusCondition :
            stack.append('ACTSTART')
        state = 'CONDITION'
    elif state == 'CONDITION' and stack[-1] == listLabel[i] :
        stack.pop()
        stack.append('ACTION')
        state = 'ACTSTART'
    elif state == 'ACTSTART' and stack[-1] == listLabel[i] :
        stack.pop()
        if statusAction :
            stack.append('ACTSTOP')
        state = 'ACTION'
    elif state == 'ACTION' and stack[-1] == listLabel[i] :
        stack.pop()
        state = 'ACTSTOP'
    elif state == 'ACTSTOP' :
        elementTerakhir = stack.pop()
        status = elementTerakhir == '#'
    else :
        status = False
    i += 1

if status :
    print('SINTAKS SESUAI GRAMMAR')
else :
    print('SINTAKS TIDAK SESUAI GRAMMAR')

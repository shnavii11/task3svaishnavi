import os
miswords = ['print', 'eval', 'exec']
linelenght = 80

def removespaces(s):
    i=len(s)-1
    while i >= 0 and s[i] == ' ':
        i = i - 1
    return s[:i+1]

def checkfiles(filepath):
    violated = 0
    
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()
    for il in lines:
        newline = removespaces(il)
        hash = -1
        for i in range(len(newline)):
            if newline[i] == '#':
                hash = i
                break
        if hash != -1:
            nl = newline[:hash] 
        else:
            nl = newline

        if len(newline) > linelenght:
            violated = violated+1
        for keyword in miswords:
            if keyword in nl:
                violated = violated+1
        dtwo =0
        d1 = 0
        for char in newline:
            if char == '"':
                dtwo = dtwo + 1
            elif char == "'":
                d1 = d1 + 1

        if (dtwo % 2) != 0 or (d1 % 2) != 0:
            violated = violated+1
    
    return violated

def FINDISSUES(violated):
    if violated > 5:
        return "High"
    elif violated < 4:
        return "Low"
    else:
        return "workss"
        
def main():
    print("DEBUG: Program starting")  
    if not os.path.exists('task3'):
        # print("ERROR: No 'task3' directory found!")
        return

    for root, dirs, files in os.walk('task3'): 
        # print(f"DEBUG: In directory {root}")  
        # print(f"DEBUG: Found files: {files}")  

        for file in files:
            if len(file) > 3 and file != 'code.py':
                filepath = os.path.join(root, file)
                # print(f"DEBUG: Checking {filepath}")

                violated = checkfiles(filepath)
                risk = FINDISSUES(violated)
                print("Result: " + filepath + " : " + str(risk))

if __name__ == "__main__":
    main()
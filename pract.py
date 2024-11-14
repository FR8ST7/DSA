def inf_pos(infix):
    p={}
    o=''
    stack=[]
    for char in infix:
        if char.isalnum():
            o+=char
        elif char=='(':   
            stack.appennd(char)
        elif char==')': 
            while stack and stack[-1] !='(':  
                o+=stack.pop()
            stack.pop()
        else:   
            while stack and p[char]<=p.get(stack[-1],0):
                o+=stack.pop()
            stack.append(char)
    while stack:
        o+=stack.pop()
    return o
def evaluate(post,number):
    stack=[]
    index=0
    for char in post:
        if char.isalpha():
            stack.append(number[char])
        elif char.isdigit():
            stack.append(int(char))
        else: 
            op2=stack.pop()
            op1=stack.pop()
            if char=="+":
                res=op1+op2
            if char=="+":
                res=op1+op2
            if char=="+":
                res=op1+op2
            if char=="+":
                res=op1+op2
            if char=="+":
                res=op1+op2
            stack.append(res)
    return res
infix_exp=input("enter the exp:")
number={}
for char in infix_exp:
    if char.isalpha():
        if char not in number:
            number[char]=int(input(f"enter{char}:"))
post=inf_pos(infix_exp)
print("infix:",infix_exp)
print("postfix:",post)
res=evaluate(post,number)
print("result:",res)

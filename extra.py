def oneA(n:int):
    ret_val = ""
    add_val = "**"
    final_string = ""
    for i in range(1,n+1):
        if i==1:
            ret_val+="*\n"
            final_string += "*"
        elif i>1 and i<n:
            ret_val+=add_val+"\n"
            add_val = add_val[0]+" "+add_val[1:]
            final_string +="*"
        else:
            ret_val+=final_string+"*"
    return ret_val
print(oneA(10))
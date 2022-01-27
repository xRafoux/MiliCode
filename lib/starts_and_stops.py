def starting_INFOS(content):
    '''
    args: content -> str
    return: [ name , developper key ]
    Read the line starting by #DETAILS#:
    '''
    if content.startswith('#DETAILS#:'):
        name = None
        developper_key = None
        try:
            name = content.replace("#DETAILS#: ","").split(" | ")[0]
        except IndexError:
            pass
        try:
            developper_key = content.replace("#DETAILS#: ","").split(" | ")[1]
        except IndexError:
            pass
        if name == '':
            name = None
        if developper_key == "":
            developper_key = None
        return [name,developper_key]
    else:
        return None

def first_line_CHECK(content:str):
    '''
    args: content -> str
    return: True if content = MiliCode.Start or MC.Start, else False
    Read the first line
    '''
    check = False
    if "MiliCode." in content:
        rst = content.replace("Milicode.","")
        if "Start()" in rst:
            check = True
            return check
        else:
            check = False
    if "MC." in content:
        rst = content.replace("MC.","")
        if "Start()" in rst:
            check = True
        else:
            check = False
    else:
        check = False
    return check
    # if content.startswith('MiliCode.') == True:
    #     print("ici")
    #     rst = content.replace("MiliCode.","").replace(" ","")
    #     print(rst)
    #     if "Start()" in rst:
    #         return True
    #     else:
    #         return False
    # print("content2 : " + content)
    # if content.startswith('MiliCode.') == False:
    #     print("ici2")
    #     if content.startswith("MC."):
    #         rst = content.replace("MC.","").replace(" ","")
    #         if "Start()" in rst:
    #             return True
    #         else:
    #             return False
    # else:
    #     print("ici3")
    #     return False
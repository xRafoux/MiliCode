# -- Modules -- #

import colorama
import argparse
import lib.starts_and_stops as Starts_and_stops
import lib.Errors as Errors

# -- Soon -- #

import os

# -- Modules initialisations -- #

colorama.init()

# -- Arg Parser -- #

parser = argparse.ArgumentParser()
parser.add_argument("file_name")
parser.add_argument("-v","--verbosity", help="increase output verbosity",default=0)

# -- Argparser args sorter -- #

args = parser.parse_args()
file_name = args.file_name
verbosity = args.verbosity

# -- Colors Variables -- #

black = colorama.Fore.BLACK
red = colorama.Fore.RED
green = colorama.Fore.GREEN
blue = colorama.Fore.BLUE
magenta = colorama.Fore.MAGENTA
cyan = colorama.Fore.CYAN
white = colorama.Fore.WHITE
reset_color = colorama.Fore.RESET

# -- Styles Variables -- #

dim = colorama.Style.DIM
normal = colorama.Style.NORMAL
bright = colorama.Style.BRIGHT
reset_style = colorama.Style.RESET_ALL

# -- Check file functions -- #

def check_file(file):
  '''
  args: file -> str
  return: True if file end with .MC or .MiliCode and if file exists, 'MC' if file doesn't end with .MC or .MiliCode, 'File' if file doesn't exists
  '''
  if file.endswith(".MC") or file.endswith(".MiliCode"):
    if os.path.isfile(file) == True:
      return True
    else:
      return 'File'
  else:
    return 'MC'

# -- Open .MC or .MiliCode Files -- #

def open_file_MC(file):
  '''
  args: file -> str
  return: the content of the file, else False
  '''
  file_exists = check_file(file)
  if file_exists == 'File':
    print(red + bright + "File doesn't exists.")
    exit()
  if file_exists == 'MC':
    print(red + bright + "The file doesn't end by .MC or .MiliCode")
    exit()
  if file_exists == True:
    content = open(file,'r').readlines()
    return content

# -- Clean Code -- #

def clean_code(file):
  '''
  args: file -> str
  return: the clean file content without \n or spaces ( for better comprehension )
  '''
  content = open_file_MC(file)
  if content != "" and content != None and content != " " and len(content) != 0:
    for i in content:
      if i == "\n" or i == "\\n" or i == "" or i == " ":
        a = i.replace("\n","").replace("\\n","").replace(" ","")
        content[content.index(i)] = a
        continue
      if i.endswith("\n"):
        a = i.replace("\n","").replace("\\n","")
        content[content.index(i)] = a
    return content
  else:
    print(red + bright + "File is empty.")
    exit()

# -- Main Script -- #

def main():
  '''
  MiliCode Worker Main Function
  args: None
  return: None
  Just execute the MiliCode files and use the lib
  '''
  global verbosity,file_name

  # -- The clean file content ready to be used -- #

  content_file__ = clean_code(file = file_name)

  # -- Necesaries Variables For Good Working Of MiliCode Script's -- #

  line = 0
  last_line = len(content_file__) - 1
  variables = {}
  fonctions = {}
  in_fonctions_ = False
  function_name_ = None
  name = None
  developper_key = None

  # -- First Checks -- #

  for content in content_file__:

    if line == 0:
      check = Starts_and_stops.first_line_CHECK(content)
      print(check)
      if check == True:
        continue
      else:
        raise Errors.CANT_START_CODE(f"[ERROR] Missing starting line. Line: {line}")

    if line == last_line:
      pass

    if content.startswith("#DETAILS#:"):
      infos = Starts_and_stops.starting_INFOS(content = content)
      if infos != None:
        name = infos[0]
        developper_key = infos[1]
        if name == None and developper_key == None:
          raise Errors.DETAILS_ERROR("I detected the line #DETAILS# but any name or developper key as been gived. Please retry with something or delete the line.")
        

main()

# for commands in content:
#   if commands.startswith("#INFO"):
#     iterations +=1
#     rst = commands.replace("#INFO ","")
#     name = rst.split(" | ")[0]
#     developer_key = rst.split(" | ")[1]
#     continue
#   if commands.startswith("#DIS#"):
#     iterations +=1
#     continue
#   if commands.replace(" ","").replace("  ","") == "" or commands.replace(" ","").replace("  ","") == " " or commands == None:
#     iterations += 1
#   commands = commands.replace("\n","").replace("\\n","")
#   if iterations == 0:
#     if commands == "louiscode.start":
#       iterations += 1
#     else:
#       print("[EXIT] ERROR CODE: 0")
#       exit(0)
#   if iterations == last_iteration:
#     if commands == "louiscode.stop":
#       print("[END] SUCCESFULLY EXECUTED")
#     else:
#       print(f"[EXIT] CODE CAN'T END, CODE: 9999, LINE: {iterations}")
#       exit(9999)
#   if "louiscode." in commands:
#     if "louiscode.ecrire" in commands:
#       if not in_fonction:
#         text = commands.replace("louiscode.ecrire ","")
#         if '"' in text:
#           text = text.replace('"','')
#           print(text)
#           iterations += 1
#         else:
#           try:
#             text = variables[text]
#             print(text)
#             iterations += 1
#           except KeyError:
#             print(f"[ERROR] CAN'T FIND THE VARIABLE {text}, CODE: 1, LINE: {iterations}")
#             exit(1)
#       else:
#         text = commands.replace("louiscode.ecrire ","").replace(" ","")
#         iterations += 1
#         fonctions[fonction_name]["execution"] += f"print({text});"
#       continue
#     if "louiscode.ecouter" in commands:
#       if not in_fonction:
#         rest = commands.replace("louiscode.ecouter ","").split("|")
#         text = rest[0].replace('"','')
#         var_name = rest[1].replace(" ","")
#         var = input(text)
#         variables[var_name] = var
#         iterations += 1
#       else:
#         rest = commands.replace("louiscode.ecouter ","").split("|")
#         text = rest[0].replace('"','')
#         var_name = rest[1].replace(" ","")
#         iterations += 1
#         fonctions[fonction_name]["exection"] += f"{var_name} = input({text});"
#       continue
#     if "louiscode.suprimer_variable" in commands:
#       var = commands.replace("louiscode.suprimer_variable ","")
#       try:
#         variables.pop(var)
#         continue
#       except KeyError:
#         print(f"[ERROR] CAN'T FIND THE VARIABLE {text}, CODE: 1, LINE: {iterations}")
#         exit(1)
#     if "louiscode.fonction" in commands:
#       if "louiscode.fonction.creer" in commands:
#         rst = commands.replace("louiscode.fonction.creer ","")
#         nom = rst.split("|")[0].replace(" ","")
#         args = []
#         json__ = {}
#         json__["nom"] = nom
#         rst = rst.replace(f"{nom} | ","")
#         arg = rst.split("/")[0].replace(" ","")
#         temp_arg = ""
#         for i in arg:
#           if i == ",":
#             args.append(temp_arg)
#             temp_arg = ""
#           if i == "[":
#             continue
#           if i == "]":
#             args.append(temp_arg.replace(",",""))
#           else:
#             temp_arg += i
#         json__["args"] = args
#         description = ""
#         rst = rst.split("/")[1]
#         if "'" in rst.split("{")[0]:
#           description = rst.split("{")[0].replace("'","")
#         json__["description"] = description
#         json__["execution"] = ""
#         fonctions[nom] = json__
#         in_fonction = True
#         fonction_name = nom
#       if "louiscode.fonction.executer" in commands:
#         rst = commands.replace("louiscode.fonction.executer ","")
#         func_name = rst.split("|")[0].replace(" ","")
#         if func_name in fonctions:
#           arg = rst.split("|")[1].replace(" ","")
#           total_args_required = len(fonctions[func_name]["args"])
#           args_required = fonctions[func_name]["args"]
#           args = []
#           temp_arg = ""
#           for i in arg:
#             if i == ",":
#               args.append(temp_arg)
#               temp_arg = ""
#             if i == "[":
#               continue
#             if i == "]":
#               args.append(temp_arg.replace(",",""))
#             else:
#               temp_arg += i
#           if len(args) == total_args_required:
#             execution = fonctions[func_name]["execution"]
#             for i in args_required:
#               execution = execution.replace(i,args[0])
#               del args[0]
#             exec(execution)
#           else:
#             print(f"[ERROR] MISSING ARGUMENTS AT THE CALL OF THE FONCTION CALLED {func_name}, LINE: {iterations}, CODE: 400")
#             exit(400)
#       if "louiscode.fonction.info" in commands:
#         rst = commands.replace("louiscode.fonction.info ","").replace(" ","").replace("\n","")
#         if rst in fonctions:
#           desc = fonctions[rst]['description']
#           args = fonctions[rst]["args"]
#           print(colorama.Fore.RED + f"🗽 INFORMATIONS OF THE FONCTION CALLED '{rst}'" + " 🗽" + colorama.Fore.RESET+ f"\n- Name: {rst}\n- Description: {desc}\n- Args: {args}")
#           if developer_key != None:
#             if developer_key == "12345678910":
#               execu = fonctions[rst]["execution"]
#               print(f"- Execution: '{execu}'")
#             else:
#               continue
#           else:
#             continue
#         else:
#           print(f"[ERROR] CAN'T FIND THE FONCTION {rst}, LINE: {iterations}, CODE: 456")
#     else:
#       if commands == "louiscode.start" or commands == "louiscode.stop":
#         continue
#       else:
#         print(f"[ERROR] CAN'T UNDERSTAND THIS THING: '{commands}' ,LINE: {iterations}, CODE: 123")
#         exit(123)
#   else:
#     if commands == "\n" or commands == " " or commands == "":
#       continue
#     if '}' == commands:
#       fonctions[fonction_name]["execution"] = fonctions[fonction_name]["execution"][:-1]
#       in_fonction = False
#       fonction_name = None
#       continue
#     else:
#       print(f"[ERROR] CAN'T UNDERSTAND THIS THING: '{commands}' ,LINE: {iterations}, CODE: 123")
#       exit(123)
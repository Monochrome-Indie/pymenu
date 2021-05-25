docs = """menu()
The menu() function is the base function used to create a menu variable.
Warning:
• Must be assigned to a variable.

menuItem()
The menuItem() function is used to assign a variable to a Menu Item.
You can then be add this on to a menu.
Parameters:
• name: The name to be displayed on the menu (this does not have to be the same as the variable name).
Warning:
• Must be assigned to a variable.

itemAppend()
The itemAppend() function is used to add append an item to a menu
Parameters:
• menuName: The name of the menu to be appended to.
• item: The item to be appended.

show()
The show() function is used to display a menu.
Parameters:
• menuName: the name of the menu to be displayed.
Warning:
• If the user does not do something correctly (such as typing the name of the option instead of it's number) it will return 'err'.\n• Must be assigned to a variable in order to store the selected option."""

about = """Pymenu is a simple python package used to create menus. Oh, and it is tiny.
Feedback: https://replit.com/@dObbOb11/PyMenu/"""

def example():
  myMenu = menu()

  helloWorldOp = menuItem("Hello, World!")
  greetOp = menuItem("Friendly Greeting")
  exitOp = menuItem("Exit")

  itemAppend(myMenu, helloWorldOp)
  itemAppend(myMenu, greetOp)
  itemAppend(myMenu, exitOp)

  mode = show(myMenu)

  if mode == 0:
    print("Hello, World!")
  if mode == 1:
    name = input("Name: ")
    print("Hello,", name + "!")
  if mode == 2:
    exit(0)

def menu():
  return []
def menuItem(name):
  return name
def itemAppend(menuName, item):
  menuName.append(item)
def show(menuName):
  optionNum = 0
  for item in menuName:
    optionNum += 1
    print("[" + str(optionNum) + "]", item)
  option = input("\n>> ")
  try:
    return int(option) - 1
  except:
    return "err"


if __name__ == "__main__":
  myMenu = menu()

  aboutOp = menuItem("About")
  docsOp = menuItem("Documentation")
  exampleOp = menuItem("Example")
  exitOp = menuItem("Exit")

  itemAppend(myMenu, aboutOp)
  itemAppend(myMenu, docsOp)
  itemAppend(myMenu, exampleOp)
  itemAppend(myMenu, exitOp)

  selected = show(myMenu)

  if selected == 0:
    print(about)
  if selected == 1:
    print(docs)
  if selected == 2:
    example()
  if selected == 3:
    exit(0)
  if selected == "err":
    print("Err")

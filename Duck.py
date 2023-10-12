
class JupyterNotebook:

    def execute(self):
        print("Interpreting")
        print("Running")

class PyCharm:

    def execute(self):
        print("Interpreting")
        print("Running")
        print("Spell Check")
        print("indentetion")


class Laptop:

    def code(self,ide):
        ide.execute()

ide = PyCharm()     #can use any class provided it has execute method (This is polymorphism Duck Typing)

lap1 = Laptop()
lap1.code(ide)



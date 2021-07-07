class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_tree(self,cond):
        space=" "*self.get_level()*2
        prefix=space + "|--"  if self.parent else""
        print(prefix + self.data)
        if self.children and self.get_level()<=cond:
            for child in self.children:
                child.print_tree(cond)


def build_product_tree():
    root = TreeNode("Global")
    India=TreeNode("India")
    USA=TreeNode("USA")

    Gujarat=TreeNode("Gujarat")
    Karnataka=TreeNode("Karnataka")
    New_Jersey=TreeNode("New Jersey")
    California=TreeNode("California")

    Ahmedabad=TreeNode("Ahmedabad")
    Baroda=TreeNode("Baroda")
    Bangalore=TreeNode("Bangalore")
    Mysore=TreeNode("Mysore")

    Prinston=TreeNode("Prinston")
    Trinton=TreeNode("Trinton")
    San_Fransico=TreeNode("San Fransico")
    Mountain_view=TreeNode("Mountain view")
    Palo_Alto=TreeNode("Palo Alto")

    root.add_child(India)
    root.add_child(USA)

    India.add_child(Gujarat)
    India.add_child(Karnataka)

    USA.add_child(New_Jersey)
    USA.add_child(California)

    Gujarat.add_child(Ahmedabad)
    Gujarat.add_child(Baroda)
    Karnataka.add_child(Bangalore)
    Karnataka.add_child(Mysore)

    New_Jersey.add_child(Prinston)
    New_Jersey.add_child(Trinton)
    California.add_child(San_Fransico)
    California.add_child(Mountain_view)
    California.add_child(Palo_Alto)

    root.print_tree(3)#printing with level as parameter
    root.print_tree(2)
    root.print_tree(1)
    root.print_tree(0)


if __name__=='__main__':
    build_product_tree()

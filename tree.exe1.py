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

    def print_tree(self,para):
        if para=="both":
            space=" "*self.get_level()*2
            prefix=space + "|--"  if self.parent else""
            print(prefix,end=" ")
            print(self.data[0],'(',self.data[1],')')
            if self.children:
                for child in self.children:
                    child.print_tree("both")
            return

        if para=="name":
            space=" "*self.get_level()*2
            prefix=space + "|--"  if self.parent else""
            print(prefix,end=" ")
            print(self.data[0])
            if self.children:
                for child in self.children:
                    child.print_tree("name")

        if para=="designation":
            space=" "*self.get_level()*2
            prefix=space + "|--"  if self.parent else""
            print(prefix,end=" ")
            print(self.data[1])
            if self.children:
                for child in self.children:
                    child.print_tree("designation")




def build_product_tree():
    root = TreeNode(("Nilupul","CEO"))
    Chinmey=TreeNode(("Chinmey","CTO"))
    Gels=TreeNode(("Gels","HR HEAD"))

    Vishwa=TreeNode(("Vishwa","Infrastructure Head"))
    Aamir=TreeNode(("Aamir","Application Head"))

    Peter=TreeNode(("Peter","Recruitment Manager"))
    Waqas=TreeNode(("Waqas","Policy Manager",))

    Dhaval=TreeNode(("Dhaval","Cloud Manager"))
    Abhijit=TreeNode(("Abhijit","App Manager"))

    root.add_child(Chinmey)
    root.add_child(Gels)
    Chinmey.add_child(Vishwa)
    Chinmey.add_child(Aamir)
    Aamir.add_child(Peter)
    Aamir.add_child(Waqas)
    Vishwa.add_child(Dhaval)
    Vishwa.add_child(Abhijit)

    root.print_tree("both") #printing based on name or designation or both
    root.print_tree("name")
    root.print_tree("designation")

if __name__=='__main__':
    build_product_tree()

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children=[]
        self.parent =None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0 
        p= self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("laptop")
    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("macbook"))
    laptop.add_child(TreeNode("Asus"))

    phone = TreeNode("phone")
    phone.add_child(TreeNode("Realme"))
    phone.add_child(TreeNode("MI"))
    phone.add_child(TreeNode("apple"))

    tv= TreeNode("tv")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("Panasonic"))



    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)

    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    pass

""" o/p- 

Electronics
   |__laptop
      |__Dell
      |__macbook
      |__Asus
   |__phone
      |__Realme
      |__MI
      |__apple
   |__tv
      |__Samsung
      |__Sony
      |__Panasonic



Electronics
   |--laptop
      |--Dell
      |--macbook
      |--Asus
   |--phone
      |--Realme
      |--MI
      |--apple
   |--tv
      |--Samsung
      |--Sony
      |--Panasonic

"""
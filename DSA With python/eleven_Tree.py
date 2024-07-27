class Tree:
    def __init__(self, data):
        self.parent=None
        self.children =[]
        self.data=data
    
    def add_child(self, child):
        child.parent=self
        self.children.append(child)
    
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_tree(self):
        spaces= '   ' * self.get_level()*3
        prefix= spaces+"|-- " if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
        


def build_product_tree():
    root= Tree('Electronics')

    laptop=Tree('Laptop')
    laptop.add_child(Tree('Mac'))
    laptop.add_child(Tree('Surface'))
    laptop.add_child(Tree('Thinkpad'))
    laptop.add_child(Tree('Tab'))

    tv= Tree("TV")
    tv.add_child(Tree('Samsung'))
    tv.add_child(Tree('LG'))
    tv.add_child(Tree('Sony'))

    cellphone=Tree('CellPhone')
    cellphone.add_child(Tree('iPhone'))
    cellphone.add_child(Tree('Samsung'))
    cellphone.add_child(Tree('Realme'))
    cellphone.add_child(Tree('Techno'))

    root.add_child(laptop)
    root.add_child(tv)
    root.add_child(cellphone)
    return root



if __name__=='__main__':
    root= build_product_tree()
    root.print_tree()
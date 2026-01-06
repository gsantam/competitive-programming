class Solution:
    def recurse(self,list_,depth):
        for element in list_:
            if element.isInteger():
                self.total+=depth*element.getInteger()
            else:
                self.recurse(element.getList(),depth+1)

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.total = 0
        self.recurse(nestedList,1)
        return self.total


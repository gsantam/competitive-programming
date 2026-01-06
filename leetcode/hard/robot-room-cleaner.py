class Solution:
    def def_from_to(self,robot,from_,to_):
        if to_[0]<from_[0]:
            move = robot.move()
        elif from_[0]<to_[0]:
            robot.turnLeft()
            robot.turnLeft()
            move = robot.move()
            robot.turnRight()
            robot.turnRight()
        elif to_[1]>from_[1]:
            robot.turnRight()
            move = robot.move()
            robot.turnLeft()
        else:
            robot.turnLeft()
            move = robot.move()
            robot.turnRight()
        if move:
            return to_
        return from_

    def cleanRoom(self, robot):
        robot.clean()
        stack = [(1,0),(0,1),(-1,0),(0,-1)]
        seen_with_prevs = {}
        current = [0,0]
        while stack:
            next_ = stack.pop()
            if next_ in seen_with_prevs:
                continue
            while not ((next_[0] == current[0] and abs(next_[1]-current[1])==1) or (next_[1] == current[1] and abs(next_[0]-current[0])==1)):
                current = self.def_from_to(robot,current,seen_with_prevs[current])
            current_next = self.def_from_to(robot,current,next_)
            if current_next!=current:
                robot.clean()
                seen_with_prevs[current_next] = current
                current = current_next
                stack+=[(current[0]+1,current[1]),(current[0],current[1]+1),(current[0]-1,current[1]),(current[0],current[1]-1)]

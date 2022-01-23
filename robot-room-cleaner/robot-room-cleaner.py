# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        
        """
        
        #let's assume the robot is facing downwards
        
        directions=[(1,0),(0,-1),(-1,0),(0,1)]
        
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            

        def letsclean(row,col,initial_direction):
            visited.add((row,col))
            robot.clean() 
            for i in range(4):
                d=(initial_direction+i) % 4
                newrow,newcol= row+ directions[d][0], col+ directions[d][1]
                if (newrow,newcol) not in visited and robot.move():
                    letsclean(newrow,newcol,d)
                    go_back()
                robot.turnRight() 
        visited = set()
        return letsclean(robot.row,robot.col,0)
                
                
            
        
        
import time

MAX_WIDTH_SIZE = 1120
MAX_HEIGTH_SIZE = int((900 / 100) * 80)
HITBOX_OFFSET_BUILDING = 10
HITBOX_OFFSET_WORKER = 5


class MobileService:
    def __init__(self, width: int = MAX_WIDTH_SIZE, height: int = MAX_HEIGTH_SIZE):
        self.__width = width
        self.__height = height

    def move_mobile(self, mobile):
        '''
        make mobile entity move of one step
        '''
        if mobile.road_to_destination:
            mobile.x += mobile.road_to_destination[0][0]
            mobile.y += mobile.road_to_destination[0][1]
            """"
            direction: int = 0
            if mobile.road_to_destination == [0, 1]:
                direction = 1
            elif mobile.road_to_destination == [0, -1]:
                direction = 2
            elif mobile.road_to_destination == [1, 0]:
                direction = 3
            elif mobile.road_to_destination == [-1, 0]:
                direction = 4
            elif mobile.road_to_destination == [1, 1]:
                direction = 5
            elif mobile.road_to_destination == [-1, -1]:
                direction = 6
            elif mobile.road_to_destination == [-1, 1]:
                direction = 7
            elif mobile.road_to_destination == [1, -1]:
                direction = 8
            """
            mobile.set_hitbox()
            mobile.road_to_destination.pop(0)

            if [mobile.x, mobile.y] == mobile.destination:
                mobile.destination = []
            # return direction

    def find_path(self, mobile):
        """
        f(n) = g(n) + h(n) is the minimum cost since the initial node to the objectives conditioned to go thought node n.
        g(n) is the minimum cost from the initial node to n.
        h(n) is the minimum cost from n to the closest objective to n

        In order to choose which square to move to next, we need to take into account 2 heuristics:
            1. The "g" value - This is how far away this node is from the departure point.
            2. The "h" value - This is how far away this node is from the destination point.
            3. The "f" value - This is the sum of the "g" value and the "h" value.
                        This is the final number which tells us which node to move to.

        In order to calculate these heuristics, this is the formula we will use:
        distance = abs(from.x - to.x) + abs(from.y - to.y)

        This is known as the "Manhattan Distance" formula.
        """
        possibility = [[]]
        offsets = [[]]

        departure = [mobile.x, mobile.y]

        offsets = [e for e in offsets if e]

        if (mobile.x > 0):
            possibility.append([departure[0] - 1, departure[1]])
            offsets.append([-1, 0])
            # as long as mobile.x is greater than 0, it can move to the left (-1,0)

        if (mobile.y + mobile.height < self.__height):
            possibility.append([departure[0], departure[1] + 1])
            offsets.append([0, 1])
            # as long as mobile.y+mobile.height is smaller than MAX_HEIGTH_SIZE, it can move to the bottom (0,+1)

        if (mobile.y + mobile.height < self.__height & mobile.x > 0):
            possibility.append([departure[0] - 1, departure[1] + 1])
            offsets.append([-1, 1])
            # as long as mobile.y+mobile.height is greater than MAX_HEIGTH_SIZE and mobile.x is greater than 0, it can move to the bottom left (-1,+1)

        if (mobile.y > 0):
            possibility.append([departure[0], departure[1] - 1])
            offsets.append([0, -1])
            # as long as mobile.y is greater than 0, it can move to the top (0,-1)
        if (mobile.x + mobile.width < self.__width):
            possibility.append([departure[0] + 1, departure[1]])
            offsets.append([1, 0])
            # as long as mobile.x+mobile.width is smaller than MAX_WIDTH_SIZE, it can move to the right (+1,0)

        if (mobile.x + mobile.width < self.__width & mobile.y > 0):
            possibility.append([departure[0] + 1, departure[1] - 1])
            offsets.append([1, -1])
            # as long as mobile.x+mobile.width is smaller than MAX_WIDTH_SIZE and mobile.y is greater than 0, it can move to the top right (+1,-1)

        if (mobile.y > 0 & mobile.x > 0):
            possibility.append([departure[0] - 1, departure[1] - 1])
            offsets.append([-1, -1])
            # as long as mobile.x is greater than 0 and mobile.y is greater than 0, it can move to the top left (-1,-1)

        if (mobile.x + mobile.width < self.__width & mobile.y + mobile.height < self.__height):
            # as long as mobile.x+mobile.width is smaller than MAX_WIDTH_SIZE and mobile.y+mobile.height is smaller than MAX_HEIGTH_SIZE , it can move to the bottom right (+1,0)
            possibility.append([departure[0] + 1, departure[1] + 1])
            offsets.append([1, 1])

        f = 0
        shortest = []
        chosen_move = []
        possibility = [e for e in possibility if e]

        counter: int = -1
        for position in possibility:

            counter += 1

            fbis = self.calculate_f_value(departure, position, mobile.destination)

            if (f == 0 or f > fbis):
                f = fbis
                ''' 
                 we keep the lowest f value
                '''
                chosen_move = offsets[counter]
                shortest = position
                '''
                then assign case with lowest f to shortest list ([x,y])
                '''
        mobile.current_step[0] += chosen_move[0]
        mobile.current_step[1] += chosen_move[1]

        mobile.road_to_destination = [e for e in mobile.road_to_destination if e]

        mobile.road_to_destination.append(chosen_move)

        ''' 
        once it's added we do the same from the next point (and at the end, we will have the complete road to reach the destination )
        '''

    def calculate_f_value(self, departure, position, destination):

        if (departure != [] or position != [] or destination != []):
            g = abs(departure[0] - position[0]) + abs(departure[1] - position[1])
            h = abs(position[0] - destination[0]) + abs(position[1] - destination[1])

            return g + h

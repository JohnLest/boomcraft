import random 


class Tools():
    ''' 
    Reunite all the usefull method
    '''
    def give_random_int_between(self, min: int, max: int) :
        ''' 
        :return an integer between min and max
        '''
        return random.randint(min,max)


    def give_random_name(self) :
        ''' 
        :return a name
        '''
        return "air v"
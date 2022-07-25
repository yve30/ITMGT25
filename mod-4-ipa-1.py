'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    social_graph = {"@bongolpoc":{"following":""},  
                    "@joaquin":{"following": ["@chums","@jobenilagan"]}, 
                    "@chums":{"following":["@bongolpoc","@miketan","@rudyang","@joeilagan"]},
                    "@jobenilagan":{"following":["@eeebeee","@joeilagan","@chums","@joaquin"]},
                    "@joeilagan":{"following":["@eeebeee","@jobenilagan","@chums"]},
                    "@eeebeee":{"following":["@jobenilagan","@joeilagan"]}
                    }
    
    from_following = to_member in social_graph[from_member]["following"]
    to_following = from_member in social_graph[to_member]["following"]
    
    if from_following == True and to_following == True:
        print("friends")
    elif from_following == True:
        print("follower")
    elif to_following == True:
        print("followed by")
    elif from_following == False and to_following == False:
        print("no relationship")

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if len(board) == 3:
        y = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    y.append(22)
                elif board[i][j] == 'O':
                    y.append(15)
                else:
                    y.append(0)
                    
        points = [y[k:k+3] for k in range (0, len(y), 3)]
        
        h_sums = [sum(v) for v in points]
        v_sums = [sum(v) for v in zip(*points)]
        diagonal_ud = sum([points[i][i] for i, n in enumerate(points)])
        diagonal_du = sum([points[2-i][i] for i, n in enumerate(points)])
        
        for i in h_sums:
            if i == 66:
                return print('X')
            elif i == 45:
                return print('O')
        for i in v_sums:
            if i == 66:
                return print('X')
            elif i == 45:
                return print('O')
        if diagonal_ud == 66:
                return print('X')
        if diagonal_ud == 45:
                return print('O')
        if diagonal_du == 66:
                return print('X')
        if diagonal_du == 45:
                return print('O')
        else:
                return print('No Winner')
    
    elif len(board) == 4:
        y = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    y.append(22)
                elif board[i][j] == 'O':
                    y.append(15)
                else:
                    y.append(0)
                    
        points = [y[k:k+4] for k in range (0, len(y), 4)]
        
        h_sums = [sum(v) for v in points]
        v_sums = [sum(v) for v in zip(*points)]
        diagonal_ud = sum([points[i][i] for i, n in enumerate(points)])
        diagonal_du = sum([points[2-i][i] for i, n in enumerate(points)])
        
        for i in h_sums:
            if i == 88:
                return print('X')
            elif i == 60:
                return print('O')
        for i in v_sums:
            if i == 88:
                return print('X')
            elif i == 60:
                return print('O')
        if diagonal_ud == 88:
                return print('X')
        if diagonal_ud == 60:
                return print('O')
        if diagonal_du == 88:
                return print('X')
        if diagonal_du == 60:
                return print('O')
        else:
                return print('No Winner')
    
    elif len(board) == 5:
        y = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    y.append(22)
                elif board[i][j] == 'O':
                    y.append(15)
                else:
                    y.append(0)
                    
        points = [y[k:k+5] for k in range (0, len(y), 5)]
        
        h_sums = [sum(v) for v in points]
        v_sums = [sum(v) for v in zip(*points)]
        diagonal_ud = sum([points[i][i] for i, n in enumerate(points)])
        diagonal_du = sum([points[2-i][i] for i, n in enumerate(points)])
        
        for i in h_sums:
            if i == 110:
                return print('X')
            elif i == 75:
                return print('O')
        for i in v_sums:
            if i == 110:
                return print('X')
            elif i == 75:
                return print('O')
        if diagonal_ud == 110:
                return print('X')
        if diagonal_ud == 75:
                return print('O')
        if diagonal_du == 110:
                return print('X')
        if diagonal_du == 75:
                return print('O')
        else:
                return print('No Winner') 
    
    elif len(board) == 6:
        y = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    y.append(22)
                elif board[i][j] == 'O':
                    y.append(15)
                else:
                    y.append(0)
                    
        points = [y[k:k+6] for k in range (0, len(y), 6)]
        
        h_sums = [sum(v) for v in points]
        v_sums = [sum(v) for v in zip(*points)]
        diagonal_ud = sum([points[i][i] for i, n in enumerate(points)])
        diagonal_du = sum([points[2-i][i] for i, n in enumerate(points)])
        
        for i in h_sums:
            if i == 132:
                return print('X')
            elif i == 90:
                return print('O')
        for i in v_sums:
            if i == 132:
                return print('X')
            elif i == 90:
                return print('O')
        if diagonal_ud == 132:
                return print('X')
        if diagonal_ud == 90:
                return print('O')
        if diagonal_du == 132:
                return print('X')
        if diagonal_du == 90:
                return print('O')
        else:
                return print('No Winner')
                          
def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    route_map = {("upd","admu"):{"travel_time_mins":10},
            ("admu","dlsu"):{"travel_time_mins":35},
            ("dlsu","upd"):{"travel_time_mins":55}}
    
    t = 0
    for y in route_map.keys():
        if y[0] == first_stop:
            if y[1] == second_stop:
                t = route_map[first_stop, second_stop]["travel_time_mins"]
                return t
            else:
                t += route_map[y]["travel_time_mins"]
                m = y[1]
                break
    for v in route_map.keys():
        if v[0] == m and v[1] == second_stop:
            t += route_map[v]["travel_time_mins"]
        return t        
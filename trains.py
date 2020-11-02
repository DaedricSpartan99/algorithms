from stack import Stack

"""
    config = configuration of the right rail order, python list
    kargs in:
        - stack : bool, if True it outputs S variable too
"""
def is_possible(config, **kargs):
    # re-initialize config as a Stack
    config = Stack(config)

    # side rail stack
    # use 0 as a sentinel
    S = Stack([0])
    
    # label = train expecting exiting from left side 
    label = len(config) 

    # apply the reverse order-time symmetry 
    while len(config) > 0:

        right = config.pop()

        """

            Find a way to solve the right popped train.
        
            A train is solved if:
                - the right side train can directly go to the left side
                - the right side train can't directly go to the left side, but the first line train in the side rail can

        """

        if right == label: 
            # right side train can pass
            label -= 1   # label solved
        else:
            if S.top() == label:
                # first line side rail train can pass
                S.pop() 
                label -= 1 # label solved
            else:
                # send right train to the side rail 
                S.push(right)

    # finalization, solve trains in the side rail
    while len(S) > 1 and S.top() == label:
        S.pop()
        label -= 1
    
    # output stack too if required
    if "stack" in kargs and kargs["stack"]:
        return (len(S) == 1, S)

    return len(S) == 1


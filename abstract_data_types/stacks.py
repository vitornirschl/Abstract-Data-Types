'''
Implements the Stack Abstract Data Type

Classes
-------
Stack
    Stack class with flexible length.

FixedStack
    Stack class with fixed maximum length.

Exceptions
----------
Empty
    When a stack is empty.
'''

class Empty(Exception):
    '''
    Exception class for empty stacks.
    '''

class Stack:
    '''
    A stack with flexible length.

    Attributes
    ----------
    stack : list
        A list with the itens in the stack.

    Methods
    -------
    is_empty():
        Checks if the stack is empty.
    push(item):
        Pushes item to the top of the stack.
    pop():
        Pops the top item of the stack.
    top():
        Returns the top item of the stack.
    '''
    def __init__(self):
        '''
        Initializes a Stack instance.
        '''
        self.stack = []

    def is_empty(self):
        '''
        Checks if the stack is empty.

        Returns
        -------
        Bool
            True if the stack is empty; False otherwise.
        '''
        if len(self.stack) == 0:
            return True
        return False

    def push(self, item):
        '''
        Pushes an item to the stack.

        Args
        ----
        item : object
            An item of any type to be pushed to the stack.
        '''
        self.stack.append(item)

    def pop(self):
        '''
        Pops the top item of the stack

        Returns
        -------
        object
            The item popped of the stack.

        Raises
        ------
        Empty
            If the stack is empty.
        '''
        if self.is_empty():
            raise Empty("Empty stack.")
        return self.stack.pop()

    def top(self):
        '''
        Returns the top item of the stack.

        Returns
        -------
        object
            The top item of the stack.

        Raises
        ------
        Empty
            If the stack is empty.
        '''
        if self.is_empty():
            raise Empty("Empty stack.")
        return self.stack[-1]

    def __str__(self):
        '''
        Returns the string representation of the stack.

        Returns
        -------
        string
            String representation of the stack.
        '''
        string = "("
        for element in self.stack:
            string.join(f"{element} ")
        string = string[:-1] + ")"
        return string

    def __repr__(self):
        '''
        Returns the abstract representation of the stack. 

        Returns
        -------
        string
            Abstract representation of the stack.
        '''
        return "Stack()"

class FixedStack:
    '''
    A stack with a fixed maximum length.

    Attributes
    ----------
    stack : list
        A list with the itens in the stack.
    max_length : int
        The maximum length of the stack.
    length : int
        The current lenght of the stack.

    Methods
    -------
    is_empty():
        Checks if the stack is empty.
    push(item):
        Push item to the top of the stack.
    pop():
        Pops the top item of the stack.
    top():
        Returns the top item of the stack.
    extend(new_length):
        Extends the stack to the new_length.
    '''
    def __init__(self, max_len=100):
        '''
        Initializes the stack.

        Args
        ----
        max_len : int
            The maximum length of the stack (Default value is 100).

        Raises
        ------
        TypeError
            If max_len is not an instance of int.
        ValueError
            If max_len is smaller or equal than zero.
        '''
        if not isinstance(max_len, int):
            raise TypeError("The maximum length of the stack must be an integer.")
        if max_len <= 0:
            raise ValueError("The maximum length must be an positive integer.")
        self.stack = [None] * max_len
        self.max_length = max_len
        self.length = 0

    def is_empty(self):
        '''
        Checks if the stack is empty.

        Returns
        -------
        Bool
            True if stack is empty; False otherwise.
        '''
        if self.length == 0:
            return True
        return False

    def push(self, item):
        '''
        Pushes item to the top of the stack.

        Args
        ----
        item : object
            Item of any type to be pushed to the top of the stack.
        
        Raises
        ------
        IndexError
            If the stack is full    
        '''
        if self.length == self.max_length:
            raise IndexError("The stack is full.")
        self.stack.append(item)
        self.length += 1

    def pop(self):
        '''
        Pops the top item from the stack.

        Returns
        -------
        object
            The top item from the stack.
        
        Raises
        ------
        Empty
            If the stack is empty.
        '''
        if self.is_empty():
            raise Empty("The stack is empty.")
        popped = self.stack[self.length - 1]
        self.stack[self.length - 1] = None
        return popped

    def top(self):
        '''
        The top element of the stack.

        Returns
        -------
        object
            The top element of the stack.

        Raises
        ------
        Empty
            If the stack is empty.
        '''
        if self.is_empty():
            raise Empty("The stack is empty.")
        return self.stack[self.length - 1]

    def extend(self, new_length):
        '''
        Extend the stack to the size new_length.

        Args
        ----
        new_length : int
            The new length of the stack.
        
        Raises
        ------
        TypeError
            If new_length is not an instance of int.
        ValueError
            If new_length is greater than the original length of the stack.
        '''
        if not isinstance(new_length, int):
            raise TypeError("The new length must be an integer.")
        if new_length <= self.max_length:
            raise ValueError("The new length must be greater than the original length of the" +
            "stack.")
        self.stack += [None] * (new_length - self.max_length)
        self.max_length = new_length

    def __str__(self):
        '''
        The string representation of the stack

        Returns
        -------
        string
            String representation of the stack.
        '''
        string = "("
        for i in range(self.length):
            string.join(f"{self.stack[i - 1]} ")
        string = string[:-1] + ")"
        return string

    def __repr__(self):
        '''
        The abstract representation of the stack. 

        Returns
        -------
        string
            Abstract representation of the stack.
        '''
        return f"FixedStack({self.max_length})"

    def __len__(self):
        '''
        Length of the stack.

        Returns
        -------
        length : int
            The length of the stack.
        '''
        return self.length

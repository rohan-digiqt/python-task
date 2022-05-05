'''

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType

'''

dt = 'Hello'                        # str
dt = 77                             # int
dt = 8.0                            # float

# A complex number has a real and imaginary part components.
dt = 8v                             # complex

dt = ['a','b']                      # list
dt = ('a','b')                      # tuple
dt = range(41)                      # range
dt = {"name":"Rohan", "age":20}     # dict
dt = {"a", "b", "c"}                # set
dt = frozenset({"a", "b", "c"})     # frozenset
dt = true                           # bool
dt = b'Hello'                       # bytes
dt = bytearray(10)                  # bytearray
dt  = memoryview(bytes(5))          # memoryview
dt = None                           # NoneType
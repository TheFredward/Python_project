print('hello World! Time to learn a new language\n \n')
# Request user name
inputName = input('Enter a name: ')
# display input
print('\n')
outName = inputName + ' Ready for this!?'
print(outName)
print('\n')
# ------
# Tuples NON MUTABLE: store variables but cannot modify, index access,
# Array and list: can modify elements, index access
# Dictionaries: similar to tuples but modifiable, values are stored based on keys
# ------
# tuples
size = (100, 200)
# finding the index and storing in width
width = size[0]
# take note of the comma after
new_size = size + (300,)
# Array
movement =  [5,-2,3,-4]
movement.append('text')
print(movement)
# dictionary
dictionaries = {'p0': 50, 'p2':23}
print(dictionaries.keys())
print(dictionaries['p2'])
# while # NOTE: continues to iterate until it is true
GV = False;
x_pos = 2;
eX_pos = 3;
final_pos = 12;
while not GV:
    print('x_pos: ');
    print( x_pos);
    print('\n')
    print('eX_pos: ');
    print(eX_pos)
    if x_pos == eX_pos:
        print('You lose')
        GV = True;
    elif x_pos >= final_pos:
        print('You win')
        GV = True
    else:
        x_pos += 3;
        eX_pos += 1;

def print_vector(x,y,z):
    print('<%s, %s, %s>' %(x,y,z))

list_vec=[1,2,3]
tuple_vec=(1,2,3)
dict_vec={'x':1, 'y':2, 'z':3}
dict_vec2={'x':2, 'y':1, 'z':3}

#for lists and tuples
print_vector(*list_vec)
print_vector(*tuple_vec)

#for dictionary
print_vector(**dict_vec)
#the key and the name of the argument must match
print_vector(**dict_vec2)

#this yields an error
#print_vector(**{'x':1, 'y':2, 'z':3,'c':5})
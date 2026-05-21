### Create a Matrix class with rich Python behavior.

import logging

class Matrix:

    def __init__(self, matrix):

        if len(matrix) == 0:
            raise ValueError("The object provided doesnt meet the requirements.")

        for row in matrix:
            if ( len(row) ) != len(matrix[0]):
                raise ValueError("Rows must all have the same length")
            
        self.matrix = tuple( tuple(row) for row in matrix )

    def __repr__(self):
        rows = ",\n     ".join( str(row) for row in self.matrix )
        return f"Matrix([\n     {rows}\n])" 

    def __str__(self):

        return "\n".join( "[" + " ".join(map(str, row)) + "]" for row in self.matrix)

    def __len__(self):

        return len(self.matrix)

    @property
    def shape(self):

        rows = len(self.matrix)
        columns = len(self.matrix[0])
        return (rows, columns)

    def __getitem__(self, key):

        if isinstance(key, tuple):
            row, col = key
            return self.matrix[row][col]

        return self.matrix[key]

    def __add__(self, other):

        if not isinstance(other, Matrix):
            return NotImplemented

        rows, cols = self.shape

        if len(other.matrix) != rows:
            raise ValueError("The number of rows doesnt match")
        if len(other.matrix[0]) != cols:
            raise ValueError("The number of columns doesnt match")

        new_matrix = []

        for row in range(rows):
            new_row = []
            for col in range(cols):
                new_row.append( self.matrix[row][col] + other.matrix[row][col] ) 
            new_matrix.append( new_row )

        return Matrix(new_matrix)

    def __mul__(self, scalar):

        if not isinstance(scalar, int):
            raise ValueError("The scalar isnt a number")

        rows, cols = self.shape
        new_matrix = []

        for row in range(rows):
            new_row = []
            for col in range(cols):
                new_row.append( self.matrix[row][col] * scalar )
            new_matrix.append(new_row)

        return Matrix(new_matrix)

    __rmul__ = __mul__

    def __matmul__(self, other):

        if not isinstance(other, Matrix):
            return NotImplemented

        rows_a, cols_a = self.shape
        rows_b, cols_b = other.shape

        if cols_a != rows_b:
            raise ValueError("Incompatible matrix dimensions")

        result = []
        for row in range(rows_a):
    
            new_row = []
            for col in range(cols_b):
        
                value = sum(
                    self.matrix[row][k] * other.matrix[k][col] for k in range(cols_a)
                )
    
                new_row.append(value)
        
            result.append(new_row)

        return Matrix(result)
        
    def __eq__(self, other):

        if not isinstance(other, Matrix):
            return NotImplemented

        return self.matrix == other.matrix

    def __bool__(self):
        return any ( value != 0 for row in self.matrix for value in row)

    @property
    def T(self):
        
        new_matrix = []

        for row in range( len(self.matrix[0]) ):
            new_row = []

            for col in range( len(self.matrix) ):
                new_row.append(self.matrix[col][row]) 

            new_matrix.append(new_row)                 

        return Matrix(new_matrix)

    def __iter__(self):
        return iter(self.matrix)

matrix = Matrix([[1,2,3], [4,5,6], [7,8,9]])    
other = Matrix([[2,2,2], [3,3,3], [4,4,4]])    

logging.warning(f"%r", matrix)
print( matrix )
print( len(matrix) )
print( matrix.shape )
print( matrix[1][2], matrix[2] )
print( matrix + other )
print( matrix * 3 )
print( matrix @ other )
print( matrix == other )
print( matrix.T )
for element in matrix:
    print(element)
print( matrix[1][2] )


__author__ = "Miqueas Garcia Gonzalez"
__copyright__ = "-"
__credits__ = ["-"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Miqueas Garcia Gonzalez"
__email__ = "coding4canary@gmail.com"
__status__ = "Development"

from array import *

class Matrix:
  """
  Este modulo es responsable de almacenar, consultar, modificar, operar y 
  mostrar matrices sin necesidad del empleo de la biblioteca numpy.

  Funciones:
    Operadores básicos: +, -, *, /, t
  """
  
  def __init__(self, dims = (0,0)):

    self._n_rows = dims[0]
    self._n_columns = dims[1]
    self.matrix = [[0] * self.n_columns for i in range(self.n_rows)]
  
  @property #Podemos acceder a este metodo como si fuera un atributo
  def n_rows(self):
    return self._n_rows
  
  @property
  def n_columns(self):
    return self._n_columns

  @n_rows.setter
  def n_rows(self, rows):
    self._n_rows = rows

  @n_columns.setter
  def n_columns(self, columns):
    self._n_columns = columns

  def set_value(self, posi , posj, value):
    self.matrix[posi][posj] = value

  #Sobrecarga operador +
  def __add__(self, other: Matrix) -> Matrix:
    """Suma de matrices del tipo C = A + B, donde A, B y C tienen las mismas
       dimensiones.

    Args:
      self: el propio objeto matriz (operador de la izquierda).
      other: otra matriz (operador de la derecha).

    Returns:
      bool: devuelve falso solo si las matrices no tienen las mismas dimensiones.
      Matrix: devuelve un objeto de tipo Matrix resultante de la suma de matrices.
    """
    if isinstance (other, Matrix):
      if self.n_columns != other.n_columns:
        return False
      elif self.n_rows != other.n_rows:
        return False
      else:
        aux = Matrix((self.n_rows, self.n_columns))
        for i in range(self.n_rows):
        # iterate through columns
          for j in range(self.n_columns):
            aux[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return aux
    else:
      return False

  #Sobrecarga operador -
  def __sub__(self, other: Matrix) -> Matrix:
    """Resta de matrices del tipo C = A - B, donde A, B y C tienen las mismas
       dimensiones.

    Args:
      self: el propio objeto matriz (operador de la izquierda).
      other: otra matriz (operador de la derecha).

    Returns:
      bool: devuelve falso solo si las matrices no tienen las mismas dimensiones.
      Matrix: devuelve un objeto de tipo Matrix resultante de la resta de matrices.
    """
    if isinstance (other, Matrix):
      if self.n_columns != other.n_columns:
        return False
      elif self.n_rows != other.n_rows:
        return False
      else:
        aux = Matrix((self.n_rows, self.n_columns))
        for i in range(self.n_rows):
        # iterate through columns
          for j in range(self.n_columns):
            aux[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return aux
    else:
      return False

  #Sobrecarga operdaor *
  def __mul__(self, other: Matrix) -> Matrix:
    """Multiplicacion de matrices del tipo C = A x B donde:
        A(k x m)
        B(m x n)
        C(k x n)

    Args:
      self: el propio objeto matriz (operador de la izquierda).
      other: otra matriz (operador de la derecha).

    Returns:
      bool: devuelve falso solo si las matrices no cumplen requisitos para mult.
      Matrix: devuelve un objeto de tipo Matrix resultante de la resta de matrices.
    """
    if isinstance (other, Matrix):
      if self.n_columns != other.n_rows:
        return False
      else:
        aux = Matrix((self.n_rows, self.n_columns))
        for i in range(self.n_rows):
          for j in range(other.n_columns):
            for z in range(other.n_columns):
              aux[i][j] += self.matrix[i][z] * other.matrix[z][j]
        return aux
    else:
      return False

  def __del__(self):
    print()

  pass


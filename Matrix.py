__author__ = "Miqueas Garcia Gonzalez"
__copyright__ = "-"
__credits__ = ["-"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Miqueas Garcia Gonzalez"
__email__ = "coding4canary@gmail.com"
__status__ = "Development"

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
    self.A = [[0] * self.n_columns for _ in range(self.n_rows)]
  
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

  def __class_set_item__(self, posi , posj, value):
    self.A[posi][posj] = value

  def __class_del_item__(self, posi , posj):
    self.A[posi][posj] = 0

  def __class_get_item__(self, posi , posj):
    return self.A[posi][posj]

  #Sobrecarga operador +
  def __add__(self, other: Matrix) -> Matrix:
    """Suma de matrices del tipo C = A + B, donde A, B y C tienen las mismas
       dimensiones.

    Args:
      self: el propio objeto matriz (operador de la izquierda).
      other: otra matriz (operador de la derecha).

    Returns:
      Matrix: devuelve un objeto de tipo Matrix resultante de la suma de matrices.
    """
    if isinstance (other, Matrix) and (self.n_columns == other.n_columns) and (self.n_rows == other.n_rows):
      aux = Matrix((self.n_rows, self.n_columns))
      for i in range(self.n_rows):
        for j in range(self.n_columns):
          aux.__class_set_item__(i,j, self.A[i][j] + other.A[i][j])
      return aux

  #Sobrecarga operador -
  def __sub__(self, other: Matrix) -> Matrix:
    """Resta de matrices del tipo C = A - B, donde A, B y C tienen las mismas
       dimensiones.

    Args:
      self: el propio objeto matriz (operador de la izquierda).
      other: otra matriz (operador de la derecha).

    Returns:
      Matrix: devuelve un objeto de tipo Matrix resultante de la resta de matrices.
    """
    if isinstance (other, Matrix) and (self.n_columns == other.n_columns) and (self.n_rows == other.n_rows):
      aux = Matrix((self.n_rows, self.n_columns))
      for i in range(self.n_rows):
        for j in range(self.n_columns):
          aux.__class_set_item__(i, j, self.A[i][j] - other.A[i][j])
      return aux

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
      Matrix: devuelve un objeto de tipo Matrix resultante de la resta de matrices.
    """
    if isinstance (other, Matrix) and (self.n_columns == other.n_rows):
      aux = Matrix((self.n_rows, self.n_columns))
      for i in range(self.n_rows):
        for j in range(other.n_columns):
          for z in range(other.n_columns):
            aux.__class_set_item__(i, j, (aux.__class_get_item__(i, j) + (self.A[i][z] * other.A[z][j])))
      return aux

  def __del__(self):
    print()



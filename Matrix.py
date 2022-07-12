__author__ = "Miqueas García González"
__copyright__ = "-"
__credits__ = ["-"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Miqueas García González"
__email__ = "coding4canary@gmail.com"
__status__ = "Development"

class Matrix:
  def __init__(self, rows = 0, columns = 0):
    self._n_rows = rows
    self._n_columns = columns
  
  @property #Podemos acceder a este método como si fuera un atributo
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

  def __del__(self):
    print()

  pass
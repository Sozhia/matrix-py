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
    self.n_rows = rows
    self.n_columns = columns
  
  def get_rows(self):
    return self.n_rows
  
  def get_columns(self):
    return self.n_columns

  def set_rows(self, rows):
    self.n_rows = rows

  def set_columns(self, columns):
    self.n_columns = columns

    
  pass
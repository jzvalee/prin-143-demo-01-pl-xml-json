import py_serializable

@py_serializable.serializable_class
class Entertainment:
  def __init__(self, *, Title: str, Genre: str, Length: str, Rated: str, Price: str) -> None:
    self._Title = Title
    self._Genre = Genre
    self._Length = Length
    self._Rated = Rated
    self._Price = Price

  @property
  def Title(self) -> str:
    return self._Title
  
  @property
  def Genre(self) -> str:
    return self._Genre
  
  @property
  def Length(self) -> str:
    return self._Length
  
  @property
  def Rated(self) -> str:
    return self._Rated
  
  @property
  def Price(self) -> str:
    return self._Price
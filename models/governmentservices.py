import py_serializable

@py_serializable.serializable_class
class GovernmentServices:
  def __init__(self, *, Name: str, Age: str, Platform: str, Record: str, Vote: str) -> None:
    self._Name = Name
    self._Age = Age
    self._Platform = Platform
    self._Record = Record
    self._Vote = Vote

  @property
  def Name(self) -> str:
    return self._Name
  
  @property
  def Age(self) -> str:
    return self._Age
  
  @property
  def Platform(self) -> str:
    return self._Platform
  
  @property
  def Record(self) -> str:
    return self._Record
  
  @property
  def Vote(self) -> str:
    return self._Vote
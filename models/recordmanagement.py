import py_serializable

@py_serializable.serializable_class
class RecordManagement:
  def __init__(self, *, StudentNumber: str, Name: str, Age: str, Section: str, TuitionPlan: str) -> None:
    self._StudentNumber = StudentNumber
    self._Name = Name
    self._Age = Age
    self._Section = Section
    self._TuitionPlan = TuitionPlan

  @property
  def StudentManager(self) -> str:
    return self._StudentNumber
  
  @property
  def Name(self) -> str:
    return self._Name
  
  @property
  def Age(self) -> str:
    return self._Age
  
  @property
  def Section(self) -> str:
    return self._Section
  
  @property
  def TuitionPlan(self) -> str:
    return self._TuitionPlan
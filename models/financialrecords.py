import py_serializable

@py_serializable.serializable_class
class FinancialRecords:
  def __init__(self, *, Number: str, Name: str, Balance: str, PhoneNumber: str, Debt: str) -> None:
    self._Number = Number
    self._Name = Name
    self._Balance = Balance
    self._PhoneNumber = PhoneNumber
    self._Debt = Debt

  @property
  def Number(self) -> str:
    return self._Number
  
  @property
  def Name(self) -> str:
    return self._Name
  
  @property
  def expiry(self) -> str:
    return self._Balance
  
  @property
  def batchNumber(self) -> str:
    return self._PhoneNumber
  
  @property
  def Debt(self) -> str:
    return self._Debt
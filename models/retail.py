import py_serializable

@py_serializable.serializable_class
class Retail:
  def __init__(self, *, brandName: str, price: str, expiry: str, batchNumber: str, category: str) -> None:
    self._brandName = brandName
    self._price = price
    self._expiry = expiry
    self._batchNumber = batchNumber
    self._category = category

  @property
  def brandName(self) -> str:
    return self._brandName
  
  @property
  def price(self) -> str:
    return self._price
  
  @property
  def expiry(self) -> str:
    return self._expiry
  
  @property
  def batchNumber(self) -> str:
    return self._batchNumber
  
  @property
  def category(self) -> str:
    return self._category
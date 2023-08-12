import pandas as pd
import numpy as np

class dbAccess():
  _dataJsonFull = None

  def __init__(self) -> None:
    self._dataJsonFull = pd.read_json("/home/gavin/Development/gavin_technical_test/app/data/db.json")

  def readAllRecords(self) -> pd.DataFrame:
    return self._dataJsonFull
  
  def readOneUser(self, userId) -> pd.DataFrame:
    return self._dataJsonFull[self._dataJsonFull["uid"] == userId]

  def readOneUserOneSession(self, userId, sessionId)  -> pd.DataFrame :
    return self._dataJsonFull[self._dataJsonFull["uid"] == userId and self._dataJsonFull["sid"] == sessionId]
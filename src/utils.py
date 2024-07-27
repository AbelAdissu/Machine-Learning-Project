import os
import sys
import joblib
from src.exception import CustomException

def save_object(file_path: str, obj) -> None:
    """
    Save the given object to the specified file path using joblib.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        joblib.dump(obj, file_path)
    except Exception as e:
        raise CustomException(e, sys)

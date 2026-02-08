

from typing import List, Optional
from pydantic import BaseModel



class FeedbackCreate(BaseModel):
    content:str
    feedback_type:FeedbackType
    metadata:dict={}
    user_id:Optional[str]=None
    

    
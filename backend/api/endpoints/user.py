from typing import List, Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend import schemas
from backend.api import deps
from backend import crud

router = APIRouter()

from typing import Dict, Any, Optional

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from backend.db.base_class import Base


class Meta(BaseModel):
    status_code: int = 200
    message: str = "Ok"


class CommonResponseSchema(BaseModel):
    meta: Meta
    data: Optional[Any] = None


class CommonResponse(JSONResponse):
    def __init__(
        self,
        status_code=None,
        message="Success",
        data=None,
        headers=None,
        media_type=None,
    ) -> JSONResponse:

        jsonable_data = jsonable_encoder(data) if data else None

        default_content = CommonResponseSchema(
            meta=Meta(status_code=status_code, message=message), data=jsonable_data
        ).model_dump()

        super().__init__(
            content=default_content,
            status_code=status_code,
            headers=headers,
            media_type=media_type,
        )

    @staticmethod
    def schema():
        return CommonResponseSchema

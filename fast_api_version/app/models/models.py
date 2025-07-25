from pydantic import BaseModel, Field
from typing import Optional

class ReportRequest(BaseModel):
    files: list[str] = Field(
        ...,
        example=["app/test_logs/example1.log"],
        description="Список путей к лог-файлам внутри контейнера"
    )
    
    report: str = Field(
        ...,
        example="average",
        description="Тип отчета (сейчас доступен только 'average')"
    )

    date: Optional[str] = Field(
        None,
        example="2025-06-22",
        description="Фильтр по дате (формат: YYYY-MM-DD)"
    )

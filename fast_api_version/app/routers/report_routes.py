from fastapi import APIRouter
from app.models.models import ReportRequest
from app.services.log_parser import LogParser
from app.controllers.main_controller import MainController
import logging

router = APIRouter()
logger = logging.getLogger("api")

@router.post("/generate_average_report")
def generate_report(request: ReportRequest):
    """Создает average отчёт"""

    log_parser = LogParser(logger, request.files, request.date)
    controller = MainController(request.report, log_parser, logger)
    data = controller.run()
    return {"report": data}

from documentation import Doc
from api import Api
import justpy as jp


jp.Route("/api", Api.serve)
jp.Route("/", Doc.serve)

jp.justpy()

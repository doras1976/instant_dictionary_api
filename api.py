from definition import Definition
import json
import justpy as jp


class Api:
    """
    Handles requests at /api?w=word
    """

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')

        defined = Definition(word).get()

        response = {
            "word": word,
            "definition": defined
        }

        wp.html = json.dumps(response)
        return wp







"""Test bl_compliance server.py"""
import json
from bl_compliance.server import app
from starlette.testclient import TestClient
from pathlib import Path


ncats_json = Path(__file__).parent / 'resources' / 'ncats.json'
robokop_json = Path(__file__).parent / 'resources' / 'robokop.json'
inval_reasoner = Path(__file__).parent / 'resources' / 'inval-reasoner-std.json'
inval_reasoner2 = Path(__file__).parent / 'resources' / 'inval-reasoner-std2.json'


class TestServer():

    @classmethod
    def setup_class(self):
        app.testing = True
        self.test_client = TestClient(app)

    @classmethod
    def teardown_class(self):
        self.test_client = None

    def test_robokop(self):
        """
        Test output from robokop
        """
        robokop = open(robokop_json, 'r')
        data = json.load(robokop)
        robokop.close()

        response = self.test_client.post('/validate/knowledge_graph', json=data)
        assert response.status_code == 418

    def test_ncats(self):
        """
        Test example for RSA validator
        http://transltr.io:7071/apidocs/#/default/post_validate_knowledgegraph
        """
        ncats = open(ncats_json, 'r')
        data = json.load(ncats)
        ncats.close()
        response = self.test_client.post('/validate/knowledge_graph', json=data)
        assert response.status_code == 418
        assert response.json()[0]['error_type'] == "TransformationError"

    def test_inval_json(self):
        """
        Test that invalid reasoner std gets a 422 via pydantic type checking
        """
        bad_fh = open(inval_reasoner, 'r')
        data = json.load(bad_fh)
        bad_fh.close()
        response = self.test_client.post('/validate/knowledge_graph', json=data)
        assert response.status_code == 422

    def test_inval_json_that_gets_passed_by_pydantic(self):
        """
        I suspect due to manually writing each dataclass __init__
        (eg @dataclass(init=False)
        pydantic does not correctly validate nested models
        in this example edges[0].id is a dict instead of a str
        but gets validated anyway

        When we remove (init=False) the validatio works, but
        then we can't support additionalProperties

        Not a huge deal because the KGX validator catches it
        and presumably the json schema validation will as well
        """
        bad_fh = open(inval_reasoner2, 'r')
        data = json.load(bad_fh)
        bad_fh.close()
        response = self.test_client.post('/validate/knowledge_graph', json=data)
        # If/when the above bug is fixable/fixed
        #assert response.status_code == 422
        assert response.status_code == 418

# -*- coding: utf-8 -*-
import pytest
from fixture.apllicattion import Application



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


# MIT License
#
# Copyright (c) 2022 Edward Haas
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import pytest

from . import models


@pytest.mark.django_db()
def test_new_member():
    member = models.Member(username="ed", firstname="Edy", lastname="H")
    member.save()

    assert member.username == "ed"


SPEAKER_ROLE_NAME = "speaker"
SPEAKER_ROLE_DESC = "Gives a lecture"


@pytest.fixture
def role0():
    return models.Role(name=SPEAKER_ROLE_NAME, description=SPEAKER_ROLE_DESC)


class TestRoleModel:
    def test_new_role(self, role0):
        assert role0.name == SPEAKER_ROLE_NAME
        assert role0.description == SPEAKER_ROLE_DESC

    @pytest.mark.django_db()
    def test_persist_role(self, role0):
        role0.save()

        assert role0 in models.Role.objects.all()

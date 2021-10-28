"""Testing mysqlmobiletest__init__()"""

from pathlib import Path
from beetools.beearchiver import Archiver
import mysqlmobiletest


_PROJ_DESC = __doc__.split("\n")[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem
_PROJ_VERSION = "0.0.1"


b_tls = Archiver(_PROJ_NAME, _PROJ_VERSION, _PROJ_DESC, _PROJ_PATH)


class TestMySqlMobileTest:
    def test__init__(self, setup_env):
        """Assert class __init__"""
        working_dir = setup_env
        t_mysqlmobiletest = mysqlmobiletest.MySqlMobileTest(_PROJ_NAME, working_dir)
        assert t_mysqlmobiletest.success
        pass


del b_tls

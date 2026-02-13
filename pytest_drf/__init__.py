from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pytest-drf")
except PackageNotFoundError:
    __version__ = "0.0.0"  # or raise, depending on your preference


from .authentication import *
from .authorization import *
from .pagination import *
from .status import *
from .views import *

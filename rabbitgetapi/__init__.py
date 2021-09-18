# Copyleft 2021 Sidon Duarte and contributors


__all__ = (
    "__title__",
    "__summary__",
    "__uri__",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
)

__copyright__ = "Copyright 2021 Sidon Duarte and individual contributors"

import importlib_metadata

metadata = importlib_metadata.metadata("rabbitgetapi-sdn")

__title__ = metadata["name"]
__summary__ = metadata["summary"]
__uri__ = metadata["home-page"]
__version__ = metadata["version"]
__author__ = metadata["author"]
__email__ = metadata["author-email"]
__license__ = metadata["license"]

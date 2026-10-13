import importlib
import pkgutil

from services.sources.base import BaseSource
import services.sources as sources


class SourceRegistry:
    sources: dict[str, BaseSource] = dict()

    def __init__(self):
        for _, module_name, _ in pkgutil.iter_modules(sources.__path__):
            if module_name == "base":
                continue
            importlib.import_module(f"services.sources.{module_name}")

        for subclass in BaseSource.__subclasses__():
            self.sources[subclass.registery_name] = subclass()

    def get_source(self, source_name: str) -> BaseSource | None:
        return self.sources.get(source_name)


SOURCE_REGISTRY = SourceRegistry()

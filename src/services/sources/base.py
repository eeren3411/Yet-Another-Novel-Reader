from abc import ABC, abstractmethod

from models import Novel, NovelContent


class BaseSource(ABC):
    registery_name: str

    @abstractmethod
    async def list_novels(self) -> list[Novel]:
        pass

    @abstractmethod
    async def search_novels(self, query: str) -> list[Novel]:
        pass

    @abstractmethod
    async def get_novel_content(self, novel_id: str) -> NovelContent:
        pass

    @abstractmethod
    async def get_chapter_content(self, novel_id: str, chapter_id: str) -> str:
        pass

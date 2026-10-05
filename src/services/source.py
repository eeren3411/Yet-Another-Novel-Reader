from abc import ABC, abstractmethod
from models import Novel, NovelContent, Chapter


class BaseSource(ABC):
    @abstractmethod
    def list_novels(self) -> list[Novel]:
        pass

    @abstractmethod
    def search_novels(self, query: str) -> list[Novel]:
        pass

    @abstractmethod
    def get_novel_content(self, novel_id: str) -> NovelContent:
        pass

    @abstractmethod
    def get_chapter_content(self, novel_id: str, chapter_id: str) -> str:
        pass


class MockSource(BaseSource):
    NOVELS = [
        Novel(id="novel_11", title="Novel 1"),
        Novel(id="novel_2", title="Novel 2"),
        Novel(id="novel_3", title="Novel 3"),
    ]

    NOVEL_CONTENTS = {
        "novel_1": NovelContent(
            id="novel_1",
            title="Novel 1",
            description="Novel 1 Description",
            chapters=[
                Chapter(id="chapter_1", title="Novel 1 Chapter 1"),
                Chapter(id="chapter_2", title="Novel 1 Chapter 2"),
            ],
        ),
        "novel_2": NovelContent(
            id="novel_2",
            title="Novel 2",
            description="Novel 2 Description",
            chapters=[
                Chapter(id="chapter_1", title="Novel 2 Chapter 1"),
                Chapter(id="chapter_2", title="Novel 2 Chapter 2"),
            ],
        ),
        "novel_3": NovelContent(
            id="novel_3",
            title="Novel 3",
            description="Novel 3 Description",
            chapters=[
                Chapter(id="chapter_1", title="Novel 3 Chapter 1"),
                Chapter(id="chapter_2", title="Novel 3 Chapter 2"),
            ],
        ),
    }

    CHAPTER_CONTENTS = {
        ("novel_1", "chapter_1"): "Novel 1 Chapter 1 Content",
        ("novel_1", "chapter_2"): "Novel 1 Chapter 2 Content",
        ("novel_2", "chapter_1"): "Novel 2 Chapter 1 Content",
        ("novel_2", "chapter_2"): "Novel 2 Chapter 2 Content",
        ("novel_3", "chapter_1"): "Novel 3 Chapter 1 Content",
        ("novel_3", "chapter_2"): "Novel 3 Chapter 2 Content",
    }

    def list_novels(self) -> list[Novel]:
        return self.NOVELS

    def search_novels(self, query: str) -> list[Novel]:
        return [novel for novel in self.NOVELS if query in novel.title]

    def get_novel_content(self, novel_id: str) -> NovelContent:
        return self.NOVEL_CONTENTS[novel_id]

    def get_chapter_content(self, novel_id: str, chapter_id: str) -> str:
        return self.CHAPTER_CONTENTS[(novel_id, chapter_id)]

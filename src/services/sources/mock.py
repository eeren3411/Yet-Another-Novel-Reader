from lorem import get_paragraph

from services.sources.base import BaseSource
from models import Novel, NovelContent, Chapter


class MockSource(BaseSource):
    registery_name = "mock"

    @property
    def mock_novel_list(self) -> list[Novel]:
        return [
            Novel(
                source=self.registery_name,
                id=f"novel_{i}",
                title=f"Novel {i}",
            )
            for i in range(10)
        ]

    async def list_novels(self) -> list[Novel]:
        return self.mock_novel_list

    async def search_novels(self, query: str) -> list[Novel]:
        return [novel for novel in self.mock_novel_list if query in novel.title]

    async def get_novel_content(self, novel_id: str) -> NovelContent:
        return NovelContent(
            source=self.registery_name,
            id=novel_id,
            title=f"Novel {novel_id.split('_')[-1]}",
            description=f"Description of {novel_id}, {get_paragraph()}",
            chapters=[
                Chapter(
                    source=self.registery_name,
                    novel_id=novel_id,
                    id=f"chapter_{i}",
                    title=f"Chapter {i}",
                )
                for i in range(10)
            ],
        )

    async def get_chapter_content(self, novel_id: str, chapter_id: str) -> str:
        return f"Content of {novel_id}: {chapter_id}, {get_paragraph()}"

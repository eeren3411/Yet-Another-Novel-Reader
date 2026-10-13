from dataclasses import dataclass


@dataclass
class Novel:
    source: str
    id: str
    title: str


@dataclass
class NovelContent(Novel):
    description: str
    chapters: list["Chapter"]


@dataclass
class Chapter:
    source: str
    novel_id: str
    id: str
    title: str

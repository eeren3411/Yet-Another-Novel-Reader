from dataclasses import dataclass


@dataclass
class Novel:
    id: str
    title: str


@dataclass
class NovelContent(Novel):
    description: str
    chapters: list["Chapter"]


@dataclass
class Chapter:
    id: str
    title: str

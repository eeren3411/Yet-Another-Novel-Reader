from services.source import MockSource

if __name__ == "__main__":
    source = MockSource()
    novels = source.list_novels()
    print(novels)
    novel_content = source.get_novel_content("novel_1")
    print(novel_content)
    chapter_content = source.get_chapter_content("novel_1", "chapter_1")
    print(chapter_content)

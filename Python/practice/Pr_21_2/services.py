"""
Сервисный слой.

BookFileParser отвечает ТОЛЬКО за превращение одной строки CSV в Book
(или None, если строка мусорная). Не знает ничего про БД.

BookLoader отвечает за оркестрацию: читает файл построчно, отдаёт
строки парсеру, готовые объекты — репозиторию. Не знает ничего про
формат CSV.

Разделение важно: если завтра формат файла изменится на JSON —
меняется только Parser. Если поменяется способ сохранения — только
Repository. BookLoader не тронется вообще.
"""
from decimal import Decimal, InvalidOperation

from models import Book
from repositories import BookRepository


class BookFileParser:
    REQUIRED_FIELDS = 4

    def parse_line(self, raw_line: str, is_first_line: bool = False) -> Book | None:
        line = raw_line.strip()
        if not line:
            return None

        if is_first_line and line.lower().startswith("title"):
            return None  # заголовок CSV — не книга

        parts = [p.strip() for p in line.split(",")]
        if len(parts) != self.REQUIRED_FIELDS:
            return None

        title, author, price_str, stock_str = parts
        try:
            price = Decimal(price_str)
            stock = int(stock_str)
        except (InvalidOperation, ValueError):
            return None

        return Book(title=title, author=author, price=price, stock=stock)


class BookLoader:
    def __init__(self, repository: BookRepository, parser: BookFileParser | None = None):
        self.repository = repository
        self.parser = parser or BookFileParser()

    def load_from_file(self, filename: str) -> int:
        added = 0
        with open(filename, "r", encoding="utf-8") as file:
            for i, line in enumerate(file):
                book = self.parser.parse_line(line, is_first_line=(i == 0))
                if book is None:
                    continue
                self.repository.save(book)
                added += 1
        return added

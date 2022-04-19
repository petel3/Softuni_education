from project.library import Library
from unittest import TestCase,main
class Test(TestCase):
    def setUp(self) -> None:
        self.library=Library("Library")

    def test_initialization_should_rises_error_for_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            library=Library ("")
        self.assertEqual("Name cannot be empty string!",str(ex.exception))

    def test_initialization_all_atributes(self):
        self.assertEqual("Library",self.library.name)
        self.assertEqual({},self.library.readers)
        self.assertEqual({},self.library.books_by_authors)

    def test_adding_book_by_author(self):
        author="Author"
        self.library.add_book(author,"Title1")
        self.library.add_book(author, "Title2")
        self.assertEqual(1,len(self.library.books_by_authors))
        self.assertEqual(2,len(self.library.books_by_authors[author]))

    def test_add_reader_if_it_is_not_in_readers(self):
        reader="Kiro"
        self.library.add_reader(reader)
        self.assertEqual(1,len(self.library.readers))

    def test_add_reader_error_when_try_to_add_reader_with_same_name(self):
        reader="Pesho"
        self.library.add_reader(reader)
        self.assertEqual(f"{reader} is already registered in the {self.library.name} library.",self.library.add_reader(reader))

    def test_rent_book_if_reader_not_registered(self):
        self.library.readers="Test"
        self.library.books_by_authors["Author"]="Title"
        reader_name="Test1"
        author="Author"
        title="Title"
        self.assertEqual(f"{reader_name} is not registered in the {self.library.name} "
                         f"Library.",self.library.rent_book(reader_name,author,title))

    def test_rent_book_if_author_not_registered(self):
        self.library.readers = "Test"
        self.library.books_by_authors["Author"] = "Title"
        reader_name = "Test"
        author = "Author1"
        title = "Title"
        self.assertEqual(f"{self.library.name} Library does not have any {author}"
                         f"'s books.", self.library.rent_book(reader_name, author, title))
    def test_rent_book_if_title_not_registered(self):
        self.library.readers = "Test"
        self.library.books_by_authors["Author"] = "Title"
        reader_name = "Test"
        author = "Author"
        title = "Title1"
        self.assertEqual(f"""{self.library.name} Library does not have {author}'s "{title}".""", self.library.rent_book(reader_name, author, title))

    def test_rent_book_after_rent_a_book_to_remove_it_from_library(self):

        reader_name = "Test"
        author = "Author"
        title = "Title"
        self.library.add_reader(reader_name)
        self.library.add_book(author,title)
        self.library.rent_book(reader_name, author, title)
        self.assertEqual([{author:title}],self.library.readers[reader_name])
        self.assertTrue(title not in self.library.books_by_authors[author])

if __name__=="__main__":
    main
from .models import Book
from ariadne import QueryType, make_executable_schema, MutationType
type_defs = """

type Query{
    all_books:[Book]
    get_book(id: Int!): Book
}
type Book{
    id:Int
    book_cover:String
    book_author:String
    publisher:String
    published_year:Int
}
type Mutation{
    add_book(book_cover:String!,book_author:String!,publisher:String!,published_year:Int!): BookResults
    delete_book(id:Int!): BookResults
    update_book(id:Int!,book_cover: String!,book_author:String!,publisher:String!,published_year:Int!): BookResults

}


 type BookResults {
        created: Boolean!
        book: Book
        err: String
}

"""


query = QueryType()
mutation = MutationType()

# Queries resolvers


@query.field('all_books')
def resolve_books(*_):
    return Book.objects.all()


@query.field('get_book')
def resolve_add_book(_, info, id):
    return Book.objects.get(id=id)

# Mutations resolvers


@mutation.field('add_book')
def resolve_add_book(_, info, book_cover, book_author, publisher, published_year):
    book = Book.objects.create(book_cover=book_cover, book_author=book_author,
                               publisher=publisher, published_year=published_year)
    return {'created': True, 'book': book, 'err': None}


@mutation.field('delete_book')
def resolve_delete_book(_, info, id):

    book = Book.objects.get(id=id)
    book.delete()
    return {'created': True, 'book': book, 'err': None}


@mutation.field('update_book')
def resolve_update_book(_, info, id, book_cover, book_author, publisher, published_year):

    book = Book.objects.get(id=id)
    book.book_cover = book_cover
    book.book_author = book_author
    book.publisher = publisher
    book.published_year = published_year
    book.save()
    return {'created': True, 'book': book, 'err': None}


# Initialize executable schema for Graphql

schema = make_executable_schema(type_defs, query, mutation)

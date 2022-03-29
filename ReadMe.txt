This program performs the Crud Operations of a Library Management system using Python Django framework with Ariadne GraphQl.

Postrgres Sql is used and linked to the program in settings.py file under library folder.
The defualt credentials used are postgres for all the parameters.
Once postgres is setup use the following commands

python manage.py makemigrations
python manage.py sqlmigrate
python manage.py migrate
python manage.py runserver

the program will run on default port 8000.

now use the graphql mutations to test the api.

Also navigate to " http://127.0.0.1:8000/admin " to check the data stored or update.

Queries to run are as follows:

query{
  all_books{
    id
    book_cover
    book_author
    publisher
    published_year
  }
}

query{
  get_book(id:8){
    id
    book_cover
    book_author
    publisher
    published_year
  }
}

Mutations to run are as follows for the respective functionality.

mutation {
  add_book(book_cover:"Harry Potter3",book_author:"J.K.Rowling",publisher:"Bloomsbury Publishing",published_year:2007)
  {
    created
    book{
      id
      book_cover
      book_author
      publisher
      published_year
    }
    err
  }
}

mutation {
  update_book(id:9,book_cover:"the kite runner",book_author:"Khaled Hosseini",publisher:"Riverhead Books",published_year:2003)
  {
    created
    book{
      id
      book_cover
    	book_author
    	publisher
    	published_year
    }
    err
  }
}

mutation {
  delete_book(id:8)
  {
    created
    book{
    	book_cover
    	book_author
    	publisher
    	published_year
    }
    err
  }
}


 
--------Thankyou for your time.

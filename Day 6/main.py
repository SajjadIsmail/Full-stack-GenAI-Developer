# Import the Pinecone library
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
import time
from dotenv import load_dotenv
import os

load_dotenv()

pc = Pinecone(os.getenv('PINECONE_API_KEY'))

# # Define a sample dataset where each item has a unique ID and piece of text
# data = [
#     # Set 1
#     {"id": "vec1", "text": "The Dark Knight is a 2008 superhero film directed by Christopher Nolan, starring Christian Bale, Heath Ledger, and Aaron Eckhart."},
#     {"id": "vec2", "text": "Inception is a 2010 science fiction heist thriller directed by Christopher Nolan, starring Leonardo DiCaprio, Joseph Gordon-Levitt, and Tom Hardy."},
#     {"id": "vec3", "text": "The Prestige is a 2006 mystery thriller directed by Christopher Nolan, starring Christian Bale, Hugh Jackman, and Scarlett Johansson."},
#     {"id": "vec4", "text": "Interstellar is a 2014 epic science fiction film directed by Christopher Nolan, starring Matthew McConaughey, Anne Hathaway, and Jessica Chastain."},
#     {"id": "vec5", "text": "The Revenant is a 2015 epic survival drama directed by Alejandro González Iñárritu, starring Leonardo DiCaprio, Tom Hardy, and Domhnall Gleeson."},
#     {"id": "vec6", "text": "Dunkirk is a 2017 war film directed by Christopher Nolan, starring Fionn Whitehead, Tom Hardy, and Kenneth Branagh."},
#     {"id": "vec7", "text": "The Avengers is a 2012 superhero film directed by Joss Whedon, starring Robert Downey Jr., Chris Evans, and Scarlett Johansson."},
#     {"id": "vec8", "text": "Iron Man is a 2008 superhero film directed by Jon Favreau, starring Robert Downey Jr., Gwyneth Paltrow, and Jeff Bridges."},
#     {"id": "vec9", "text": "Thor is a 2011 superhero film directed by Kenneth Branagh, starring Chris Hemsworth, Natalie Portman, and Tom Hiddleston."},
#     {"id": "vec10", "text": "Guardians of the Galaxy is a 2014 superhero film directed by James Gunn, starring Chris Pratt, Zoe Saldana, and Dave Bautista."},
#     {"id": "vec11", "text": "Jurassic Park is a 1993 science fiction adventure film directed by Steven Spielberg, starring Sam Neill, Laura Dern, and Jeff Goldblum."},
#     {"id": "vec12", "text": "Jurassic World is a 2015 science fiction adventure film directed by Colin Trevorrow, starring Chris Pratt, Bryce Dallas Howard, and Vincent D'Onofrio."},
#     {"id": "vec13", "text": "Star Wars: A New Hope is a 1977 epic space opera film directed by George Lucas, starring Mark Hamill, Carrie Fisher, and Harrison Ford."},
#     {"id": "vec14", "text": "Star Wars: The Force Awakens is a 2015 epic space opera film directed by J.J. Abrams, starring Daisy Ridley, Adam Driver, and Harrison Ford."},
#     {"id": "vec15", "text": "The Shawshank Redemption is a 1994 drama film directed by Frank Darabont, starring Tim Robbins, Morgan Freeman, and Bob Gunton."},
#     {"id": "vec16", "text": "The Green Mile is a 1999 fantasy drama film directed by Frank Darabont, starring Tom Hanks, Michael Clarke Duncan, and David Morse."},
#     {"id": "vec17", "text": "The Departed is a 2006 crime thriller film directed by Martin Scorsese, starring Leonardo DiCaprio, Matt Damon, and Jack Nicholson."},
#     {"id": "vec18", "text": "Goodfellas is a 1990 crime film directed by Martin Scorsese, starring Robert De Niro, Ray Liotta, and Joe Pesci."},
#     {"id": "vec19", "text": "Gladiator is a 2000 historical epic film directed by Ridley Scott, starring Russell Crowe, Joaquin Phoenix, and Connie Nielsen."},
#     {"id": "vec20", "text": "Blade Runner 2049 is a 2017 neo-noir science fiction film directed by Denis Villeneuve, starring Ryan Gosling, Harrison Ford, and Ana de Armas."},
#     {"id": "vec21", "text": "The Lord of the Rings: The Fellowship of the Ring is a 2001 fantasy epic directed by Peter Jackson, starring Elijah Wood, Ian McKellen, and Viggo Mortensen."},
#     {"id": "vec22", "text": "The Lord of the Rings: The Two Towers is a 2002 fantasy epic directed by Peter Jackson, starring Elijah Wood, Ian McKellen, and Orlando Bloom."},
#     {"id": "vec23", "text": "The Hobbit: An Unexpected Journey is a 2012 fantasy adventure film directed by Peter Jackson, starring Martin Freeman, Ian McKellen, and Richard Armitage."},
#     {"id": "vec24", "text": "Harry Potter and the Sorcerer's Stone is a 2001 fantasy film directed by Chris Columbus, starring Daniel Radcliffe, Emma Watson, and Rupert Grint."},
#     {"id": "vec25", "text": "Harry Potter and the Deathly Hallows – Part 2 is a 2011 fantasy film directed by David Yates, starring Daniel Radcliffe, Emma Watson, and Ralph Fiennes."},
#     {"id": "vec26", "text": "The Hunger Games is a 2012 science fiction film directed by Gary Ross, starring Jennifer Lawrence, Josh Hutcherson, and Liam Hemsworth."},
#     {"id": "vec27", "text": "Catching Fire is a 2013 science fiction film directed by Francis Lawrence, starring Jennifer Lawrence, Josh Hutcherson, and Woody Harrelson."},
#     {"id": "vec28", "text": "Django Unchained is a 2012 western film directed by Quentin Tarantino, starring Jamie Foxx, Christoph Waltz, and Leonardo DiCaprio."},
#     {"id": "vec29", "text": "The Revenant is a 2015 epic survival drama directed by Alejandro González Iñárritu, starring Leonardo DiCaprio, Tom Hardy, and Domhnall Gleeson."},
#     {"id": "vec30", "text": "Mad Max: Fury Road is a 2015 post-apocalyptic action film directed by George Miller, starring Tom Hardy, Charlize Theron, and Nicholas Hoult."},
#     {"id": "vec31", "text": "Jurassic Park is a 1993 science fiction adventure film directed by Steven Spielberg, starring Sam Neill, Laura Dern, and Jeff Goldblum."},
#     {"id": "vec32", "text": "Jurassic World is a 2015 science fiction adventure film directed by Colin Trevorrow, starring Chris Pratt, Bryce Dallas Howard, and Vincent D'Onofrio."},
#     {"id": "vec33", "text": "Star Wars: A New Hope is a 1977 epic space opera film directed by George Lucas, starring Mark Hamill, Carrie Fisher, and Harrison Ford."},
#     {"id": "vec34", "text": "Star Wars: The Force Awakens is a 2015 epic space opera film directed by J.J. Abrams, starring Daisy Ridley, Adam Driver, and Harrison Ford."},
#     {"id": "vec35", "text": "The Shawshank Redemption is a 1994 drama film directed by Frank Darabont, starring Tim Robbins, Morgan Freeman, and Bob Gunton."},
#     {"id": "vec36", "text": "The Green Mile is a 1999 fantasy drama film directed by Frank Darabont, starring Tom Hanks, Michael Clarke Duncan, and David Morse."},
#     {"id": "vec37", "text": "The Departed is a 2006 crime thriller film directed by Martin Scorsese, starring Leonardo DiCaprio, Matt Damon, and Jack Nicholson."},
#     {"id": "vec38", "text": "Goodfellas is a 1990 crime film directed by Martin Scorsese, starring Robert De Niro, Ray Liotta, and Joe Pesci."},
#     {"id": "vec39", "text": "Gladiator is a 2000 historical epic film directed by Ridley Scott, starring Russell Crowe, Joaquin Phoenix, and Connie Nielsen."},
#     {"id": "vec40", "text": "Blade Runner 2049 is a 2017 neo-noir science fiction film directed by Denis Villeneuve, starring Ryan Gosling, Harrison Ford, and Ana de Armas."},
#     {"id": "vec41", "text": "The Matrix Reloaded is a 2003 science fiction action film directed by Lana Wachowski, Lilly Wachowski, starring Keanu Reeves, Laurence Fishburne, and Carrie-Anne Moss."},
#     {"id": "vec42", "text": "The Matrix Revolutions is a 2003 science fiction action film directed by Lana Wachowski, Lilly Wachowski, starring Keanu Reeves, Laurence Fishburne, and Carrie-Anne Moss."},
#     {"id": "vec43", "text": "The Dark Knight Rises is a 2012 superhero film directed by Christopher Nolan, starring Christian Bale, Tom Hardy, and Anne Hathaway."},
#     {"id": "vec44", "text": "Man of Steel is a 2013 superhero film directed by Zack Snyder, starring Henry Cavill, Amy Adams, and Michael Shannon."},
#     {"id": "vec45", "text": "Batman v Superman: Dawn of Justice is a 2016 superhero film directed by Zack Snyder, starring Ben Affleck, Henry Cavill, and Gal Gadot."},
#     {"id": "vec46", "text": "Wonder Woman is a 2017 superhero film directed by Patty Jenkins, starring Gal Gadot, Chris Pine, and Robin Wright."},
#     {"id": "vec47", "text": "Aquaman is a 2018 superhero film directed by James Wan, starring Jason Momoa, Amber Heard, and Nicole Kidman."},
#     {"id": "vec48", "text": "Justice League is a 2017 superhero film directed by Zack Snyder, starring Ben Affleck, Henry Cavill, and Gal Gadot."},
#     {"id": "vec49", "text": "Shazam! is a 2019 superhero film directed by David F. Sandberg, starring Zachary Levi, Asher Angel, and Mark Strong."},
#     {"id": "vec50", "text": "The Suicide Squad is a 2021 superhero film directed by James Gunn, starring Margot Robbie, Idris Elba, and John Cena."},
#     {"id": "vec51", "text": "Frozen is a 2013 animated musical fantasy film directed by Chris Buck and Jennifer Lee, starring Kristen Bell, Idina Menzel, and Josh Gad."},
#     {"id": "vec52", "text": "Frozen II is a 2019 animated musical fantasy film directed by Chris Buck and Jennifer Lee, starring Kristen Bell, Idina Menzel, and Josh Gad."},
#     {"id": "vec53", "text": "Moana is a 2016 animated musical fantasy film directed by Ron Clements and John Musker, starring Auli'i Cravalho, Dwayne Johnson, and Rachel House."},
#     {"id": "vec54", "text": "Zootopia is a 2016 animated buddy cop comedy film directed by Byron Howard and Rich Moore, starring Ginnifer Goodwin, Jason Bateman, and Idris Elba."},
#     {"id": "vec55", "text": "The Lion King is a 1994 animated musical drama film directed by Roger Allers and Rob Minkoff, starring Matthew Broderick, James Earl Jones, and Jeremy Irons."},
#     {"id": "vec56", "text": "The Incredibles is a 2004 animated superhero film directed by Brad Bird, starring Craig T. Nelson, Holly Hunter, and Samuel L. Jackson."},
#     {"id": "vec57", "text": "Coco is a 2017 animated musical fantasy film directed by Lee Unkrich and Adrian Molina, starring Anthony Gonzalez, Gael García Bernal, and Benjamin Bratt."},
#     {"id": "vec58", "text": "Toy Story is a 1995 animated buddy comedy film directed by John Lasseter, starring Tom Hanks, Tim Allen, and Don Rickles."},
#     {"id": "vec59", "text": "Toy Story 3 is a 2010 animated comedy-drama film directed by Lee Unkrich, starring Tom Hanks, Tim Allen, and Joan Cusack."},
#     {"id": "vec60", "text": "Finding Nemo is a 2003 animated adventure film directed by Andrew Stanton and Lee Unkrich, starring Albert Brooks, Ellen DeGeneres, and Alexander Gould."}
# ]
#
# # Convert the text into numerical vectors that Pinecone can index
# embeddings = pc.inference.embed(
#     model="multilingual-e5-large",
#     inputs=[d['text'] for d in data],
#     parameters={"input_type": "passage", "truncate": "END"}
# )
#
# print(embeddings)
#
# # Create a serverless index
# index_name = "moviecontent"
#
# if index_name not in pc.list_indexes().names():
#     pc.create_index(
#         name=index_name,
#         dimension=1024,
#         metric="cosine",
#         spec=ServerlessSpec(
#             cloud='aws',
#             region='us-east-1'
#         )
#     )
#
# # Wait for the index to be ready
# while not pc.describe_index(index_name).status['ready']:
#     time.sleep(1)

# Target the index where you'll store the vector embeddings
index = pc.Index("example-index")
# Prepare the records for upsert
# Each contains an 'id', the embedding 'values', and the original text as 'metadata'
# records = []
# for d, e in zip(data, embeddings):
#     records.append({
#         "id": d['id'],
#         "values": e['values'],
#         "metadata": {'text': d['text']}
#     })

# Upsert the records into the index
# index.upsert(
#     vectors=records,
#     namespace="example-namespace"
# )

# Define your query
query = "Batman"

# Convert the query into a numerical vector that Pinecone can search with
query_embedding = pc.inference.embed(
    model="multilingual-e5-large",
    inputs=query,
    parameters={
        "input_type": "query"
    }
)

# Search the index for the three most similar vectors
results = index.query(
    namespace='example-namespace',
    vector=query_embedding[0].values,
    top_k=3,
    include_metadata=True,
    include_values=False
)

o = []

for match in results['matches']:
    o.append(match['metadata']['text'])
print(o)

import spacy
# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

def find_matches(query, answer_list):
    query_doc = nlp(query.lower())  # Process the query with spaCy
    relevant_matches = []
    for answer in answer_list:
        answer_doc = nlp(answer.lower())  # Process the answer
        common_words = set(token.text for token in query_doc if token.is_alpha) & \
                       set(token.text for token in answer_doc if token.is_alpha)
        if common_words:  # If there are common words
            return o
    return relevant_matches if relevant_matches else "IRRELEVANT"

final = find_matches(query,o)
print(final)
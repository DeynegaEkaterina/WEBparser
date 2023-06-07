from stanza import Pipeline, download


if __name__ == '__main__':
    nlp = Pipeline(
        lang='ru', 
        processors='tokenize,ner'
        )
    
    download('ru')
    
    with open('data.txt', 'r') as data:
        text = data.read()

        with open("entities.txt", 'a') as entities:
            for sentence in nlp(text).sentences:
                for ent in sentence.ents:
                    entities.write(f"{ent.text} - {ent.type}\n")

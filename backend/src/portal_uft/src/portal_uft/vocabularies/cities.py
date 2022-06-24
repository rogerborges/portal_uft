from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


CITIES = [
    ("palmas", "Palmas"),
    ("araguaina", "Araguaína"),
    ("gurupi", "Gurupi"),
]


@provider(IVocabularyFactory)
def cities_vocabulary(context):
    """Vocabulary of cities in TO."""
    terms = []
    for id_, title in CITIES:
        terms.append(SimpleTerm(id_, id_, title))
    return SimpleVocabulary(terms)

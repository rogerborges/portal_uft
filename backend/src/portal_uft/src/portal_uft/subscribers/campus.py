from kitconcept import api
from portal_uft.content.campus import Campus
from zope.lifecycleevent import ObjectAddedEvent
from zope.lifecycleevent import ObjectModifiedEvent


def _update_tags(obj: Campus):
    """Update tags on Campus object."""
    tags = set(obj.subject)
    city = obj.city
    tags.add(f"Campus: {city}")
    obj.subject = tuple(tags)


def modified(obj: Campus, event: ObjectModifiedEvent):
    """Post modification handler for Campus."""
    _update_tags(obj)


def added(obj: Campus, event: ObjectAddedEvent):
    """Post creation handler for Campus."""
    _update_tags(obj)

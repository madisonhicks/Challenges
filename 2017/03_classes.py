"""
This Python challenge will help you to familiarize yourself with
Python's classes, which will also help you to learn about the general
concept of classes in object-oriented programming across languages.

This module includes both instructions for getting started, an area
for your to write your code, and tests to ensure that your code
functions as intended. The tests are automatically run when
you run the module. You are encouraged to look at the tests in order
to understand how they work and what they are testing.

You may use your own functions in other functions, if you desire.

If you haven't seen the type annotation syntax yet, you can find
a description of it here: https://docs.python.org/3/library/typing.html
"""

# # # Place your imports below this line # # #

from datetime import date, datetime, timedelta
from sys import argv
from typing import Union
from unittest.mock import Mock

import pytest


#
#
#
# # # Coding Challenges Begin # # #
#
#
#


# One: a class is a container
#   At its most basic level, a class can be thought of as a container.
#   It provides a "namespace," which is a fancy of way of saying that
#   variables defined within a class' scope are independent from the
#   variables around them, so if I have a class called Magic with
#   a class variable called "spells", that variable would not interfere
#   with another variable called "spells" defined outside of the class.

#   Classes have a lot of fancy, complicated inner workings, but you
#   can also use a class as a really simple, static container for
#   variables. For example:

#   class Executives:
#       CEO = 'Bob McGuffin'
#       CFO = 'Janice Miller'
#       COO = 'Billiam Willy III'

#   You can then reference those attributes, without doing any class
#   instantiation or anything, like:

#   print(Executives.CEO)

#   Variables defined at the class level, like those above, are called
#   "class attributes," because they are attributes of the class.
#   We'll talk more about class instances later, but you should know
#   that class attributes are also available from instances of a class,
#   as well as from references to the class itself (like above, when
#   we printed the name of the CEO).

#   For this first challenge, fill in the class below so that it has
#   two class attributes. They can be named anything you like, but
#   their values should be strings. Do not add any more than
#   two spells. Your spell names should not start with an underscore.

#   You should know that not all languages provide the ability to use
#   classes as structured containers so easily. These sorts of "static"
#   classes (which are classes that behave identically whether or not
#   they are instantiated), will be explored more later.


class FirstLevelSpells:
    """First-level spell class

    This class defines first-level spells as attributes, and their
    incantations as those attributes' values.
    """
    unlock = 'alohamora'
    levitate = 'wingardium leviosa'

# Two: post-definition assignment
#   Classes are not necessarily static once they are defined. At any
#   time, attributes may be assigned to classes (or their instances,
#   but we will get to that later).

#   For example, I could reference my Executives table from challenge
#   one and add a new employee to it, without changing the definition:

#   Executives.human_resources = 'Goolash McGee'

#   From then on, I can access Goolash's name by referencing
#   Executives.human_resources.

#   It is important to note that changes to the attributes of a class
#   persist as long as the program is running. Whether you change
#   them directly beneath the class, in another file, or in a function,
#   the class will have those changes henceforth. When we get to
#   instances, you will see that these changes also affect any
#   instances created from that class

#   Below, compose the function such that it adds a new spell to
#   FirstLevelSpells. As before, the attribute's value should be
#   a string, and the attribute's name should not start with an
#   underscore.


def add_first_level_spell() -> None:
    """Add a spell to the FirstLevelSpells class"""
    FirstLevelSpells.fire = 'incendio'

# Three: classes as instances
#   One of, if not the primary, uses of classes is found in their
#   ability to be instantiated. You can think of a class definition
#   like a template, and that template defines what a created
#   instance is going to look like. Instances are entirely separate
#   entities from the classes that defined them, just like objects
#   cast from a mold are separate from the mold itself.

#   There are lots of special methods that you can use in writing
#   classes to make the creation of instances easier, more consistent,
#   or more functional. However, none of them are necessary. You can
#   make an instance out of any class, including our FirstLevelSpells
#   container!

#   You instantiate a class by calling it (with parentheses), so, to
#   make an instance of FirstLevelSpells, I can do:

#   first_level_spells = FirstLevelSpells()

#   The variable first_level_spells is now referencing an *instance*
#   of the FirstLevelSpells class.

#   What is special about instances, as opposed to classes themselves?
#   Well, they are completely different entities, as we said above.
#   What that means is that they have their own namespace, so if you
#   define a new attribute on an instance of a class, it does *not*
#   affect the class as a whole, unlike defining the attribute on the
#   class.

#   So, let's look at a quick example to illustrate this.

#   class Demons:
#       chief: 'Diablo'

#   Remember that instances receive a copy of class attributes, so if
#   I make a new instance of Demons, it has a "chief" attribute:

#   print(Demons.chief)  # prints "Diablo"  - accessing a class attribute
#   demons = Demons()
#   print(demons.chief)  # prints "Diablo" - accessing an instance attribute


#   However, let's say I change a class attribute before I instantiate
#   the class. What then? Well, the instance is based on the class, and
#   we changed the class itself, so the new instance will bear whatever
#   changes were made. Let's say Mephistopheles sneakily gets in
#   and updates our class attribute:

#   Demons.chief = 'Mephistopheles'

#   Now, if I access the "chief" attribute on a class reference or in
#   a new instance, I get Mephistopheles:

#   print(Demons.chief)  # prints "Mephistopheles"
#   demons_two = Demons()
#   print(demons_two.chief)  # prints "Mephistopheles"

#   Makes sense so far? Good. But what about my first instance?

#   print(demons.chief)  # prints "Diablo"!

#   Because the first instance was made *before* Mephistopheles
#   made his sneaky change, and because instances are totally
#   separate entities from their classes, the "chief" attribute
#   on our instance did not change. Only the instance created
#   after the change to the class reflected that change, in the
#   same way that updating a mold will only affect newly cast
#   objects, not ones that were cast before updating it.

#   Note that, since instances are totally separate entities, any
#   new attributes defined on the instance are *not* available on
#   the class or any new instances created from it. So if Beelzebub
#   gets a hold of our "demons" instance and updates it:

#   demons.most_horrible = 'beelzebub'

#   That attribute will be available on the instance, but not on
#   the class, on other instances, or on new instances of the class:

#   print(demons.most_horrible)  # prints 'beelzebub'
#   print(demons_two.most_horrible)  # AttributeError!
#   print(Demons.most_horrible)  # AttributeError!
#   new_demons = Demons()
#   print(new_demons.most_horrible)  # AttributeError!

#   This challenge is twofold. First, fill out the SecondLevelSpells
#   class, below, so that it has four spells available to it, with
#   the same guidelines for attribute values as above. Then,
#   fill out the custom_second_level_spells function so that it
#   assigns the value of the passed parameter to a new instance
#   of SecondLevelSpells. The value should be assigned to an
#   attribute called "custom". The function should return the new
#   instance.


class SecondLevelSpells:
    """Second Level Spells"""
    disarm = 'expelliarmus'
    light = 'lumos'
    dark = 'nox'
    dance = 'tarantallegra'


def custom_second_level_spells(new_spell: str) -> SecondLevelSpells:
    """Return an instance of SecondLevelSpells with a custom spell"""
    second_level_instance = SecondLevelSpells()
    second_level_instance.custom = new_spell
    return second_level_instance


# Four: overwriting at the instance level

#   As you saw above in our example with Mephistopheles, you can
#   overwrite class attributes after a class has been defined.
#   You can also overwrite attributes at the instance level. However,
#   unlike with class references, these do not affect the class
#   itself or future instances. Again, back to the concept of a mold,
#   this makes perfect sense. Let's say I have a mold that is used to
#   cast bronze figurines of Achilles. If I make one of these figurines,
#   and then swap out his shield for a handful of flowers, it does not
#   affect any other figurines made by the same mold.

#   Let's define a new Demons class

#   class Demons:
#       most_horrible: 'beelzebub'
#
#   print(Demons.most_horrible)  # prints 'beelzebub'
#   demons = Demons()
#   print(demons.most_horrible)  # prints 'beelzebub'

#   Now, this time we do a better job of keeping our class safe, but
#   Mephistopheles manages to get a hold of one of our instances, and
#   of course, he updates it:

#   demons.most_horrible = 'Mephistopheles'

#   On that instance "demons", "most_horrible" is now Mephistopheles,
#   but on any new instances of the Demons class, and on the class
#   itself, most_horrible will still be "beelzebub":

#   print(demons.most_horrible)  # prints 'Mephistopheles'
#   print(Demons.most_horrible)  # prints 'beelzebub'
#   new_demons = Demons()
#   print(new_demons.most_horrible)  # prints 'beelzebub'

#   For this challenge, write a function that takes some object as
#   its parameter and gives it a new attribute (or overwrites
#   an existing attribute) called "called_by_me_at", whose value
#   is a new datetime instance representing the current time. The
#   updated object should be returned.


def add_called_by_me_at(obj: object) -> object:
    """Add a "called_by_me_at" parameter with the current datetime"""
    obj.called_by_me_at = datetime.now()
    return obj.called_by_me_at

# Five: instance methods and "self"
#   So, we now know all about how class attributes are defined, how
#   they live within the class namespace, and how they are copied
#   to the instance namespace (note this isn't exactly accurate
#   but it is close enough for now). We also know how new attributes
#   can be defined on an instance, that we call these "instance
#   attributes", and that these are only present in the instance's
#   namespace.

#   One neat thing about classes is that you can define instance
#   methods that will only be accessible from instances, and which
#   will have access to the instance's namespace. A "method" is
#   just a function defined inside of a class. By default, all
#   methods defined in a class are instance methods, and they are
#   automatically passed a reference to the instance itself as
#   their first parameter. Traditionally, this parameter is called
#   "self". It could be called anything, but it is recommended to
#   stick with "self" always.

#   Let's say we get tired of these darned demons mucking around
#   with our classes all the time, so we decide to provide them
#   with a method of updating who is chief demon on any instance
#   at any time:

#   class Demons:
#       chief = 'who knows?'
#
#       def update_chief(self, chief_name):
#           self.chief = chief_name

#   With this class, we can just leave our instances laying about,
#   and it doesn't matter which pesky demon gets a hold of them,
#   because updating the chief is now super easy, so they won't
#   be tempted to go trying to change the class itself:

#   demons = Demons()
#   print(demons.chief)  # prints 'who knows?'
#   demons.update_chief('Diablo')
#   print(demons.chief)  # prints 'Diablo'
#   demons.update_chief('Mephisto')  # prints 'Mephisto'

#   Note that, even though chief was originally defined at the
#   class level, because we use "self" to update it, it is only
#   updated on the instance, just as if we had said
#   demons.chief = 'whomever'.

#   print(Demons.chief)  # prints 'who knows?'

#   And therefore, new instances will start off with our originally
#   defined value (at least until a demon gets a hold of it):

#   new_demons = Demons()
#   print(new_demons.chief)  # prints 'who knows?'


#
#
#
# # # Test Code # # #
#
#
#

# You shouldn't need to directly adjust anything in here, but you're
# encouraged to review and understand it.


class TestFirstLevelSpells:

    def test_first_level_form(self):
        """Test that only two spells were defined & that they are strings"""
        _check_form(FirstLevelSpells, 2)


def test_add_first_level_spell():
    """Test the addition of a spell to the FirstLevelSpells class"""
    add_first_level_spell()
    _check_form(FirstLevelSpells, 3)


class TestSecondLevelSpells:

    def test_second_level_form(self):
        """Test that the spells were defined correctly"""
        _check_form(SecondLevelSpells, 4)


@pytest.mark.parametrize('spell', [
    'Aloha mora',
    'Bippity boppity boo',
    'dragonpoop'
])
def test_custom_second_level_spells(spell):
    """Test that the function returns as expected"""
    instance = custom_second_level_spells(spell)

    assert isinstance(instance, SecondLevelSpells)

    _check_form(instance, 5)

    assert hasattr(instance, 'custom')
    assert getattr(instance, 'custom') == spell

    # Verify the class itself has not changed
    _check_form(SecondLevelSpells, 4)


@pytest.mark.parametrize('obj', [
    Mock(),
    # the "type" thing here makes a new class in a tricky way
    type('NewClass', (object, ), {})(),
    type('NewClass', (object, ), {}),
])
def test_add_called_by_me_at(obj):
    """Test the called_by_me_at function"""
    add_called_by_me_at(obj)

    now = datetime.now()
    two_seconds = timedelta(seconds=2)
    assert hasattr(obj, 'called_by_me_at')
    assert now - two_seconds < obj.called_by_me_at < now + two_seconds


def _check_form(obj, expected_spells):
    """Check that the number of spells in an object is as expected"""
    spells = [a for a in dir(obj) if not a.startswith('_')]
    assert len(spells) == expected_spells
    for spell in spells:
        assert isinstance(getattr(obj, spell), str)


if __name__ == '__main__':
    args = ['-x', __file__, '-s', '-v']  # base arguments

    if len(argv) == 2:
        # We got a particular function name to test, so we use pytest's
        # -k argument to find a test called test_<function_name>.
        # Note the use of a Python 3.6+ ONLY f-string
        # (see # https://www.python.org/dev/peps/pep-0498/)

        test_name = (
            f'test_{argv[1]}' if argv[1][0].islower() else f'Test{argv[1]}'
        )
        args.extend(['-k', test_name])

    pytest.main(args)

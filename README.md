# Django Project Structure

This repo is an experiment for django proejct strucutre. Focusing on spliting huge `models.py`, `views.py`, etc. into separate files for better code readability and easier file navigation.

## Django signal test

The pre_save and post_save hook works.

```
(django-model)~/Documents/Repos/djangoProjectStructure(master*)$ python manage.py shell
Python 2.7.10 (default, Jun  1 2015, 00:54:32)
[GCC 4.2.1 Compatible Apple LLVM 6.1.0 (clang-602.0.53)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from todo.models import List, Item
>>> l = List(name='remainder', color='cccccc')
>>> l.save()
List is pre_save first thing
List is pre_save second thing
List is pre_save third thing
List is post_save first thing
List is post_save second thing
List is post_save third thing
>>> i = Item(name='send out claim', description='claim last dental visit', list=l)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/gregwang/.pyenv/versions/django-model/lib/python2.7/site-packages/django/db/models/base.py", line 480, in __init__
    raise TypeError("'%s' is an invalid keyword argument for this function" % list(kwargs)[0])
TypeError: 'name' is an invalid keyword argument for this function
>>> i = Item(title='send out claim', description='claim last dental visit', list=l)
>>> i.save()
Item is pre_save first thing
Item is pre_save second thing
Item is pre_save third thing
Item is post_save first thing
Item is post_save second thing
Item is post_save third thing
>>>
```

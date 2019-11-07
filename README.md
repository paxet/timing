timing
======

Python3.3+ timing module, based on the work of Paul McGuire http://stackoverflow.com/a/1557906
When the program finishes, prints the time expent.

Use
---

You have to import the module and it will print the time on exit
```python
import timing
```

If you want to process some info at intermediate work, yo must call:
```python
start_time = timing.now()
some_method()
finish_time = timing.now()
log('Called some_method()', finish_time - start_time)
```

Installation
------------

```
pip install git+https://github.com/paxet/timing.git
```

License
-------

Licensed under [MIT license](LICENSE)

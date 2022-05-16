# Uploading to PyPi (or test PyPi in this case)

Once you have built your package, the next step is to upload it to PyPi.

However, to avoid clogging up PyPi with everyones testing projects, there is a server called test PyPi that we can use for situations just such as this. 

1. if you haven't already, [create an account on test PyPi](https://test.pypi.org/). **you will need to know your login details later** 
2. In a terminal, type

```python
twine upload --repository testpypi dist/*
# nb: for real PyPi, we just have to do:
twine upload dist/*
```

You should see something like this:

![](__resources/twine_succcess.PNG)

and if you click on the link:

![](__resources/testPyPi.PNG)

You could now create a new environment, pip install your package, and see if it works!!

## uploading future versions

Releases are categorised by their version number (in our case, defined inside ```MyPackage / __init__.py```). PyPi will not let you overwrite a release, which means if you try and reupload without incrementing the version number, it will throw an error.

Therefore, every time you  want to release a new package, you should increment the version number according to [semantic versioning rules](https://en.wikipedia.org/wiki/Software_versioning#Semantic_versioning). 

If you don't want to read this, the short answer is that for almost any change you make that isn't a major release, increment the middle digit, e.g.

```python
__version__ = '0.0.0'
__version__ = '0.1.0'
```




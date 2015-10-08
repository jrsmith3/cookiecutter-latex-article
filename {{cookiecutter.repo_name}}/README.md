{{cookiecutter.project_name}}
====================
This repository contains the files needed to build the paper "{{cookiecutter.project_name}}."

This repo was created from a [`cookiecutter`](https://github.com/audreyr/cookiecutter) [template](https://github.com/jrsmith3/cookiecutter-latex-article).


Build instructions
==================
To build a PDF from the LaTeX source, execute the `scons` command in the root level directory of this project. The PDF will be placed in the `build` subdirectory. The `build` subdirectory is ignored by git (cf. `.gitignore`).

```
$ scons
```

I recommend installing SCons via [The Continuum Anaconda distribution](https://www.continuum.io/why-anaconda).

Dependencies
------------
* [LaTeX](http://www.latex-project.org)
* [SCons](http://scons.org)

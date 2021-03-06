# Data Structure Visualiser

[![License](https://img.shields.io/badge/license-MIT-brightgreen)][license_link]

[license_link]:https://github.com/IshMehta/DSViz/blob/main/LICENSE
[![PyPI downloads](https://img.shields.io/pypi/dm/DataStructureVisualiser?color=important)](https://pypistats.org/packages/datastructurevisualiser)


DSViz is a simple and intuitive Python interface to multiple packages in order to help visualise different data structres while coding them. This package is developed mainly for students or developers who are in the process of learning data structures. 

 This packages acts as an interface to Tkinter a Python UI library and [GraphViz](https://www.graphviz.org/) which facillitates rendering of graphs described in the [DOT](https://www.graphviz.org/doc/info/lang.html) language.

This package can be used to visualise any implementations of the following:

* Array Lists
* Linked Lists
    * Singly Linked Lists
    * Doubly Linked Lists
    * Circular Linked Lists
* Trees
    * Binary Trees
    * AVL
    * 2-4 Trees
* Graphs
    * Directed Graphs
    * Undirected Graphs
These are just a few examples data structures that can be visualised using DSViz.

# Links

- GitHub: https://github.com/IshMehta/DSViz
- PyPI: https://pypi.org/project/DataStructureVisualiser/
- Documentation: https://ishmehta.github.io/DSViz/


# Install


This library requires the GraphViz to be installed.




## Mac 



We recommend using Homebrew to install GraphViz.

Open terminal and run the following command (assuming you have Homebrew installed)

```zsh
brew install graphviz
```


## Windows


Historically, installing Graphviz and PyGraphviz on Windows has been challenging.
Fortunately, the Graphviz developers are working to fix this and
their recent releases have much improved the situation.

For this reason, PyGraphviz 1.7 only supports Graphviz 2.46.0 or higher on Windows.
We recommend either manually installing the official binary release of Graphviz

You may also need to install Visual C/C++, e.g. from here:
https://visualstudio.microsoft.com/visual-cpp-build-tools/

Assuming you have Python and Visual C/C++ installed,
we believe the following should work on Windows 10 (64 bit) using PowerShell.

Manual download: 


Download and install 2.46.0 for Windows 10 (64-bit):
   [stable_windows_10_cmake_Release_x64_graphviz-install-2.46.0-win64.exe](https://gitlab.com/graphviz/graphviz/-/package_files/6164164/download)

## Linux


We recommend installing Graphviz using your Linux system's package manager.
Below are examples for some popular distributions.

Ubuntu and Debian

```zsh
sudo apt-get install graphviz graphviz-dev
```

Fedora and Red Hat


You may need to replace ``dnf`` with ``yum`` in the example below.
```zsh
sudo dnf install graphviz graphviz-devel
```
## Finally
After installing GraphViz according to your OS, you can install our > package and the other dependencies using pip

```bash
 $ pip install DataStructureVisualiser
```

*Credits to [pygraphviz](https://github.com/pygraphviz/pygraphviz/blob/main/INSTALL.txt) for specific instructions on downloading GraphViz.*


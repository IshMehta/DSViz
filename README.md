# DataStructureViz

DSViz is a simple and intuitive Python interface to multiple packages in order to help visualise different data structres while codng them. This package is developed mainly for students or developers who are in the process of learning data structures. 

 This packages acts as an interface to Tkinter a Python UI library and [GraphViz](https://www.graphviz.org/) which facillitates rendering of graphs described in the [DOT](https://www.graphviz.org/doc/info/lang.html) language.

This package can be used to visualise any implementations of the following:

* Array Lists
* Linked Lists
    * Singly Linked Lists
    * Doubly Linked Lists
    * Circular Linked Lists
* Trees
* Graphs
    * Directed Graphs
    * Undirected Graphs

# Install


This library requires the GraphViz to be installed.




## Mac 



We recommend using Homebrew to install GraphViz.

Open terminal and run the following command (assuming you have Homebrew installed)

```
brew install graphviz
```

> Important Note:
> 

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
~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ sudo apt-get install graphviz graphviz-dev


Fedora and Red Hat
~~~~~~~~~~~~~~~~~~

You may need to replace ``dnf`` with ``yum`` in the example below.

.. code-block:: console

    $ sudo dnf install graphviz graphviz-devel


> After installing GraphViz according to your OS, you can install our > package and the other dependencies using pip
> 
> ```
> TODO: pip install our package name
> ```

*Credits to [pygraphviz](https://github.com/pygraphviz/pygraphviz/blob/main/INSTALL.txt) for specidifc instructions on downloading GraphViz.*


# License

This package is distributed under the [MIT License](https://github.com/IshMehta/DataStructureViz/blob/main/LICENSE)


# cyber_components

`cyber_components` is a library meant to help you represent your cyber environments with Python objects and a database.

`cyber_components` is currently optimized for Windows environments but there are plans to include other environments.

Examples of components that may be represented with `cyber_components`:
* Machines (PCs, servers, anything in between)
* Network interfaces
* Windows sessions
* Processes
* File system objects (drives, folders, files)
* Much more

All components are declared in Pythonic classes and reference each other. 

For example, since processes run on machines `Machine` objects will have a list of `Process` objects linked.

All components are automatically stored and linked to each other in a SQLite database for further manipulation and inspection. 
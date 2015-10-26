#Grindstone

![Grindstone Logo](gs.png)

*Helping you get shit done since 2015.*

##Usage

```
$ pip install --user GrindStone
$ grindstone init .
Grindstone Created at /path/to/current/working/dir
$ grindstone add a_task which I really need to get done
$ grindstone add another_task that might be less important
$ grindstone
[a_task] which I really need to get done
$ grindstone list
[a_task] which I really need to get done
[another_task] that might be less important
$ grindstone prioritize another_task
$ grindstone list
[another_task] that might be less important
[a_task] which I really need to get done
$ grindstone remove a_task
$ grindstone list
[another_task] that might be less important
$ grindstone pop
$ grindstone list
$ grindstone help
GrindStone: Keeping you on task since 2015.
Usage:
   grindstone [top]
       Prints the top task on the grindstone
   grindstone init <path>
       Initializes a .grindstone in the <path> directory
   grindstone add <task_name> <description of task>
       Adds a task to the closest .grindstone
   grindstone remove <task_name>
       Removes the specified task with <task_name>
   grindstone prioritize <task_name>
       Move a given task to the top of the grindstone
   grindstone pop
       Removes the top task on the grindstone
   grindstone list
       Lists all tasks on the grindstone
   grindstone help
       Prints this help message
```

And that's pretty much it.

##License

GrindStone is licensed under the MIT license

Copyright © 2015 Elijah Caine M. Voigt

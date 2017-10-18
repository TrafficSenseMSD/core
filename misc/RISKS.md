# Risks
Identified below are a series of risks and countermeassures to derisk this project and ensure that we are able to actually
move forward with real progress through the MSD I and MSD II phases.  After looking at the scope of the project
and the position of groups in a similar position to the team, it is clear that without starting to explore the details
of the system and tools, we will fail to deliver as we start development.  Nodding and saying we will add something to our scope
without real understanding of the scale of the task is dangerous.  

We can be confident that we are capable people however if we can ramp up our skills on as much as possible, we will encounter
roadblocks with the tools, files, and systems before they are on the critical path the development.

Table of Contents
=================

   * [Risks](#risks)
   * [Table of Contents](#table-of-contents)
      * [Familiarity with git, <code>github</code> and use of source control](#familiarity-with-git-github-and-use-of-source-control)
      * [Repository structuring and project framework](#repository-structuring-and-project-framework)
      * [Configuration of Python environment](#configuration-of-python-environment)
      * [Ensure the entire team is comfortable doing development (not scripts) in Python 3.6](#ensure-the-entire-team-is-comfortable-doing-development-not-scripts-in-python-36)
      * [Core Compentency: Python   XML](#core-compentency-python--xml)
      * [Core Compentency: Python   TraCI   SUMO](#core-compentency-python--traci--sumo)
      * [Core Competency: Python   Pandas   NumPy](#core-competency-python--pandas--numpy)
      * [Face the fallacy of "We will just use machine learning (ML)" or similar algorithmic implementation](#face-the-fallacy-of-we-will-just-use-machine-learning-ml-or-similar-algorithmic-implementation)
      * [Is cross platform native install or virtualized environment (Vagrant/Docker/VirtualBox) a better option?](#is-cross-platform-native-install-or-virtualized-environment-vagrantdockervirtualbox-a-better-option)
      * [The source code must be testable and "build" after <em>most</em> commits to master](#the-source-code-must-be-testable-and-build-after-most-commits-to-master)
   * [Additional Information](#additional-information)
      * [Eilif Mikkelsen](#eilif-mikkelsen)
      
      
## Familiarity with `git`, `github` and use of source control
### Purpose
Source control tools allow multi-member software teams to develop in a parallel, distributed way.  Git 
is a technology adopted world wide as an excellent source control system. GitHub is a hosted Git service
used by thousands of companies and millions of individuals.

###  Mitigation Measures
Have every team member...
* Fork this repository
* Clone their fork to their local development machine (including how get git working for them locally)
* Add their name and favorite color to the end of this document under the section `Addition Info`
* Create a pull request merging their fork with the master branch of this repository.
* Add at least one other team member as the reviewer
* If the reviewer, review and merge.



## Repository structuring and project framework
### Purpose
It's not required that everyone be an expert on how to setup and structure Python software projects, that said
a structure needs to be developed, accepted, and enforced for project sanity.  Project structure changes may be required
as the project progresses.  These changes should be considered carefully and any changes need to be reflected in the build system. 

### Mitigation Measures
* Following Python best practices, anticipate the structure, set it up, and document the structure.
* Confirm that the entire team understand how to develop within the project structure.



## Configuration of Python environment
Virtualenv, anaconda, pipenv, etc.  Decide and implement. 
Everyone should be confident setting up the development tool chain on their local and test environments. 



## Ensure the entire team is comfortable doing development (not scripts) in Python 3.6
### Mitigation Measures
Have every team member...
* Fork and clone this repository
* In `misc/training_resource` create a folder called `<firstname_lastname`
* Complete a moderately comprehensive Python core competency test `TBD` in the created folder
* Push this code to their fork and create a PR to `master`
* Before merging, have at least one other team member download the other member's fork and run the code.
* If it runs and performs as expected, merge it to `core/master`

### Acceptance Criteria
* Write two modules with classes and functions that do something and can be imported by other python code
* One module must use functions or classes declared in the other module
* A script or commandline tool that uses the aforementioned modules to do something


## Core Compentency: Python + XML
### Purpose and Acceptance Criteria
Ramp all team members on 
- Python + XML
- Parsing SUMO XML parsing
- Generating SUMO XML files

### Mitigation Measures
Online course completion, group developed tests, or similar.




## Core Compentency: Python + TraCI + SUMO
### Purpose and Acceptance Criteria
`TBD`

### Mitigation Measures
Online course completion, group developed tests, or similar.



## Core Competency: Python + Pandas + NumPy
### Purpose and Acceptance Criteria
`TBD`

### Mitigation Measures
Online course completion, group developed tests, or similar.




## Face the fallacy of "We will just use machine learning (ML)" or similar algorithmic implementation
Saying we will use ML implies ML is a magic black box with data as an input and answers as an output.  In practice implementing ML
is a long painful process that in itself could take the entire semester.  

When talking with Dr. Katie she noted the cavalier statements  like "Yeah, we will just add a genetic algorithm to do xyz" pointing out that even for experienced developers, this alone is a 
serious undertaking. 


## Is cross platform native install or virtualized environment (Vagrant/Docker/VirtualBox) a better option?
Lots to talk about here, TBD.  Virtualized Enviroment keeps the development simple since we are only writing one set of tools.




## The source code must be testable and "build" after _most_ commits to `master`
### Mitigation Measures
* Given `sumo` installed at linked at environment variable `SUMO_HOME` (SUMO default on all systems)
* Define a linux based test build that, including:
    * Cloning this repository
    * Install the source code including Python source code and all other additional modules
    * Build documentation
    * 

#### Purpose a Linux automated build system?
- It's free to get a Linux build system using TravisCI or similar
- Scientific computer is more often than not run on Linux to maximize resources



# Additional Information
##  Eilif Mikkelsen
My name is Eilif Mikkelsen and I like blue

# Risks
Identified below are a series of risks and countermeassures to derisk this project and ensure that we are able to actually
move forward with real progress through the MSD I and MSD II phases.  After looking at the scope of the project
and the position of groups in a similar position to the team, it is clear that without starting to explore the details
of the system and tools, we will fail to deliver as we start development.  Nodding and saying we will add something to our scope
without real understanding of the scale of the task is dangerous.  

Table of Contents
=================

   * [Risks](#risks)
      * [Familiarity with git, <code>github</code> and use of source control](#familiarity-with-git-github-and-use-of-source-control)
      * [Repository structuring and project framework](#repository-structuring-and-project-framework)
      * [Ensure the entire team is comfortable doing development (not scripts) in Python 3.6](#ensure-the-entire-team-is-comfortable-doing-development-not-scripts-in-python-36)
      * [Face the fallacy of "We will just use machine learning (ML)"](#face-the-fallacy-of-we-will-just-use-machine-learning-ml)
      * [The source code must be testable and "build" after <em>most</em> commits to master](#the-source-code-must-be-testable-and-build-after-most-commits-to-master)

   * [Additional Information](#additional-information)
      * [Eilif Mikkelsen](#eilif-mikkelsen)


## Familiarity with `git`, `github` and use of source control
### Why
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
### Why
It's not required that everyone be an expert on how to setup and structure Python software projects, that said
a structure needs to be developed, accepted, and enforced for project sanity.  Project structure changes may be required
as the project progresses.  These changes should be considered carefully and any changes need to be reflected in the build system. 

### Mitigation Measures
* Following Python best practices, anticipate the structure, set it up, and document the structure.
* Confirm that the entire team understand how to develop within the project structure.



## Ensure the entire team is comfortable doing development (not scripts) in Python 3.6
### Mitigation Measures
Have every team member...
* Fork and clone this repository
* In `misc/training_resource` create a folder called `<firstname_lastname`
* Complete a moderately comprehensive Python core competency test `TBD` in the created folder
* Push this code to their fork and create a PR to `master`
* Before merging, have at least one other team member download the other member's fork and run the code.
* If it runs and performs as expected, merge it to `core/master`


## Face the fallacy of "We will just use machine learning (ML)"
Saying we will use ML implies ML is a magic black box with data as an input and answers as an output.  In practice implementing ML
is a long painful process that in itself could take the entire semester.  

## The source code must be testable and "build" after _most_ commits to `master`
### Mitigation Measures
* Given `sumo` installed at linked at environment variable `SUMO_HOME` (SUMO default on all systems)
* Define a linux based test build that, including:
    * Cloning this repository
    * Install the source code including Python source code and all other additional modules
    * Build documentation
    * 

#### Why a Linux automated build system?
- It's free to get a Linux build system using TravisCI or similar
- Scientific computer is more often than not run on Linux to maximize resources


# Additional Information
##  Eilif Mikkelsen
My name is Eilif Mikkelsen and I like blue

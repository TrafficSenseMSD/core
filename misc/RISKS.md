# Risks

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



## Ensure the entire team is comfortable doing development (not scripts) in Python 3.6
### Mitigation Measures
Have every team member...
* Fork and clone this repository
* 

## Face the fallacy of "We will just use machine learning (ML)"


# Additional Information
##  Eilif Mikkelsen
My name is Eilif Mikkelsen and I like blue

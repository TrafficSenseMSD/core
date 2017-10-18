# Risks

## Familiarity with `git`, `github` and use of source control
###  Mitigation Measures
Have every team member...
* Fork this repository
* Clone their fork to their local development machine (including how get git working for them locally)
* Add their name and favorite color to the end of this document under the section `Addition Info`
* Create a pull request merging their fork with the master branch of this repository.
* Add at least one other team member as the reviewer
* If the reviewer, review and merge.
            
- Familiarity with Python package development
            
## The source code must be testable after _most_ commits to `master`
### Mitigation Measures
* Given `sumo` installed at linked at environment variable `SUMO_HOME` (SUMO default on all systems)
* Define a linux based test build that, including:
    * Cloning this repository
    * Install the source code including Python source code and all other additional modules
    * Build documentation
    * 

#### Why a Linux automated build system?
- It's free to get a Linux build system using TravisCI or similar

# Additional Information
##  Eilif Mikkelsen
My name is Eilif Mikkelsen and I like blue

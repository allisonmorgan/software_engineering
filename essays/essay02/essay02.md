# Open Source Development & Licenses: Overview

When developing [open source software](https://en.wikipedia.org/wiki/Open-source_software), there are many open source licenses which can be used by authors to allow others to modify and develop upon a codebase, while still retaining some intellectual property.

### Development of Open Source Software (OSS)

In 1998, the term ["open source"](https://en.wikipedia.org/wiki/Open-source_model#Open_source_as_a_term) was coined by members of the software community to describe public collaboration on top of free and commercially available software ([official definition](https://opensource.org/osd-annotated)). Though there existed other open source projects at the time (e.g. Linux), the release of the source code behind the browser [Netscape](https://www.engadget.com/2018/02/03/20-years-of-open-source-software/) inspired the introduction of the term. Unlike other projects at the time, [Netscape](https://en.wikipedia.org/wiki/Netscape#Open_sourcing) was released under a license which would still allow the company to publish proprietary work containing any publicly released source code. Shortly after, open source evangelist, Eric Raymond, defined a model for the development of "open source" projects. 

#### Brief Tangent - A Model of OSS

![cathedral_bazaar](https://user-images.githubusercontent.com/6633242/35839782-a35b3924-0aaf-11e8-86b4-cc55f34fd575.jpg)
_From the blog of [Gulia Forsythe](http://gforsythe.ca/sakai-oae-a-bazaar-in-the-cathedral/)_

In his model, Raymond contrasts two different open source software models. From the Wikipedia article for his book ["The Cathedral and the Bazaar"](https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar):

> - **The Cathedral model,** in which source code is available with each software release, but code developed between releases is restricted to an exclusive group of software developers. GNU Emacs and GCC were presented as examples.
> - **The Bazaar model,** in which the code is developed over the Internet in view of the public. Raymond credits Linus Torvalds, leader of the Linux kernel project, as the inventor of this process. Raymond also provides anecdotal accounts of his own implementation of this model for the Fetchmail project. 

Raymond argues that the Cathedral model is more typical of traditional software, centralized with well-defined roles among developers. He argues that Bazaar is the faster model of development. The latter has inspired the development model of [Wikipedia](https://www.newyorker.com/magazine/2006/07/31/know-it-all). (More features of this Bazaar model can be found [here](https://en.wikipedia.org/wiki/Open-source_software#Development_model).)

### Why Choose an Open Source License?

By specifying an open source license, you allow developers to use, modify or share your code, while still retaining certain copyright permissions. By providing no license, you retain the [exclusive copyright](https://choosealicense.com/no-permission/) of the work, and disallow others from contributing. 

### How to Choose a License

[Over 80 licenses](https://opensource.org/licenses/alphabetical) have been approved by the Open Source Initiative. Generally all of these licenses allow for the use, reproduction, and modification of software, with or (in some cases) without reference to the original source code. There are many options for open source licenses. Some of the comparison tools that I've provided below can be helpful in choosing the appropriate license for your project.

Here, I will highlight a few of the popular license options: (1) MIT License, (2) Apache License 2.0 and (3) GNU General Public License v3.0]. From [choosealicense.org](https://choosealicense.com), I've reproduced the short descriptions of each:

#### [MIT License](https://choosealicense.com/licenses/mit/)

> A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.

#### [Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)

> A permissive license whose main conditions require preservation of copyright and license notices. Contributors provide an express grant of patent rights. Licensed works, modifications, and larger works may be distributed under different terms and without source code.

#### [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)

> Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.


I'd encourage you to puruse [choosealicense.org](https://choosealicense.com) to find the appropriate license for your project.

### Adding an Open Source License to your Github Project

Once you have chosen an open source license, it's very easy to add a license to your Github repository. Check out [this](https://help.github.com/articles/adding-a-license-to-a-repository/) tutorial.

### References

- Comparison Tools: 
	- [Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses)
	- [choosealicense.com](https://choosealicense.com) 
	- [Open Source Iniative](https://opensource.org/licenses)

I say "seemingly straightforward" because the MIT License is one of the most popular licenses used by open source software. The MIT License, Apache License, and BSD license are the main permissive licenses, a term that contrasts with reciprocal licenses like the GPL, which require source code to be made available when software is redistributed.

Given its popularity, you'd think the license's inception would be well-documented. I found various clues that added up to a date in the late 1980s but nothing definitive. However, Keith Packard and Jim Gettys jumped on the thread to offer first-hand accounts of the license's creation. In addition to providing early examples of the license, their help also gave me the context to better understand how the license evolved over time.

The date? The best single answer is probably 1987. But the complete story is more complicated and even a little mysterious.

This story begins with Project Athena at the Massachusetts Institute of Technology (MIT). "Project Athena was a joint project of MIT, Digital Equipment Corporation (DEC), and IBM to produce a campus-wide distributed computing environment for educational use," says Wikipedia. Launched in 1983, it gave rise to important software that would end up being used broadly, including the X Window System and Kerberos.

The X Window System specifically provides the basic framework for "drawing and moving windows on the display device and interacting with a mouse and keyboard," says Wikipedia. Version 1 of X came out in June 1984. The software reached version 11 in 1987 (hence "X11," as all subsequent releases have been called). Minor releases use nomenclature such as X10R4 or X11R7.7.

X was originally under a proprietary license but, according to Packard, what we would now call an open source license was added to X version 6 in 1985. (I say "now call" because the term "open source" wasn't coined until Christine Peterson did so in 1998.) According to Gettys, "Distributing X under license became enough of a pain that I argued we should just give it away." However, it turned out that just placing it into the public domain wasn't an option. "IBM would not touch public domain code (anything without a specific license). We went to the MIT lawyers to craft text to explicitly make it available for any purpose. I think Jerry Saltzer probably did the text with them. I remember approving of the result," Gettys added.

There's some ambiguity about when exactly the early license language stabilized; as Gettys writes, "we weren't very consistent on wording." However, the license that Packard indicates was added to X Version 6 in 1985 appears to have persisted through X Version 11, Release 5. A later version of the license language seems to have been introduced in X Version 11, Release 6 in 1994.

Hence, there's a good argument to be made that the MIT License, also called the X Consortium or X11 License at the time, crystallized with X11 in 1987, and that's the best date to use. You could argue it was created in 1985 with possible adjustments over the next couple of years. Licenses often evolved incrementally in those days. For example, Gettys observed that although the GPLv1 license was officially released in 1989, Richard Stallman's Emacs was previously distributed under a license similar to the GPL.

But the story doesn't end there. If you look at the license used for X11 and the approved MIT License at the Open Source Initiative (OSI), they're not the same. Similar in spirit, but significantly different in the words used.

The "modern" MIT License is the same as the license used for the Expat XML parser library beginning in about 1998. The MIT License using this text was part of the first group of licenses approved by the OSI in 1999. What's peculiar is that, although the OSI described it as "The MIT license (sometimes called called [sic] the 'X Consortium license')," it is not in fact the same as the X Consortium License.

How and why this shift happened—and even if it happened by accident—is unknown. But it's clear that by 1999, the approved version of the MIT License, as documented by the OSI, used language different from the X Consortium License. This is the reason why some, including the Free Software Foundation, prefer to avoid the "MIT License" terminology entirely, given that it can refer to several related, but different, licenses.

(The MIT License is not unique in such inconsistency. For example, there is a 3-Clause BSD License and an older 4-Clause one, even though there is no explicit versioning.)

So, there you have it. Pick your date. Precursors from 1985. The X Consortium or X11 License variant from 1987. Or the Expat License from 1998 or 1999.

Thanks to the participants in this Twitter thread for making this article possible.

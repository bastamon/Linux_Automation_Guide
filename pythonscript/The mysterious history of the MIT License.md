# 麻省理工学院许可证的神秘历史

## Given its popularity, you'd think the MIT License's inception would be well-documented, but it's actually quite a mystery.

## 考虑到许可证的受欢迎程度，大家可能会认为创立许可证的起源会有详细记载，但实际上却是个谜。

![pics](https://opensource.com/sites/default/files/styles/image-full-size/public/lead-images/freesoftwareway_law3.png?itok=wyze_0fV)

***图像取自: opensource.com***

Recently, [David Humphrey posed](https://twitter.com/humphd/status/1112747178685026304) a seemingly straightforward question on Twitter.

    When was the MIT License created? I can't find any source that gives a year.
    — David Humphrey (@humphd) April 1, 2019

最近, David Humphrey在Twitter上提出了一个看似直截了当的问题。

    MIT许可证是何时创立的? 我花了一整年也没找到任何论据。
    — David Humphrey (@humphd) April 1, 2019

I say "seemingly straightforward" because the MIT License is one of the most popular licenses used by open source software. The MIT License, Apache License, and BSD license are the main permissive licenses, a term that contrasts with reciprocal licenses like the GPL, which require source code to be made available when software is redistributed.

说“看似直截了当”，是因为麻省理工学院许可证是使用开源软件中最流行的许可证之一。MIT许可证、Apache许可证和BSD许可证是目前主要的授权许可证，这一术语与GPL等互惠许可证形成鲜明对比，因为GPL要求在重新分发软件时提供源代码。

Given its popularity, you'd think the license's inception would be well-documented. I found various clues that added up to a date in the late 1980s but nothing definitive. However, [Keith Packard](https://twitter.com/keith_x11) and [Jim Gettys](https://twitter.com/JimGettys) jumped on the [thread](https://web.archive.org/web/20190402160714/https:/gist.github.com/humphd/2832b267ee1dfc0329a58a638bc20d4c) to offer first-hand accounts of the license's creation. In addition to providing early examples of the license, their help also gave me the context to better understand how the license evolved over time.

考虑到许可证的受欢迎程度，大家可能会认为创立许可证的起源会有详细记载。我虽然找到了各种线索，这些线索加起来最早可追溯到上世纪80年代末，但都算不上是理想的证明材料。好在 [Keith Packard](https://twitter.com/keith_x11)和 [Jim Gettys](https://twitter.com/JimGettys)很快加入了[讨论](https://web.archive.org/web/20190402160714/https:/gist.github.com/humphd/2832b267ee1dfc0329a58a638bc20d4c)，并向我提供了许可创建时的第一手资料。除了提供许可证的早期案例外，他们还帮助我理解许可证是如何随着时间演变的。

The date? The best single answer is probably 1987. But the complete story is more complicated and even a little mysterious.

执意想知道许可证创立的日期？那么它创立的日子可能是在1987年。 但完整的故事其实要复杂得多，甚至有些神秘。

This story begins with Project Athena at the Massachusetts Institute of Technology (MIT). "Project Athena was a joint project of MIT, Digital Equipment Corporation (DEC), and IBM to produce a campus-wide distributed computing environment for educational use," says [Wikipedia](https://en.wikipedia.org/wiki/Project_Athena). Launched in 1983, it gave rise to important software that would end up being used broadly, including the X Window System and Kerberos.

故事要从麻省理工学院的雅典娜计划开始。据 [Wikipedia](https://en.wikipedia.org/wiki/Project_Athena)引述:“雅典娜项目是麻省理工学院、数字设备公司(DEC)和IBM公司三家单位的合作项目，目的是为教育领域建设一个适用于校级范围的分布式计算环境。”自雅典娜项目1983年推出后，产生了一些重要的软件，最终得到了广泛的应用，其中就包括X视窗系统和Kerberos。

The X Window System specifically provides the basic framework for "drawing and moving windows on the display device and interacting with a mouse and keyboard," says [Wikipedia](https://en.wikipedia.org/wiki/X_Window_System). Version 1 of X came out in June 1984. The software reached version 11 in 1987 (hence "X11," as all subsequent releases have been called). Minor releases use nomenclature such as X10R4 or X11R7.7.

引用[Wikipedia原文](https://en.wikipedia.org/wiki/X_Window_System)：X视窗系统是专门为“在显示设备上进行绘制、移动窗口以及键鼠交互”所提供的基本框架。X视窗系统的第1版虽然于1984年6月问世，但仅经过3年它就已被迭代到第11版(因此称为“X11”，也是后续所有版本的名称)。次要版本则使用诸如X10R4或X11R7.7之类的命名法。

X was originally under a proprietary license but, according to Packard, what we would now call an open source license [was added](https://keithp.com/data/mit-copyright.h) to X version 6 in 1985. (I say "now call" because the term "open source" wasn't coined until [Christine Peterson](https://opensource.com/article/18/2/coining-term-open-source-software) did so in 1998.) According to Gettys, "Distributing X under license became enough of a pain that I argued we should just give it away." However, it turned out that just placing it into the public domain wasn't an option. "IBM would not touch public domain code (anything without a specific license). We went to the MIT lawyers to craft text to explicitly make it available for any purpose. I think Jerry Saltzer probably did the text with them. I remember approving of the result," Gettys added.

X视窗系统最初使用的是专有的许可证，但根据Packard的说法，我们现今所指的开放源码许可证是直到1985年才[添加](https://keithp.com/data/mit-copyright.h)到X视窗第6版中的。(“当今所指”是因为“开源”这一专有术语直到1998年才被 [Christine Peterson所提出](https://opensource.com/article/18/2/coining-term-open-source-software)。)据Gettys回忆道：“在许可证制约下发布X视窗系统真的有够痛苦的，当时我认为我们应该直接把它白送出去。” 但事实证明，仅将其传到公开平台并没公司买账。Gettys解释道：“IBM公司压根就不想理会这些公开的(任何没有特定许可的)代码。结果我们只好去请麻省理工学院的律师帮忙起草了一份法律文件，明确指出可将X视窗系统用于任何目的。我记得当时Jerry Saltzer也是起草法律文件的一员，另外我还记得当时我赞成了这一结果。”

There's some ambiguity about when exactly the early license language stabilized; as Gettys writes, "we weren't very consistent on wording." However, the license that Packard indicates was added to X Version 6 in 1985 appears to have persisted through X Version 11, Release 5. A later version of the license language seems to have been introduced in [X Version 11, Release 6](https://www.x.org/releases/X11R6/) in 1994.

早期许可证的标准语言是何时启用的依旧难以琢磨。正如Gettys评论的：“我们当时在措辞上十分不一致。” 但是，Packard指出的于1985年添加到第6版X视窗系统中的许可证似乎一直延用到第11.5版X视窗系统。稍晚一点的许可证标准语言则似乎已在1994年[第11.6版的X视窗系统](https://www.x.org/releases/X11R6/)的中引入。

Hence, there's a good argument to be made that the MIT License, also called the X Consortium or X11 License at the time, crystallized with X11 in 1987, and that's the best date to use. You could argue it was created in 1985 with possible adjustments over the next couple of years. Licenses often evolved incrementally in those days. For example, Gettys observed that although the GPLv1 license was officially released in 1989, Richard Stallman's Emacs was previously distributed under a license similar to the GPL.

因此，有论点很好地指出：麻省理工学院的许可证，当时也被称为X财团或X11许可证，是在1987年与X11一同正式发布的，所以该发布日理应成为许可证腾空出世的正确日期。但有人可能会反驳说：“许可证应该是1985年创建的，后来几年只不过进行了修订。”在当时的条件下，许可证的确需要经常修订。Gettys也提到一个例子，虽然GPLv1许可证在1989年正式发布，但Richard Stallman的IDE工具“Emacs”之前就已经采用类似于GPL的许可证发布了。

But the story doesn't end there. If you look at the license used for X11 and the [approved MIT License](https://opensource.org/licenses/MIT) at the Open Source Initiative (OSI), they're not the same. Similar in spirit, but significantly different in the words used.

故事并没有就此结束。如果您仔细查看X11的使用许可证和开放源码计划(OSI)中已[批准的MIT许可证]((https://opensource.org/licenses/MIT))，二者内容是不一样的。虽然在精神上相似，但在措辞上就有明显不同。

The "modern" MIT License is the same as the license used for the Expat XML parser library beginning in about 1998. The MIT License using this text was part of the first group of licenses approved by the OSI in 1999. What's peculiar is that, although the OSI described it as "The MIT license (sometimes called called [sic] the 'X Consortium license')," it is not in fact the same as the X Consortium License.

“现代”MIT许可证与1998年用在Expat XML解析器库的许可证相同。采用该本文的MIT许可证是1999年由OSI计划第一批批准的一部分。怪的是，尽管OSI计划将其描述为“MIT许可证(有时也称为【原文】‘X财团许可证’)”，但它实际上与X财团许可证并不相同。

How and why this shift happened—and even if it happened by accident—is unknown. But it's clear that by 1999, the approved version of the MIT License, as documented by the OSI, used language different from the X Consortium License. This is the reason why some, including the Free Software Foundation, prefer to avoid the "MIT License" terminology entirely, given that it can refer to several related, but different, licenses.

这种转变是如何发生的，以及为什么会发生，甚至是不是偶然发生的，目前都还是未知。但显然如OSI计划所记录的那样，1999年之前的MIT许可证的批准版本使用的是与X财团许可证不同的语言。这也是为什么包括自由软件基金会在内的一些机构宁愿完全规避使用“MIT许可证”术语的原因，因为“MIT许可证”可以引用几个相关却不同的许可证。

(The MIT License is not unique in such inconsistency. For example, there is a 3-Clause BSD License and an older 4-Clause one, even though there is no explicit versioning.)

在这种不一致的情况下，MIT许可证并不是唯一的选择。例如，BSD许可的第3条款和一个较老的第4条款，尽管其中并没有针对版本控制的明显条款。

So, there you have it. Pick your date. Precursors from 1985. The X Consortium or X11 License variant from 1987. Or the Expat License from 1998 or 1999.

好了，解释到这里。选择你的日期吧。是1985年的先驱许可证。 还是取自1987年的X财团许可证或是X11变种证。亦或是1998或1999年的可进行外部引用许可证。

Thanks to the participants in [this Twitter thread](https://web.archive.org/web/20190402160714/https:/gist.github.com/humphd/2832b267ee1dfc0329a58a638bc20d4c) for making this article possible.

最后，感谢参与[本Twitter话题](https://web.archive.org/web/20190402160714/https:/gist.github.com/humphd/2832b267ee1dfc0329a58a638bc20d4c)的诸多评论者们，ta们使此文成为可能。
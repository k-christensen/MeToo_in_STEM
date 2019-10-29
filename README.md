# #MeToo and STEM
### _By Kate Christensen_

_____________
## Contents:
- `metoo_stem.py`: script to scrape stories from [metoostem.com](https://metoostem.com/stories/) 

- `exploratory.ipynb`: rough exploratory analysis of the data and its collection

- `me_too_STEM.zip`: corpus of #metoo stories within STEM taken from [metoostem.com](https://metoostem.com/stories/)

- `reddit_metoo.zip`: corpus of #metoo stories taken from r/metoo, stories taken were either tagged "Personal" or "Serious/personal" (so no news stories or research questions were mistakenly added to the corpus)

- `reddit_metoo.py`: script to scrape stories from r/metoo on reddit
    - **Note**: client_id, client_secret, and user_agent are required to run this script as this interacts with the reddit API
______________________________


### About Me Too:
Me Too was originally started in 2006 by Tarana Burke, but went viral in 2017 following the sexual abuse allegations of Harvey Weinstein and Alyssa Milano's tweet: 

![Alyssa Milano's tweet](https://mediad.publicbroadcasting.net/p/ipr/files/styles/x_large/public/201811/MeTooAlyssa.JPG)

[More info about the MeToo movement here](https://en.wikipedia.org/wiki/Me_Too_movement)

This movement has become a catalyst for women to share their own stories of sexual harassment and sexual assault they have experienced in their own lives. 
________________

### Motivation to focus on STEM:
Anyone who has worked in STEM (science, technology, engineering, and mathematics) can tell you that the field is markedly male-dominated (with the exception of social sciences).

[More info about women in STEM here](https://en.wikipedia.org/wiki/Women_in_STEM_fields)

Most troubling is that the percentage of female computer and mathematical scientists is at 26.4 percent as of 2015, illustrated in the graph below:

![graph](https://www.nsf.gov/statistics/2018/nsb20181/assets/901/figures/fig03-27.png) 

This is particularly worrisome because we are entering an age where tech and particularly AI is becoming an increasingly integral part of our lives. When women are not included in the conversation of how our AI evolves, we run into issues such as [gender bias within abusive language detection](https://www.aclweb.org/anthology/D18-1302/) and [biased](https://www.aclweb.org/anthology/W19-3801/) [pronoun resolution](https://www.aclweb.org/anthology/N18-2002/) and issues where biases are not just existent, but amplified within models used for [machine translation](https://medium.com/@laurahelendouglas/ai-is-not-just-learning-our-biases-it-is-amplifying-them-4d0dee75931d) and [object classification](https://www.aclweb.org/anthology/D17-1323/). [Here](https://www.aclweb.org/anthology/P19-1159.pdf) is a review of various gender bias issues within the field of NLP (Natural Language Processing). AI is only as unbiased as its teachers, and when the teachers are a largely homogenous group, it will contain more bias, and the teachers may not even think to mitigate said biases. 

So the question remains, why are there so few women in STEM? Of course, when dealing with a systemic issue such as this, there is no straightforward answer. There are many factors at play, but one reason in particular that women either do not enter or leave the field is because of the culture. As said [here](https://metoostem.com/), women in STEM have the highest rate of sexual harassment of any profession outside the military. This is indicative of a toxic culture within the field that needs to be examined and addressed. With my analysis of people's #metoo stories both within STEM and and outside, I hope to identify unique patterns within the field that are not just the patterns of sexism we've seen everywhere else in the #metoo movement. By identifying these patterns, I hope to shed light on the field-specific issues or issues more prevalent within the field. By doing this, I can more concretely delinate the culture of sexism within the field. With a more concrete, data-driven analysis of this culture, we can find better ways to combat this culture, and hopefully foster a culture where women not only enter STEM, but stay in it.

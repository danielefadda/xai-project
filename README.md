# XAI Project - Website 

The theme used in the website is a customization of Jekyll `al-folio` theme.

- To update publication list update the `xai_papers.bib`
- To update news page and generate news cards update `xai_news_all.json`

---


## Installing and Deploying

For installation and deployment details please refer to [INSTALL.md](INSTALL.md).

## Features

### People

To update people page update the `_data/people.json` file.
People images must be saved in the following directory: `assets/img/people_img/` and referenced in the json file.
Each entry has the following structure:
```
{
    "firstName": "Fosca",
    "lastName": "Giannotti",
    "role": "Principal Investigator",
    "affiliation": "Scuola Normale",
    "type": "pl",
    "r1": "0", 
    "r2": "0",
    "r3": "0",
    "r4": "0",
    "r5": "0",
    "more": "True",
    "image": "p_Giannotti.jpg"
  }
```
set `r1`, `r2`... to 1 to visualize the research line people is working on
`more` tag is optional and will display a personal page with details of each person (coming soon).
`image` require only the file name (path is defined in the layout code)


---

### Publications

Your publications' page is generated automatically from your BibTex bibliography. Simply edit [\_bibliography/papers.bib](_bibliography/papers.bib). You can also add new `*.bib` files and customize the look of your publications however you like by editing [\_pages/publications.md](_pages/publications.md). By default, the publications will be sorted by year and the most recent will be displayed first. You can change this behavior and more in the `Jekyll Scholar` section in [\_config.yml](_config.yml) file.

You can add extra information to a publication, like a PDF file in the [assets/pdf/](assets/pdf/) directory and add the path to the PDF file in the BibTeX entry with the `pdf` field. Some of the supported fields are: `abstract`, `altmetric`, `arxiv`, `bibtex_show`, `blog`, `code`, `dimensions`, `doi`, `eprint`, `html`, `isbn`, `pdf`, `pmid`, `poster`, `slides`, `supp`, `video`, and `website`.

A sample BibTeX entry is shown below:

```bibtex
@article{einstein1905movement,
  title={On the movement of small particles suspended in stationary liquids required by the molecular-kinetic theory of heat},
  author={Einstein, Albert},
  journal={Annalen der Physik},
  volume={17},
  number={8},
  pages={549--560},
  year={1905},
  publisher={Wiley Online Library},
  pdf={/assets/pdf/einstein1905movement.pdf},
  doi={10.1002/andp.19053220806},
    }
```

After you have updated your BibTeX file, you can cite your publications in your markdown files using the `{% cite %}` tag. For example, `{% cite einstein1905movement %}` will cite the publication with the key `einstein1905movement`. You can also cite multiple publications at once, like this: `{% cite einstein1905movement einstein1950meaning %}`. You can also include a complete reference in your markdown file by using the `{% reference  einstein1905movement %}` tag.


---

### Research Lines

This Jekyll theme implements `collections` to let you break up your work into categories. `projects` collection is used to describe Research Lines.


## News

Items from the `news` are automatically displayed on the news page.
To update news page:
- update  `xai_news_all.json` to generate news cards 
- run `create_news.ipynb` to create single news entries Each news will be a markdown file in the form of `2022-12-21-GLocalX.md` and will be saved in the `_posts/xai/` folder. (If the file already exists don't worry: nothing will be overwritten!)
- The generated markdown is a template usefull to easily write the blogpost, update this file.

Following example is an entry to update news cards.
`selected` is a tag to filter selected news in the homepage
`inline` is a tag to display the title of the news without internal or external link
`onlylink` is a tag to display the card news and refers it to an external webpage (the one in the `link` tag) 

```
{
    "image": "/assets/img/news/workflow_reason_x.png",
    "title": "ReasonX",
    "link": "https://github.com/lstate/REASONX",
    "content": "Declarative, interactive explanations for decision trees",
    "selected": true,
    "inline": false,
    "categories": "Workshop",
    "id": 45,
    "date_verb": "Apr 18, 2024",
    "date": "2024-04-18 00:00:00-0000",
    "onlylink": false
  }
```

## Seminars

to quick update the seminars page run the `import_calendar.py` script. 
It will update the `_posts/xai/` folder with the new seminars, creating a markdown file for each seminar.
The new md file will be named with the date of the seminar and the title of the seminar.
the date of the seminar is the current date if the seminar is in the future, otherwise it is the date of the seminar.
the event-date is the real date of the seminar. The date is used to sort the seminars in the page. 
Pay attention to the assigned date, for this reason.
Before publishing the new seminars, check the generated md files and update the content if needed.
We try to clean the content as much as possible, but sometimes the content is not well formatted.

In case of connection problems or other issues, use the `import_calendar.ipynb` to debug the py script.


## Layout

#### Full support for math & code

The theme supports fast math typesetting through [MathJax](https://www.mathjax.org/) and code syntax highlighting using [GitHub style](https://github.com/jwarby/jekyll-pygments-themes).

#### Photos, Audio, Video and more

Photo formatting is made simple using [Bootstrap's grid system](https://getbootstrap.com/docs/4.4/layout/grid/). Easily create beautiful grids within your blog posts and project pages, also with support for [video](https://alshedivat.github.io/al-folio/blog/2023/videos/) and [audio](https://alshedivat.github.io/al-folio/blog/2023/audios/) embeds:

<p align="center">
  <a href="https://alshedivat.github.io/al-folio/projects/1_project/">
    <img src="readme_preview/photos-screenshot.png" width="75%">
  </a>
</p>

---

### Other features

#### GitHub's repositories and user stats

The theme uses [github-readme-stats](https://github.com/anuraghazra/github-readme-stats) and [github-profile-trophy](https://github.com/ryo-ma/github-profile-trophy) to display GitHub repositories and user stats on the `/repositories/` page.

[![Repositories Preview](readme_preview/repositories.png)](https://alshedivat.github.io/al-folio/repositories/)

Edit the `_data/repositories.yml` and change the `github_users` and `github_repos` lists to include your own GitHub profile and repositories to the `/repositories/` page.

You may also use the following codes for displaying this in any other pages.

```html
<!-- code for GitHub users -->
{% if site.data.repositories.github_users %}
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for user in site.data.repositories.github_users %} {% include repository/repo_user.liquid username=user %} {% endfor %}
</div>
{% endif %}


<!-- code for GitHub repositories -->
{% if site.data.repositories.github_repos %}
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %} {% include repository/repo.liquid repository=repo %} {% endfor %}
</div>
{% endif %}
```

---

#### Theming

You can change css style by editing the `--global-theme-color` variable in the `_sass/_themes.scss` file. Other color variables are listed there as well. The stock theme color options available can be found at [\_sass/\_variables.scss](_sass/_variables.scss). You can also add your own colors to this file assigning each a name for ease of use across the template.


---

#### Atom (RSS-like) Feed

It generates an Atom (RSS-like) feed of your posts, useful for Atom and RSS readers. The feed is reachable simply by typing after your homepage `/feed.xml`. E.g. assuming your website mountpoint is the main folder, you can type `yourusername.github.io/feed.xml`
## License

The theme is available as open source under the terms of the [MIT License](https://github.com/alshedivat/al-folio/blob/master/LICENSE).

Originally, **al-folio** was based on the [\*folio theme](https://github.com/bogoli/-folio) (published by [Lia Bogoev](https://liabogoev.com) and under the MIT license). Since then, it got a full re-write of the styles and many additional cool features.

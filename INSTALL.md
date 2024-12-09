# XAI Project - Website 

- To update publication list update the `xai_papers.bib`
- To update news page and generate news cards update `xai_news_all.json`


---

- Use the file `header.pug` to update main menu.
- To update events create an object into the file `src\includes\_config.pug` in the `news` list. For example:
```
 news = [
    {
        image: 'assets/images/blog/dubaiExpo.png',
        title: 'Expo Dubai: High-Level Forum on EU Vision for TrustworthyAI',
        link: 'news_dubaiExpo.html', 
        category: 'Forum',
        content: "Event organised by EU Commission to bring European AI Excellence & Trust approaches to the world",
        date: '15-16 March 2022 13:30 – 15:00 CET'
    },
    {...}
]
```
`link: 'news_dubaiExpo.html'` è una pagina html con template news e path `news_*.html`

- To add people to the *people page* `src\includes\_config.pug` in the `people` list. For example:
 
```
 people = [
                {
                    'firstName': 'Salvatore',
                    'lastName': 'Ruggieri',
                    'role': 'Full Professor',
                    'affiliation': 'University of Pisa',
                    'type': 'core',
                    'researchLine': '1 ▪ 2',
                    'researchLeader': '2',
                    'r1': '1',
                    'r2': '1',
                    'r3': '0',
                    'r4': '0',
                    'r5': '0',
                    'more': 'True'
                },
    {...}
]
```


---

### Deployment to an hosting server (non GitHub Pages)

If you decide to not use GitHub Pages and host your page elsewhere, simply run:

```bash
$ bundle exec jekyll build
```

which will (re-)generate the static webpage in the `_site/` folder.
Then simply copy the contents of the `_site/` directory to your hosting server.

If you also want to remove unused css classes from your file, run:

```bash
$ purgecss -c purgecss.config.js
```

which will replace the css files in the `_site/assets/css/` folder with the purged css files.

**Note:** Make sure to correctly set the `url` and `baseurl` fields in `_config.yml` before building the webpage. If you are deploying your webpage to `your-domain.com/your-project/`, you must set `url: your-domain.com` and `baseurl: /your-project/`. If you are deploying directly to `your-domain.com`, leave `baseurl` blank, **do not delete it**.

### Deployment to a separate repository (advanced users only)

**Note:** Do not try using this method unless you know what you are doing (make sure you are familiar with [publishing sources](https://help.github.com/en/github/working-with-github-pages/about-github-pages#publishing-sources-for-github-pages-sites)). This approach allows to have the website's source code in one repository and the deployment version in a different repository.

Let's assume that your website's publishing source is a `publishing-source` subdirectory of a git-versioned repository cloned under `$HOME/repo/`.
For a user site this could well be something like `$HOME/<user>.github.io`.

Firstly, from the deployment repo dir, checkout the git branch hosting your publishing source.

Then from the website sources dir (commonly your al-folio fork's clone):

```bash
$ bundle exec jekyll build --destination $HOME/repo/publishing-source
```

This will instruct jekyll to deploy the website under `$HOME/repo/publishing-source`.

**Note:** Jekyll will clean `$HOME/repo/publishing-source` before building!

The quote below is taken directly from the [jekyll configuration docs](https://jekyllrb.com/docs/configuration/options/):

> Destination folders are cleaned on site builds
>
> The contents of `<destination>` are automatically cleaned, by default, when the site is built. Files or folders that are not created by your site will be removed. Some files could be retained by specifying them within the `<keep_files>` configuration directive.
>
> Do not use an important location for `<destination>`; instead, use it as a staging area and copy files from there to your web server.

If `$HOME/repo/publishing-source` contains files that you want jekyll to leave untouched, specify them under `keep_files` in `_config.yml`.
In its default configuration, al-folio will copy the top-level `README.md` to the publishing source. If you want to change this behavior, add `README.md` under `exclude` in `_config.yml`.

**Note:** Do _not_ run `jekyll clean` on your publishing source repo as this will result in the entire directory getting deleted, irrespective of the content of `keep_files` in `_config.yml`.

## Upgrading from a previous version

If you installed **al-folio** as described above, you can configure a [GitHub action](https://github.com/AndreasAugustin/actions-template-sync) to automatically sync your repository with the latest version of the theme.

Go to Settings -> Actions -> General -> Workflow permissions, give Read and write permissions to GitHub Actions, check "Allow GitHub Actions to create and approve pull requests", and save your changes.

Then go to Actions -> New workflow -> set up a workflow yourself, setup the following workflow and commit your changes:

```yaml
name: Sync from template
on:
  # cronjob trigger
  schedule:
    - cron: "0 0 1 * *"
  # manual trigger
  workflow_dispatch:
jobs:
  repo-sync:
    runs-on: ubuntu-latest
    steps:
      # To use this repository's private action, you must check out the repository
      - name: Checkout
        uses: actions/checkout@v4
      - name: actions-template-sync
        uses: AndreasAugustin/actions-template-sync@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          source_repo_path: alshedivat/al-folio
          upstream_branch: master
```

You will receive a pull request within your repository if there are some changes available in the template.

Another option is to manually update your code by following the steps below:

```bash
# Assuming the current directory is <your-repo-name>
$ git remote add upstream https://github.com/alshedivat/al-folio.git
$ git fetch upstream
$ git rebase v0.11.0
```

If you have extensively customized a previous version, it might be trickier to upgrade.
You can still follow the steps above, but `git rebase` may result in merge conflicts that must be resolved.
See [git rebase manual](https://help.github.com/en/github/using-git/about-git-rebase) and how to [resolve conflicts](https://help.github.com/en/github/using-git/resolving-merge-conflicts-after-a-git-rebase) for more information.
If rebasing is too complicated, we recommend re-installing the new version of the theme from scratch and port over your content and changes from the previous version manually. You can use tools like [meld](https://meldmerge.org/)
or [winmerge](https://winmerge.org/) to help in this process.

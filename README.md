# wp2.2_reference

> Reference git repository for data-mining

This repository is to be used with [wp2.2_dev](https://github.com/OPEN-NEXT/wp2.2_dev) which contains scripts that mine git repository metadata. Testing those scripts against "real"/production repositories with long commit histories and lots of branches and forks take a long time, so this repository was created. See [wp2.2_dev issue #3](https://github.com/OPEN-NEXT/wp2.2_dev/issues/3).

The plan is to artificially create items and activities in this repository that our data mining scripts would look for including, but not limited to, commits, branches (and branches of branches), merges, forks (and forks of forks with their own activities), and issues. The goal is to make this repository representative of common activity patterns that you would see in [open source](https://opensource.org/osd) projects hosted on GitHub.

## License

© 2020 Pen-Yuan Hsing et al.

Code (files in `src`): \
[GNU GPLv3 or later](../LICENSE)

Non-code (files not in `src`): \
[Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)
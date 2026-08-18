# Documentation Workflows

This repository contains composite actions and workflows that automate documentation
quality checks.

## Requirements

To use the workflows in your documentation project, it's recommended that you
incorporate Canonical's [Sphinx Starter
Pack](https://github.com/canonical/sphinx-docs-starter-pack). With the Starter Pack in
place, you can use the workflows without overriding the default inputs or implementing
the checks in your own Makefile.

## `documentation-checks.yaml`

The primary documentation workflow checks spelling, links, and inclusive language in a
documentation project.

### Usage

If your project uses the Starter Pack, you can add the documentation checks to a new
or existing workflow's jobs with:

```yaml
jobs:
  [...]
  documentation-checks:
    uses: canonical/documentation-workflows/.github/workflows/documentation-checks.yaml@main
    with:
      working-directory: 'docs'
```

### Inputs

If your project doesn't use the Starter Pack or consumes it in a non-traditional way,
declare any of the following inputs to customize the workflow as needed:

| Input               | Description                                                    | Default                      |
|---------------------|----------------------------------------------------------------|------------------------------|
| `working-directory` | The root of the documentation project. This input is required. | None                         |
| `python-version`    | The Python interpreter to use for the workflow's jobs.         | `'3.10'`                     |
| `fetch-depth`       | The number of commits to fetch from your repository.           | The full history is fetched. |
| `submodules`        | Whether to check out submodules along with the repository.     | `false`                      |
| `runs-on`           | The host system for the workflow's runners.                    | `'["ubuntu-24.04"]'`         |
| `makefile`          | The Makefile that checks are invoked from.                     | `'Makefile'`                 |
| `install-target`    | The make target for installing required tools.                 | `'install'`                  |
| `spelling-target`   | The make target to run for the spelling check.                 | `'spelling'`                 |
| `woke-target`       | The make target to run for the inclusive language check.       | `'woke'`                     |
| `linkcheck-target`  | The make target to run for the link check.                     | `'linkcheck'`                |

## Individual checks

Workflows are available for each individual check so that projects may run a subset of
those defined in `documentation-checks.yaml`. The following jobs are equivalent to the
`documentation-checks` job from the previous example:

```yaml
jobs:
  spell-check:
    uses: canonical/documentation-workflows/.github/workflows/spelling-check.yaml@main
    with:
      working-directory: "docs"
  inclusive-language-check:
    uses: canonical/documentation-workflows/.github/workflows/inclusive-language-check.yaml@main
    with:
      working-directory: "docs"    
  link-check:
    uses: canonical/documentation-workflows/.github/workflows/link-check.yaml@main
    with:
      working-directory: "docs"
```

Each of these workflows supports the same inputs as `documentation-checks.yaml`, save
the targets for the other checks. For example, the `link-check.yaml` workflow doesn't
support the `spelling-target` or `woke-target` inputs.

## Contributing

We welcome any and all contributions. For new features and enhancements, [open an
issue](https://github.com/canonical/documentation-workflows/issues/new) and state that
you'd like to take it on. A maintainer will then review the issue and assign it to you.

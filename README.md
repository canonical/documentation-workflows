# Documentation Workflows

This repository contains a collection of GitHub Actions and workflows designed to automate various checks and processes related to documentation. These tools aim to ensure the quality, consistency, and accuracy of documentation across projects.

## Overview

- **GitHub Actions**: We have a set of individual actions that can be used in any workflow. These actions are designed to perform specific tasks such as spell checking, inclusive language checks, and link validation.
  
- **Reusable Workflows**: In addition to individual actions, this repository offers a top-level workflow (`documentation-checks.yaml`) that combines multiple checks. This workflow can be called from other repositories, providing a comprehensive documentation validation process in a single step.

## Requirements

To be able to use the workflow, your repository must have a Makefile (at the location specified by `working-directory`) that defines the following targets:

- `make install` - install the tools needed for all checks
- `make woke` - run the inclusive language check
- `make linkcheck` - run the link validator
- `make spelling` - run the spelling check

## Using the Reusable Workflow

To utilize the `documentation-checks.yml` workflow in another repository, create a new workflow and reference it using the `uses` directive. Here's a basic example:

```yaml
name: Main Documentation Checks

on:
  - push
  - pull_request

jobs:
  documentation-checks:
    uses: canonical/documentation-workflows/.github/workflows/documentation-checks.yml@main
    with:
      working-directory: '.'
```

If you want to use a workflow version other than `main`, replace `@main` with the appropriate branch or tag.

## Contributing

We welcome contributions to improve and expand the capabilities of this repository. If you have a new check or enhancement in mind, please open an issue to discuss it or submit a pull request.

# flowlab

repo for learning GitHub flow: branches, pull requests, CI, releases and prod approvals.

## What's in it

| File | Purpose |
| --- | --- |
| `app.py` | `greet(name)` and `farewell(name)` |
| `test_app.py` | unit tests for the app |
| `.github/workflows/ci.yml` | CI: runs the tests on every PR into `main` |
| `.github/dependabot.yml` | weekly PRs to update pinned GitHub Actions |
| `.github/pull_request_template.md` | template every PR starts from |
| `.pre-commit-config.yaml` | gitleaks hook that blocks secrets at commit time |

## Getting started

```bash
git clone git@github.com:Hassan1646/flowlab.git
cd flowlab
pre-commit install        # enables the secret-scanning hook (needs pre-commit installed)
```

## Run it

```bash
python3 app.py
python3 -m unittest -v
```

## How we work

1. Branch from an up-to-date `main`: `feature/FL-XX-short-name`
2. Commit messages start with the Jira ticket: `FL-XX: what it does`
3. Open a PR into `main` and fill in the template
4. CI must be green before merging
5. Squash-merge, then delete the branch

`main` is protected: no direct pushes, no force pushes.
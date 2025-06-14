# Setting Up Dynamic Badges

This document explains how to set up dynamic badges for your Pitwall fork.

## Overview

The project includes a GitHub Actions workflow that can automatically update coverage and test badges. This requires some initial setup to create GitHub Gists and configure repository secrets.

## Setup Steps

### 1. Create GitHub Gists

You need to create two public GitHub Gists to store the badge data:

1. **Coverage Badge Gist**:
   - Go to https://gist.github.com
   - Create a new public gist
   - Filename: `pitwall-coverage.json`
   - Content: `{"schemaVersion": 1, "label": "coverage", "message": "0%", "color": "red"}`
   - Save and note the Gist ID from the URL

2. **Tests Badge Gist**:
   - Create another public gist
   - Filename: `pitwall-tests.json`
   - Content: `{"schemaVersion": 1, "label": "tests", "message": "passing", "color": "brightgreen"}`
   - Save and note the Gist ID from the URL

### 2. Configure Repository Secrets

In your GitHub repository:

1. Go to Settings → Secrets and variables → Actions
2. Add the following repository secrets:
   - `COVERAGE_GIST_ID`: The ID from your coverage gist URL
   - `TESTS_GIST_ID`: The ID from your tests gist URL

### 3. Update README Badges

Replace the static badges in README.md with dynamic ones:

```markdown
[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/yourusername/your-coverage-gist-id/raw/pitwall-coverage.json)](https://github.com/yourusername/pitwall)
[![Tests](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/yourusername/your-tests-gist-id/raw/pitwall-tests.json)](https://github.com/yourusername/pitwall)
```

Replace:
- `yourusername` with your GitHub username
- `your-coverage-gist-id` with your coverage gist ID
- `your-tests-gist-id` with your tests gist ID

### 4. Enable Automatic Updates

Once the secrets are configured, the badge workflow will:

- Run manually via workflow dispatch
- Update badges when you have both gist IDs configured
- Skip badge updates gracefully if secrets are missing

### 5. Manual Badge Update

You can manually trigger a badge update:

1. Go to Actions → Update Badges
2. Click "Run workflow"
3. The workflow will generate a new coverage report and update the badges

## Troubleshooting

### Workflow Skipped

If the badge workflow is being skipped, ensure:
- Both `COVERAGE_GIST_ID` and `TESTS_GIST_ID` secrets are set
- The secrets contain valid gist IDs
- The gists are public

### Badge Not Updating

If badges aren't updating:
- Check the workflow logs for errors
- Verify the gist IDs are correct
- Ensure the GitHub token has permissions to update gists
- Try running the workflow manually

### API Rate Limits

The workflow uses GitHub's API which has rate limits. If you encounter rate limiting:
- Reduce the frequency of badge updates
- Use workflow dispatch instead of automatic triggers
- Check your API usage in GitHub settings

## Alternative: Static Badges

If you prefer simpler setup, you can use static badges instead:

```markdown
[![Coverage](https://img.shields.io/badge/coverage-66%25-yellow)](https://github.com/yourusername/pitwall)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](https://github.com/yourusername/pitwall/actions)
```

Update the coverage percentage manually when needed.
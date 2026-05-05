# Branch Protection Rules Setup Guide

## Overview

This guide explains how to set up branch protection rules on GitHub to enforce professional development practices and prevent direct pushes to the main branch.

## Why Branch Protection Rules?

✅ **Prevent Accidental Bugs**: Requires code review before merge
✅ **Maintain Code Quality**: Enforces tests and status checks
✅ **Team Collaboration**: Ensures team awareness of changes
✅ **Audit Trail**: All changes tracked through PRs
✅ **Security**: Protects production code

---

## Step-by-Step Setup

### **Access Branch Protection Rules**

1. Go to: https://github.com/farukhfrk/langchain-practice/settings/branches
2. Click **Add rule**

### **Rule Configuration**

#### **1. Branch Name Pattern**
```
Pattern: main
```
Apply rules to the main branch.

#### **2. Require a Pull Request Before Merging**
✅ **ENABLE** this option

**Sub-options:**
- ✅ **Dismiss stale pull request approvals when new commits are pushed**
  - Ensures reviews stay current with latest code

- ✅ **Require code review from code owners**
  - Enforces review from CODEOWNERS file (optional)

**Why**: Prevents direct commits/pushes to main. All changes must go through PR.

#### **3. Require Status Checks to Pass Before Merging**
✅ **ENABLE** this option

**Sub-options:**
- ✅ **Require branches to be up to date before merging**
  - PR must be rebased on latest main before merge
  - Prevents merge conflicts

**Why**: Ensures all automated checks pass before code reaches main.

#### **4. Require Code Reviews Before Merging**
✅ **ENABLE** this option

**Set to**: `1` (minimum number of approvals required)

**Sub-options:**
- ✅ **Require code review from code owners** (optional)
  - Requires specific people to review

**Why**: At least one person must review and approve changes.

#### **5. Require Status Checks to Pass Before Merging**
✅ **ENABLE** this option

**Required status checks**:
- (Add any CI/CD checks like: Tests, Linting, etc.)
- For now: can be left empty if no CI configured

**Why**: Automated tests must pass before merge.

#### **6. Require Conversation Resolution Before Merging**
✅ **ENABLE** this option

**Why**: All PR comments must be resolved before merge.

#### **7. Require Signed Commits**
⚪ **OPTIONAL** (recommended for security)

**Why**: Verifies commits are signed with GPG key.

#### **8. Restrict Who Can Push to Matching Branches**
✅ **ENABLE** this option

**Allowed to push**: 
- Admins only (check box)
- This means even repository admins must follow the PR process

**Why**: Prevents anyone (including admins) from bypassing rules.

#### **9. Require Linear History**
⚪ **OPTIONAL** but recommended

**Why**: Prevents merge commits, keeps clean linear history.

#### **10. Allow Force Pushes**
❌ **DO NOT ENABLE**

**Why**: Protects against accidental history rewrites.

---

## Complete Configuration Checklist

```
✅ Require a pull request before merging
   ✅ Dismiss stale PR reviews when new commits pushed
   ✅ Require code review from code owners (optional)
   
✅ Require status checks to pass before merging
   ✅ Require branches to be up to date before merging
   
✅ Require code reviews before merging
   Set to: 1 or more required approvals
   
✅ Require conversation resolution before merging

✅ Restrict who can push to matching branches
   Select: Admins only

❌ Allow force pushes: DISABLED
❌ Allow deletions: DISABLED
```

---

## Workflow After Setup

### **For Developers: How to Contribute**

```bash
# 1. Create feature branch
git checkout -b feature/new-example

# 2. Make changes and commit
git add .
git commit -m "Add detailed docstring for example"

# 3. Push to GitHub
git push origin feature/new-example

# 4. Open Pull Request
#    - Go to GitHub
#    - Click "Compare & pull request"
#    - Fill in PR description
#    - Create PR

# 5. Wait for Reviews
#    - Maintainer will review code
#    - May request changes

# 6. Make Updates (if needed)
git add .
git commit -m "Address review feedback"
git push origin feature/new-example

# 7. After Approval
#    - PR can be merged to main
#    - Reviewer clicks "Merge pull request"
```

### **PR Checklist Template**

Add a PULL_REQUEST_TEMPLATE.md to automate this:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code improvement

## Testing
How was this tested?

## Checklist
- [ ] Code follows style guidelines
- [ ] Comments and docstrings added
- [ ] Tests pass locally
- [ ] No new warnings
- [ ] Changes documented
```

---

## Additional Security Rules

### **Optional: Create CODEOWNERS File**

Create `.github/CODEOWNERS`:

```
# All files require review from these people
* @farukhfrk

# Specific paths require specific reviewers
/chains/ @farukhfrk
/runnables/ @farukhfrk
/EmbeddingModels/ @farukhfrk
```

**Effect**: PRs automatically request reviews from code owners.

### **Optional: Enable Require Dismissal of Stale Reviews**

When PR is updated, old approvals are dismissed, requiring new review.

### **Optional: Require Linear History**

Prevents messy merge commits:
```bash
# Instead of merge commits, use rebase
git rebase origin/main
git push --force-with-lease
```

---

## Common Scenarios After Setup

### **Scenario 1: I Made a Direct Commit (Blocked!)**

```bash
# This will be REJECTED:
git push origin main
# Error: "protected branch hook declined"

# Solution: Use PR workflow instead
git checkout -b feature/my-change
git add .
git commit -m "My changes"
git push origin feature/my-change
# Then open PR on GitHub
```

### **Scenario 2: My PR Needs Updates After Review**

```bash
# Make requested changes
git add .
git commit -m "Address feedback"
git push origin feature/my-change

# Review automatically refreshes
# Stale approvals are dismissed
# Need re-review for merge
```

### **Scenario 3: My Branch is Outdated**

```bash
# Update your branch before merge
git fetch origin
git rebase origin/main
git push --force-with-lease

# Now branch is up-to-date
# Can be merged
```

---

## Best Practices

### ✅ Do This

1. **Create meaningful feature branches**
   ```bash
   feature/add-documentation
   fix/typo-in-readme
   docs/update-installation
   ```

2. **Write clear commit messages**
   ```bash
   git commit -m "Add comprehensive docstring to chains module"
   ```

3. **Use descriptive PR titles**
   ```
   "Add semantic similarity search example with documentation"
   ```

4. **Include PR description**
   - What changed
   - Why it changed
   - How to test

5. **Review others' PRs**
   - Comment on code
   - Suggest improvements
   - Be constructive

### ❌ Don't Do This

1. ❌ Don't push directly to main
2. ❌ Don't bypass review process
3. ❌ Don't use generic commit messages ("fix" or "update")
4. ❌ Don't force-push to shared branches
5. ❌ Don't merge your own PRs without team consensus

---

## Troubleshooting

### **Problem: "This branch has no pull requests"**
- Your branch might not have pushes yet
- Try creating a small test PR first

### **Problem: "Branch is out of date"**
```bash
git fetch origin
git rebase origin/main
git push --force-with-lease origin feature-branch
```

### **Problem: "Need approval from code owner"**
- Wait for designated reviewer
- Tag them in PR comments with @username

### **Problem: Cannot push to main**
- Good! That means rules are working
- Create a feature branch instead
- Open a PR for your changes

---

## Viewing Your Rules

To see applied rules:

1. Go to: https://github.com/farukhfrk/langchain-practice/settings/branches
2. Rules appear under "Branch protection rules"
3. Click rule to view/edit details
4. Click pencil icon to modify
5. Click trash icon to delete

---

## Command Reference

```bash
# View branch rules (locally - just informational)
git config --get-all branch.*.protect

# List all branches
git branch -a

# Create and switch to feature branch
git checkout -b feature/my-feature

# Push new branch
git push -u origin feature/my-feature

# Update branch from main
git fetch origin
git rebase origin/main

# Force push updated branch (safe version)
git push --force-with-lease origin feature/my-feature

# Delete local branch
git branch -d feature/my-feature

# Delete remote branch
git push origin --delete feature/my-feature
```

---

## Summary

**After setting up branch protection rules:**

✅ No one can push directly to main
✅ All changes require PR
✅ All PRs require review
✅ All PRs require passing checks
✅ Maintains code quality
✅ Creates audit trail
✅ Professional workflow

**Your repository is now production-ready!** 🚀

---

**Last Updated**: May 5, 2026
**Repository**: https://github.com/farukhfrk/langchain-practice

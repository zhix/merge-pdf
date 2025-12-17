# How to Push Your Project to GitHub

Since you have initialized Git locally, follow these steps to put your project on GitHub.

## 1. Create a Repository on GitHub
1. Log in to [GitHub](https://github.com).
2. Click the **+** icon in the top-right corner and select **New repository**.
3. **Repository name**: `merge-pdfs` (or whatever you prefer).
4. **Visibility**: Public or Private.
5. **Do NOT** initialize with README, .gitignore, or License (we already have them).
6. Click **Create repository**.

## 2. Link Local Repo to GitHub
Copy the commands shown on the GitHub "Quick setup" page (under "…or push an existing repository from the command line"), which look like this:

```bash
git remote add origin https://github.com/YOUR_USERNAME/merge-pdfs.git
git branch -M main
git push -u origin main
```

## 3. Run the commands
Paste those commands into your terminal (in the project folder).

## Common Issues
- **Authentication**: You might be asked to sign in. If you have 2FA enabled, you'll need a Personal Access Token or SSH keys.
- **"Remote origin already exists"**: If you see this, run `git remote remove origin` first.

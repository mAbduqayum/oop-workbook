# Git - Distributed Version Control System

## Table of Contents

1. [What is Git?](#what-is-git)
2. [Git Fundamentals](#git-fundamentals)
3. [Git Workflow](#git-workflow)
4. [Branching and Merging](#branching-and-merging)
5. [Common Git Commands](#common-git-commands)
6. [Best Practices](#best-practices)
7. [Git Workflow Examples](#git-workflow-examples)
8. [Troubleshooting Common Issues](#troubleshooting-common-issues)

## What is Git?

**Git** is a distributed version control system created by Linus Torvalds in 2005. It's designed to handle everything
from small to huge projects with speed and efficiency.

### Key Features of Git:

- **Distributed**: Every clone is a full backup
- **Fast**: Local operations are lightning fast
- **Data Integrity**: Everything has checksum
- **Branching**: Lightweight branching and merging
- **Staging Area**: Intermediate area for preparing commits

```mermaid
graph LR
    A[Working Directory] --> B[Staging Area]
    B --> C[Git Repository]
    C --> D[Remote Repository]

    A -.->|git add| B
    B -.->|git commit| C
    C -.->|git push| D
    D -.->|git pull/fetch| C
    C -.->|git checkout| A

    style A fill:#ffe0b2,stroke:#333,stroke-width:2px,color:#000
    style B fill:#bbdefb,stroke:#333,stroke-width:2px,color:#000
    style C fill:#c8e6c8,stroke:#333,stroke-width:2px,color:#000
    style D fill:#f8bbd9,stroke:#333,stroke-width:2px,color:#000
```

## Git Fundamentals

### The Three States

Git has three main states that your files can reside in:

1. **Modified**: Changed but not committed to the database
2. **Staged**: Marked to go into the next commit snapshot
3. **Committed**: Safely stored in the local database

### Git Areas

```mermaid
graph TB
    subgraph "Git Project"
        A[Working Directory<br/>Modified Files]
        B[Staging Area<br/>Staged Files]
        C[Git Directory<br/>Committed Files]
    end

    A -->|git add| B
    B -->|git commit| C
    C -->|git checkout| A

    style A fill:#ffcdd2,stroke:#333,stroke-width:2px,color:#000
    style B fill:#bbdefb,stroke:#333,stroke-width:2px,color:#000
    style C fill:#c8e6c8,stroke:#333,stroke-width:2px,color:#000
```

### Git Object Types

Git stores four types of objects:

1. **Blob**: File content
2. **Tree**: Directory structure
3. **Commit**: Snapshot with metadata
4. **Tag**: Named reference to a commit

```mermaid
graph TD
    A[Commit Object] --> B[Tree Object]
    A --> C[Parent Commit]
    A --> D[Author Info]
    A --> E[Commit Message]

    B --> F[File1.txt<br/>Blob]
    B --> G[File2.py<br/>Blob]
    B --> H[Subdirectory<br/>Tree]

    H --> I[File3.md<br/>Blob]

    style A fill:#c8e6c8,stroke:#333,stroke-width:2px,color:#000
    style B fill:#bbdefb,stroke:#333,stroke-width:2px,color:#000
    style C fill:#ffcdd2,stroke:#333,stroke-width:2px,color:#000
    style D fill:#ffcdd2,stroke:#333,stroke-width:2px,color:#000
    style E fill:#ffcdd2,stroke:#333,stroke-width:2px,color:#000
    style F fill:#ffe0b2,stroke:#333,stroke-width:2px,color:#000
    style G fill:#ffe0b2,stroke:#333,stroke-width:2px,color:#000
    style H fill:#bbdefb,stroke:#333,stroke-width:2px,color:#000
    style I fill:#ffe0b2,stroke:#333,stroke-width:2px,color:#000
```

## Git Workflow

### Basic Git Workflow

```mermaid
flowchart TD
    A[Initialize Repository<br/>`git init`] --> B[Add Files<br/>`git add`]
    B --> C[Commit Changes<br/>`git commit`]
    C --> D[Make Changes]
    D --> B
    C --> E[Push to Remote<br/>`git push`]
    E --> F[Pull Updates<br/>`git pull`]
    F --> D

    style A fill:#c8e6c8,stroke:#333,stroke-width:2px,color:#000
    style B fill:#bbdefb,stroke:#333,stroke-width:2px,color:#000
    style C fill:#c8e6c8,stroke:#333,stroke-width:2px,color:#000
    style D fill:#ffe0b2,stroke:#333,stroke-width:2px,color:#000
    style E fill:#f8bbd9,stroke:#333,stroke-width:2px,color:#000
    style F fill:#f8bbd9,stroke:#333,stroke-width:2px,color:#000
```

### Detailed Workflow Steps

1. **Initialize**: Create a new Git repository
2. **Add**: Stage changes for commit
3. **Commit**: Save changes to a local repository
4. **Push**: Upload changes to a remote repository
5. **Pull**: Download changes from a remote repository
6. **Merge**: Combine different branches

## Branching and Merging

### What is Branching?

Branching allows you to diverge from the main line of development and work on features independently.

```mermaid
gitGraph
    commit id: "Initial commit"
    commit id: "Add basic structure"
    branch feature-branch
    checkout feature-branch
    commit id: "Work on feature"
    commit id: "Complete feature"
    checkout main
    commit id: "Fix bug"
    merge feature-branch
    commit id: "Release v1.0"
```

### Branch Types

1. **Main/Master**: Primary development branch
2. **Feature Branches**: For developing new features
3. **Hotfix Branches**: For critical bug fixes
4. **Release Branches**: For preparing releases

### Git Flow Model

```mermaid
gitGraph
    commit id: "Start"

    branch develop
    checkout develop
    commit id: "Dev work"

    branch feature/login
    checkout feature/login
    commit id: "Login feature"
    checkout develop
    merge feature/login

    branch release/v1.0
    checkout release/v1.0
    commit id: "Prepare release"

    checkout main
    merge release/v1.0
    commit id: "v1.0"

    checkout develop
    merge release/v1.0
```

## Common Git Commands

### Repository Setup

```bash
# Initialize a new repository
git init

# Clone an existing repository
git clone <repository-url>

# Add remote repository
git remote add origin <repository-url>
```

### Basic Operations

```bash
# Check status
git status

# Add files to staging area
git add <file>
git add .  # Add all files

# Commit changes
git commit -m "Commit message"

# Push to remote repository
git push origin main

# Pull from remote repository
git pull origin main
```

### Branching Commands

```bash
# List branches
git branch

# Create new branch
git branch <branch-name>

# Switch to branch
git checkout <branch-name>

# Create and switch to new branch
git checkout -b <branch-name>

# Merge branch
git merge <branch-name>

# Delete branch
git branch -d <branch-name>
```

### History and Logs

```bash
# View commit history
git log

# View compact history
git log --oneline

# View changes
git diff

# View staged changes
git diff --staged
```

### Working with Remotes

```bash
# View remote repositories
git remote -v

# Add remote
git remote add upstream <url>

# Fetch from remote
git fetch origin

# Push to different remote
git push upstream main
```

## Best Practices

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Keep the first line under 50 characters
- Use imperative mood
- Be descriptive but concise

```
Good commit messages:
✓ Add user authentication system
✓ Fix memory leak in data processor
✓ Update README with installation instructions

Bad commit messages:
✗ Fixed stuff
✗ Working on it
✗ asdfgh
```

### Branching Strategy

```mermaid
graph TD
    A[main] --> B[develop]
    B --> C[feature/user-auth]
    B --> D[feature/payment]
    B --> E[release/v1.0]
    A --> F[hotfix/critical-bug]

    C --> B
    D --> B
    E --> A
    E --> B
    F --> A
    F --> B

    style A fill:#ff8a80,stroke:#333,stroke-width:2px,color:#000
    style B fill:#4dd0e1,stroke:#333,stroke-width:2px,color:#000
    style C fill:#64b5f6,stroke:#333,stroke-width:2px,color:#000
    style D fill:#64b5f6,stroke:#333,stroke-width:2px,color:#000
    style E fill:#81c784,stroke:#333,stroke-width:2px,color:#000
    style F fill:#ffcc02,stroke:#333,stroke-width:2px,color:#000
```

### Modern Python Project Structure

```
project/
├── .git/                   # Git repository
│   ├── objects/            # Git object database (blobs, trees, commits)
│   ├── refs/               # Branch and tag references
│   │   ├── heads/          # Local branches
│   │   └── remotes/        # Remote tracking branches
│   ├── HEAD                # Current branch pointer
│   ├── config              # Repository configuration
│   └── index               # Staging area
├── .venv/                  # Virtual environment (uv)
├── src/                    # Source code
├── .gitignore              # Files to ignore
├── pyproject.toml          # Project metadata and dependencies (uv)
├── README.md               # Project documentation
└── uv.lock                 # Dependency lockfile (uv)
```

## Git Workflow Examples

### Feature Development Workflow

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant Local as Local Repo
    participant Remote as Remote Repo

    Dev->>Local: git checkout -b feature/new-login
    Dev->>Local: Make changes
    Dev->>Local: git add .
    Dev->>Local: git commit -m "Add login feature"
    Dev->>Remote: git push origin feature/new-login
    Remote->>Remote: Create Pull Request
    Remote->>Local: git checkout main
    Remote->>Local: git pull origin main
    Local->>Local: git branch -d feature/new-login
```

### Collaboration Workflow

```mermaid
graph TD
    A[Developer A<br/>Feature Branch] --> C[Main Repository]
    B[Developer B<br/>Feature Branch] --> C
    C --> D[Code Review]
    D --> E[Merge to Main]
    E --> F[Deploy]

    C --> G[Developer C<br/>Pull Latest]
    G --> H[New Feature Branch]
    H --> C

    style A fill:#64b5f6,stroke:#333,stroke-width:2px,color:#000
    style B fill:#64b5f6,stroke:#333,stroke-width:2px,color:#000
    style C fill:#f8bbd9,stroke:#333,stroke-width:2px,color:#000
    style D fill:#ffe0b2,stroke:#333,stroke-width:2px,color:#000
    style E fill:#c8e6c8,stroke:#333,stroke-width:2px,color:#000
    style F fill:#ffcdd2,stroke:#333,stroke-width:2px,color:#000
    style G fill:#64b5f6,stroke:#333,stroke-width:2px,color:#000
    style H fill:#64b5f6,stroke:#333,stroke-width:2px,color:#000
```

## Troubleshooting Common Issues

### Merge Conflicts

When Git can't automatically merge changes:

```bash
# See conflicted files
git status

# Edit files to resolve conflicts
# Look for conflict markers: <<<<<<< ======= >>>>>>>

# Add resolved files
git add <resolved-file>

# Complete the merge
git commit
```

### Undoing Changes

```bash
# Unstage files
git reset HEAD <file>

# Discard local changes
git checkout -- <file>

# Undo last commit (keep changes)
git reset --soft HEAD^

# Undo last commit (discard changes)
git reset --hard HEAD^
```

---

## Summary

Git is a powerful distributed version control system that provides:

- **History Tracking**: Complete history of all changes
- **Branching**: Parallel development of features
- **Distributed**: Every clone is a complete backup
- **Speed**: Local operations are fast
- **Data Integrity**: Everything is checksummed

### Key Takeaways

1. Always commit frequently with meaningful messages
2. Use branches for features and experiments
3. Keep your main branch stable
4. Use `.gitignore` to exclude unnecessary files
5. Follow consistent naming conventions
6. Understand the three states: modified, staged, committed
7. Learn to resolve merge conflicts
8. Use proper branching strategies for team collaboration

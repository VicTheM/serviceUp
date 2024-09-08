#!/bin/bash

# Switch to the main branch
git checkout main

# Pull latest changes
git pull origin main

# Switch to the publish branch
git checkout publish

# Copy the docs/ and static folder folder from main
git checkout main -- docs/
git checkout main -- static/

# Commit the changes in the publish branch
git add docs/
git add static/
git commit -m "pulled updates from static folder"

# Push to the publish branch
git push origin publish

# Switch back to the main branch
git checkout main


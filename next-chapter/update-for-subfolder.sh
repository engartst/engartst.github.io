# Adding Conference Site to Existing GitHub Pages Site

This guide shows how to add your conference website as a subdirectory to your existing GitHub Pages site, so it will be accessible at `yoursite.com/conference`.

## 🎯 Overview

Instead of creating a new repository, you'll add the conference files as a subfolder in your existing GitHub Pages repository. Your site structure will look like:

```
your-existing-site/
├── index.html                 # Your main site
├── about/
├── blog/
├── conference/                # New conference section
│   ├── index.html
│   ├── css/
│   ├── js/
│   └── ...
└── other-folders/
```

## 🚀 Method 1: Using GitHub Web Interface

### Step 1: Navigate to Your Existing Repository
1. Go to your existing GitHub Pages repository
2. Make sure you're on the main/master branch
3. Click "Create new file" or "Upload files"

### Step 2: Create Conference Folder Structure
1. Click "Create new file"
2. Type `conference/index.html` (this creates the folder)
3. Copy the contents of your conference `index.html` into this file
4. Commit the change

### Step 3: Upload Remaining Files
1. Navigate into the `conference/` folder you just created
2. Upload the CSS folder: `conference/css/style.css`
3. Upload the JS folder: `conference/js/script.js`
4. Upload other files as needed

## 🔧 Method 2: Using Git Command Line

### Step 1: Clone Your Existing Repository
```bash
# Clone your existing site repository
git clone https://github.com/yourusername/your-existing-site.git
cd your-existing-site
```

### Step 2: Create Conference Subfolder
```bash
# Create the conference directory
mkdir conference

# Copy all conference files to the new directory
cp -r /Users/hse9/fake_conference_site/* conference/

# Remove files that don't belong in the subfolder
cd conference
rm GITHUB_PAGES_SETUP.md prepare-for-github.sh
```

### Step 3: Update File Paths
The conference site files need small adjustments for the subfolder:

```bash
# Update the HTML file to work in subfolder context
# (We'll do this in the next step)
```

### Step 4: Commit and Push
```bash
# Go back to repository root
cd ..

# Add all conference files
git add conference/

# Commit the changes
git commit -m "Add conference website to /conference subfolder"

# Push to GitHub
git push origin main
```

## 📝 Required File Updates

Since the conference site will be in a subfolder, you need to make a few small updates:

### Update index.html Base Path
Add this to the `<head>` section of `conference/index.html`:

```html
<base href="/conference/">
```

Or manually update all relative paths. I'll help you with this:

<function_calls>
<invoke name="create_file">
<parameter name="content">#!/bin/bash

# Script to update conference site files for subfolder deployment
# Run this from your conference directory

echo "🔧 Updating conference site for subfolder deployment..."

# Check if we're in the conference directory
if [ ! -f "index.html" ]; then
    echo "❌ Error: Please run this script from the conference directory"
    exit 1
fi

# Update HTML file paths
echo "📝 Updating index.html..."
sed -i.bak 's|href="css/|href="/conference/css/|g' index.html
sed -i.bak 's|src="js/|src="/conference/js/|g' index.html

# Update CSS file paths if any internal references exist
echo "📝 Checking CSS for path updates..."
if [ -f "css/style.css" ]; then
    # Update any URL references in CSS (uncomment if needed)
    # sed -i.bak 's|url("../|url("/conference/|g' css/style.css
    echo "✅ CSS checked"
fi

# Create a backup of the original files
echo "💾 Original files backed up with .bak extension"

echo ""
echo "🎉 Conference site updated for subfolder deployment!"
echo ""
echo "Your conference site will be available at:"
echo "https://yourusername.github.io/your-repo/conference"
echo "or"
echo "https://yourdomain.com/conference"
echo ""
echo "Next steps:"
echo "1. Test the site locally if possible"
echo "2. Commit and push the changes to GitHub"
echo "3. Wait a few minutes for GitHub Pages to update"

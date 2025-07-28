#!/bin/bash

# GitHub Pages Deployment Preparation Script
# This script helps prepare your conference website for GitHub Pages deployment

echo "🚀 Preparing Conference Website for GitHub Pages..."
echo "=================================================="

# Check if we're in the right directory
if [ ! -f "index.html" ]; then
    echo "❌ Error: index.html not found. Please run this script from your website directory."
    exit 1
fi

echo "✅ Found index.html - we're in the right directory"

# Create .gitignore file for GitHub
echo "📝 Creating .gitignore file..."
cat > .gitignore << EOL
# macOS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Editor files
.vscode/
.idea/
*.swp
*.swo
*~

# Logs
*.log
npm-debug.log*

# Temporary files
*.tmp
*.temp

# Backup files
*.bak
*.backup

# Node modules (if you add any later)
node_modules/

# Environment variables
.env
.env.local
.env.production
EOL

# Validate HTML structure
echo "🔍 Checking HTML structure..."
if grep -q "<html" index.html && grep -q "</html>" index.html; then
    echo "✅ HTML structure looks good"
else
    echo "⚠️  Warning: HTML structure may have issues"
fi

# Check for relative paths
echo "🔍 Checking for absolute file paths..."
if grep -q "file://" index.html || grep -q "C:\\" index.html; then
    echo "⚠️  Warning: Found absolute file paths. GitHub Pages needs relative paths."
    echo "   Please check your index.html for any file:// or C:\\ references"
else
    echo "✅ No absolute paths found"
fi

# Check if CSS and JS files exist
echo "🔍 Checking required files..."
if [ -f "css/style.css" ]; then
    echo "✅ CSS file found"
else
    echo "❌ Error: css/style.css not found"
fi

if [ -f "js/script.js" ]; then
    echo "✅ JavaScript file found"
else
    echo "❌ Error: js/script.js not found"
fi

# Create a simple robots.txt
echo "🤖 Creating robots.txt..."
cat > robots.txt << EOL
User-agent: *
Allow: /

Sitemap: https://yourusername.github.io/your-repo-name/sitemap.xml
EOL
echo "   📝 Remember to update the sitemap URL with your actual GitHub Pages URL"

# Create a basic sitemap.xml
echo "🗺️  Creating sitemap.xml..."
cat > sitemap.xml << EOL
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://yourusername.github.io/your-repo-name/</loc>
    <lastmod>$(date +%Y-%m-%d)</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
EOL
echo "   📝 Remember to update the URL with your actual GitHub Pages URL"

# List all files that will be uploaded
echo ""
echo "📁 Files ready for GitHub Pages:"
echo "================================"
find . -type f -not -path "./.git/*" -not -name ".*" | sort

echo ""
echo "🎉 Preparation Complete!"
echo "======================="
echo ""
echo "Next steps:"
echo "1. Review the files listed above"
echo "2. Follow the GITHUB_PAGES_SETUP.md guide to upload to GitHub"
echo "3. Enable GitHub Pages in your repository settings"
echo "4. Update robots.txt and sitemap.xml with your actual URL"
echo ""
echo "Your website will be available at: https://yourusername.github.io/your-repo-name"
echo ""
echo "Need help? Check GITHUB_PAGES_SETUP.md for detailed instructions!"

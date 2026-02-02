#!/bin/bash
# Deployment script for Issue-Based Commentary Website

# Configuration
SOURCE_DIR="/Users/davidrosser/clawd/issue-commentary"
BUILD_DIR="/Users/davidrosser/clawd/issue-commentary/_build"
DEPLOY_DIR="/var/www/html"  # Adjust to your actual web server directory

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Starting Issue-Based Commentary Website Deployment${NC}"

# Create build directory
mkdir -p $BUILD_DIR

# Copy static assets
echo -e "${GREEN}Copying static assets...${NC}"
cp -r $SOURCE_DIR/css $BUILD_DIR/
cp -r $SOURCE_DIR/js $BUILD_DIR/
cp -r $SOURCE_DIR/posts $BUILD_DIR/
cp $SOURCE_DIR/index.html $BUILD_DIR/
cp $SOURCE_DIR/sitemap.xml $BUILD_DIR/ 2>/dev/null || echo "No sitemap.xml found, will be generated"
cp $SOURCE_DIR/feed.rss $BUILD_DIR/ 2>/dev/null || echo "No feed.rss found, will be generated"

# Create additional pages
mkdir -p $BUILD_DIR/category

# Create category pages
for category in cost-of-living workers-workplace healthcare-community climate-solutions privacy-rights civic-basics; do
    cat > $BUILD_DIR/category/${category}.html << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${category//-/ } - Better World Commentary</title>
    <meta name="description" content="Articles about ${category//-/ } on Better World Commentary">
    <link rel="stylesheet" href="/css/style.css">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-YHM6QJDPFC"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-YHM6QJDPFC');
    </script>
</head>
<body>
    <header>
        <div class="container">
            <h1>Better World Commentary</h1>
            <p>Positive, solution-focused commentary on today's issues</p>
        </div>
    </header>
    
    <nav>
        <div class="container">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/category/cost-of-living/">Cost of Living</a></li>
                <li><a href="/category/workers-workplace/">Workers & Workplace</a></li>
                <li><a href="/category/healthcare-community/">Healthcare & Community</a></li>
                <li><a href="/category/climate-solutions/">Climate Solutions</a></li>
                <li><a href="/category/privacy-rights/">Privacy & Digital Rights</a></li>
                <li><a href="/category/civic-basics/">Civic Basics</a></li>
            </ul>
        </div>
    </nav>
    
    <main>
        <div class="container">
            <h1>${category//-/ } Articles</h1>
            <p>Explore our collection of constructive commentary on ${category//-/ } issues with practical solutions.</p>
            
            <div class="post-grid">
                <!-- Dynamic content would go here -->
                <div class="post-card">
                    <h3>No articles yet in this category</h3>
                    <p>Check back soon for new content addressing ${category//-/ } challenges with practical solutions.</p>
                </div>
            </div>
        </div>
    </main>
    
    <footer>
        <div class="container">
            <p>&copy; 2026 Better World Commentary. All rights reserved.</p>
            <p><a href="/affiliate-disclosure/">Affiliate Disclosure</a> | <a href="/privacy-policy/">Privacy Policy</a></p>
        </div>
    </footer>
</body>
</html>
EOF
done

# Create affiliate disclosure page
cat > $BUILD_DIR/affiliate-disclosure.html << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Affiliate Disclosure - Better World Commentary</title>
    <meta name="description" content="Our affiliate disclosure policy for Better World Commentary">
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>Better World Commentary</h1>
            <p>Positive, solution-focused commentary on today's issues</p>
        </div>
    </header>
    
    <nav>
        <div class="container">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/category/cost-of-living/">Cost of Living</a></li>
                <li><a href="/category/workers-workplace/">Workers & Workplace</a></li>
                <li><a href="/category/healthcare-community/">Healthcare & Community</a></li>
                <li><a href="/category/climate-solutions/">Climate Solutions</a></li>
                <li><a href="/category/privacy-rights/">Privacy & Digital Rights</a></li>
                <li><a href="/category/civic-basics/">Civic Basics</a></li>
            </ul>
        </div>
    </nav>
    
    <main>
        <div class="container">
            <h1>Affiliate Disclosure</h1>
            
            <p>Better World Commentary is a participant in the Amazon Services LLC Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to Amazon.com.</p>
            
            <p>In addition, we may earn commissions through other affiliate programs when you click on links and make purchases. These commissions help support our work in providing solution-focused commentary on important social issues.</p>
            
            <p>We only recommend products that we believe will add value to our readers' efforts to address the challenges discussed in our content. Our editorial content is not influenced by affiliate partnerships.</p>
            
            <p>As an Amazon Associate, I earn from qualifying purchases made through links on this site. This does not impact the price you pay for any product.</p>
        </div>
    </main>
    
    <footer>
        <div class="container">
            <p>&copy; 2026 Better World Commentary. All rights reserved.</p>
            <p><a href="/affiliate-disclosure/">Affiliate Disclosure</a> | <a href="/privacy-policy/">Privacy Policy</a></p>
        </div>
    </footer>
</body>
</html>
EOF

# Create privacy policy page
cat > $BUILD_DIR/privacy-policy.html << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy - Better World Commentary</title>
    <meta name="description" content="Our privacy policy for Better World Commentary">
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>Better World Commentary</h1>
            <p>Positive, solution-focused commentary on today's issues</p>
        </div>
    </header>
    
    <nav>
        <div class="container">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/category/cost-of-living/">Cost of Living</a></li>
                <li><a href="/category/workers-workplace/">Workers & Workplace</a></li>
                <li><a href="/category/healthcare-community/">Healthcare & Community</a></li>
                <li><a href="/category/climate-solutions/">Climate Solutions</a></li>
                <li><a href="/category/privacy-rights/">Privacy & Digital Rights</a></li>
                <li><a href="/category/civic-basics/">Civic Basics</a></li>
            </ul>
        </div>
    </nav>
    
    <main>
        <div class="container">
            <h1>Privacy Policy</h1>
            
            <p>Your privacy is important to us. This privacy policy explains what personal data we collect and how we use it.</p>
            
            <h2>Information Collection and Use</h2>
            <p>We collect information from you when you visit our site and interact with our content. This may include your IP address, browser type, and pages visited.</p>
            
            <h2>Log Files</h2>
            <p>Like many other sites, we use log files. These files log visitors when they visit websites. The information collected includes internet protocol (IP) addresses, browser type, Internet Service Provider (ISP), date/time stamp, referring/exit pages, and number of clicks.</p>
            
            <h2>Cookies and Web Beacons</h2>
            <p>We use cookies to store information about visitors' preferences, record user-specific information on which pages the user accesses or visits, customize web page content based on visitors' browser type or other information that the visitor sends via their browser.</p>
            
            <h2>Third Party Disclosure</h2>
            <p>We do not sell, trade, or rent users' personal identification information to others.</p>
            
            <h2>Third party links</h2>
            <p>Occasionally, at our discretion, we may include or offer third party products or services on our website. These third party sites have separate and independent privacy policies. We therefore have no responsibility or liability for the content and activities of these linked sites.</p>
            
            <h2>Google Analytics</h2>
            <p>We use Google Analytics to help analyze how visitors use our site. Google Analytics collects standard internet log information and visitor behavior information in an anonymous form.</p>
            
            <h2>Consent</h2>
            <p>By using our site, you consent to our privacy policy.</p>
        </div>
    </main>
    
    <footer>
        <div class="container">
            <p>&copy; 2026 Better World Commentary. All rights reserved.</p>
            <p><a href="/affiliate-disclosure/">Affiliate Disclosure</a> | <a href="/privacy-policy/">Privacy Policy</a></p>
        </div>
    </footer>
</body>
</html>
EOF

echo -e "${GREEN}Static pages created successfully${NC}"

# Run content generator to populate with content
echo -e "${YELLOW}Generating initial content...${NC}"
cd $SOURCE_DIR
python3 content_generator.py

# Copy generated content to build directory
cp -r $SOURCE_DIR/posts $BUILD_DIR/ 2>/dev/null || echo "No posts generated yet"

# Copy generated sitemap and RSS feed
cp $SOURCE_DIR/sitemap.xml $BUILD_DIR/ 2>/dev/null || echo "No sitemap.xml generated yet"
cp $SOURCE_DIR/feed.rss $BUILD_DIR/ 2>/dev/null || echo "No feed.rss generated yet"

echo -e "${GREEN}Initial content generated${NC}"

# Set up cron job for automatic content generation
(crontab -l 2>/dev/null; echo "0 9 * * * cd $SOURCE_DIR && python3 content_generator.py") | crontab -

echo -e "${GREEN}Cron job set up for daily content generation at 9 AM${NC}"

echo -e "${GREEN}Deployment complete!${NC}"
echo -e "${YELLOW}Next steps:${NC}"
echo -e "1. Customize the site name and identity in the templates"
echo -e "2. Add your Google Analytics ID (replace G-YHM6QJDPFC)"
echo -e "3. Add your affiliate program IDs"
echo -e "4. Deploy the contents of $BUILD_DIR to your web server"
echo -e "5. Verify your domain with Google Search Console"
# Issue-Based Commentary Website

An automated content website focused on positive, left-leaning issue-based commentary that highlights problems in today's world while offering practical solutions.

## Core Values
- Workers' dignity, fair wages, consumer protection, healthcare access
- Climate solutions, privacy rights, anti-corruption, equal opportunity
- Hopeful, constructive, and grounded tone
- Problem-focused but solution-oriented

## Site Structure
1. **Cost of Living & Corporate Tricks** - fees, shrinkflation, scams
2. **Workers & Workplace Power** - rights, negotiation, organizing basics
3. **Healthcare & Community** - access, prevention, mutual aid, navigating systems
4. **Climate Solutions That Work** - local wins, policy explained simply
5. **Privacy & Digital Rights** - beginner-friendly cybersecurity and privacy
6. **Civic Basics** - how local government works; how to participate constructively

## Automation Features
- Content generator script that creates 1 new post per run
- Automatic site index updates
- Sitemap.xml and RSS feed generation
- Topic queue system for planned content
- Daily scheduled content generation via cron job

## Monetization Strategy
Ethical affiliate marketing focused on products that match the content:
- Books and educational resources
- Budgeting tools
- Privacy tools (VPNs, password managers)
- Home energy efficiency basics
- Reusable household items
- Worker gear (ergonomic tools, safety equipment)
- Learning resources

## Directory Structure
```
issue-commentary/
├── css/                 # Stylesheets
├── js/                  # JavaScript files
├── posts/               # Generated content organized by category
├── pages/               # Static pages
├── templates/           # HTML templates for generation
├── content_generator.py # Main content generation script
├── topic_queue.txt      # Queue of topics to cover
├── deploy.sh           # Deployment script
├── README.md           # This file
├── example_posts.md    # Three example posts following all rules
├── CUSTOMIZATION_CHECKLIST.md # What you need to customize
└── _build/             # Generated site ready for deployment
```

## Content Rules Implemented
- No hate or harassment, no personal attacks
- No electioneering - issue-based and educational only
- No misinformation - includes Sources section with links and dates
- Original writing only - no copying articles
- Each post includes: title, slug, meta description, hook intro, 3-7 subheads, bullet summary, listener takeaway, and related posts

## Running the System

### Generate New Content
```bash
cd /Users/davidrosser/clawd/issue-commentary
python3 content_generator.py
```

### Manual Deployment
```bash
cd /Users/davidrosser/clawd/issue-commentary
./deploy.sh
```

### Check Scheduled Content Generation
The system automatically runs content generation daily at 9 AM via cron job.

## What You Need to Customize

### 1. Sign Up for These Services
- **Google Analytics**: Create a GA4 property and replace `G-XXXXXXXXXX` with your actual ID
- **Amazon Associates**: Sign up for Amazon's affiliate program for product recommendations
- **Additional Affiliate Programs**: Consider other ethical affiliate programs that match your content

### 2. Site Identity
- Replace "Better World Commentary" with your preferred site name
- Update meta information for SEO
- Add your contact information

### 3. Legal Pages
- Review and customize the affiliate disclosure page
- Update the privacy policy with your specific practices
- Create an About page with your bio and mission

### 4. Hosting
- Deploy the `_build` directory contents to your web server
- Set up SSL/HTTPS
- Configure DNS to point to your hosting

## How to Add New Topics
Edit `topic_queue.txt` and add new topics in the format:
```
Topic Title|category-key|Brief description
```

## 30 Topic Ideas Already Included
The system comes with 30 pre-planned topics across all six categories, including:
- The True Cost of Subscription Creep
- Worker Rights in the Gig Economy
- Patient Advocacy: Getting Second Opinions
- Community Solar Programs Explained
- Encryption Basics for Regular Users
- City Council Meetings: Your Voice Matters
- And 24 more issue-based topics with practical solutions

## 3 Fully Written Example Posts
The system includes three complete example posts following all rules:
1. "The Hidden Costs of Banking: How Fee Creep Is Draining Your Wallet"
2. "Know Your Rights: Essential Worker Protections You Should Understand"
3. "Navigating Healthcare: A Guide to Getting Quality Care Without Bankruptcy"

Each includes all required elements: hook, what's wrong, why it happens, what's working, actions, sources, and related posts.

## Revenue Potential
The system is designed for ethical monetization through:
- Affiliate marketing for products that solve the problems discussed
- AdSense advertising (once traffic builds up)
- Potential premium content or newsletters in the future

The automated nature means new content is generated daily, building your site's authority and search ranking over time while you sleep.